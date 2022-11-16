import sys, pickle
import pandas as pd
import collections as cll;

# items: hierarchichal list, tids: simple set, sup: integer
ITGroup = cll.namedtuple('ITGroup', 'items, tids, sup')

def flatten(itemList):
    rtn = set()
    for item in itemList:
        rtn = rtn | (flatten(item) if (type(item) is list) else {item}) 
    return rtn

def charm(itGroups, minSup, cSets):
   for idx1, grp1 in enumerate(itGroups):
      subGroups = []
      idx2 = idx1 + 1
      while (idx2 < len(itGroups)):
         grp2 = itGroups[idx2]
         jointTids = grp1.tids & grp2.tids
         sup = len(jointTids)
         if sup >= minSup:
            if grp1.sup == sup and grp2.sup == sup:      # Absorb grp2 into grp1
               # print(f"Absorb {grp2.items} into {grp1.items}\n")
               grp1.items.append(grp2.items)
               del itGroups[idx2]
               idx2 -= 1
            else:
               if grp1.sup == sup:       # Grp1 also supports all of grp2
                  # print(f"Add {grp2.items} to {grp1.items}\n")               
                  grp1.items.append(grp2.items)
               else:             # Blending grp1 and grp2 results in new tidset
                  subGroups.append(ITGroup([grp1.items, grp2.items],
                   jointTids, sup))
         idx2 += 1

      if len(subGroups):
         charm(subGroups, minSup, cSets)

      newSet = flatten(grp1.items)
      for existingSet in cSets:
         if (newSet <= existingSet.items and existingSet.tids == grp1.tids):
            newSet = None
            break;
      if newSet != None:
         cSets.append(ITGroup(newSet, grp1.tids, grp1.sup))

def main():
   supSets = pd.read_pickle(sys.argv[1])
   minSup = int(sys.argv[3])

   cSets = [];

   itmSets = list(map(lambda v: ITGroup([v[0]], v[1], len(v[1])),
    enumerate(map(set, filter(lambda s: len(s) >= minSup, supSets["userIds"])))))

   itmSets.sort(key=lambda x: len(x.tids))
   print(f"Filtered, listed and sorted\n")

   charm(itmSets, minSup, cSets)
   
   pickle.dump(cSets, open(sys.argv[2], "wb"))
   checkRead = pickle.load(open(sys.argv[2], "rb"))
   print(f"Read/write check\n{checkRead[:10]}\n{checkRead[-10:]}\n")

main()