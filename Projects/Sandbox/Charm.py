import sys
import pandas as pd
import collections as cll;

# items: hierarchichal list, tids: simple set, sup: integer
ITGroup = cll.namedtuple('ITGroup', 'items, tids, sup')
ItemSet = cll.namedtuple('ItemSet', 'items, tids')

def flatten(itemList):
    rtn = set()
    for item in itemList:
        rtn = rtn | (flatten(item) if (type(item) is list) else {item}) 
    return rtn

def charm(itGroups, minSup, cSets):
   print(f"Analyze {itGroups}, for {minSup}");
   for idx1, grp1 in enumerate(itGroups):
      subGroups = []
      idx2 = idx1 + 1
      while (idx2 < len(itGroups)):
         grp2 = itGroups[idx2]
         mergedTids = grp1.tids & grp2.tids
         sup = len(mergedTids)
         if sup >= minSup:
            if grp1.tids == grp2.tids:         # Absorb grp2 into grp1
               grp1.items.append(grp2.items)
               del itGroups[idx2]
            else:
               idx2 += 1
               if grp1.tids < grp2.tids:       # Grp1 also supports all of grp2
                  grp1.items.append(grp2.items)
               else:             # Blending grp1 and grp2 results in new tidset
                  subGroups.append(ITGroup([grp1.items, grp2.items],
                   mergedTids, sup))

      if len(subGroups):
         charm(subGroups, minSup, cSets)
      newSet = flatten(grp1.items)
      for existingSet in cSets:
         if (newSet <= existingSet.items and existingSet.tids == grp1.tids):
            newSet = None
            break;
      if newSet != None:
         cSets.append(ItemSet(newSet, grp1.tids))

def main():
   supSets = pd.read_pickle(sys.argv[1])
   minSup = int(sys.argv[2])
   cSets = [];

   itmSets = list(map(lambda v: ITGroup([v[0]], v[1], len(v[1])),
    enumerate(map(set, filter(lambda s: len(s) >= minSup, supSets["userIds"])))))
   print("Filtered and listed")

   charm(itmSets, minSup, cSets)

   for closure in cSets:
       print(closure)

main()