import sys
import pandas as pd
import collections as cll;

ITGroup = cll.namedtuple('ITGroup', 'items, tids, sup')
ItemSet = cll.namedtuple('ItemSet', 'items, sup')

def dEclat(itGroups, minSup, fSets, topCall):
   print(f"Analyze {itGroups}, for {minSup}");
   for idx1, grp1 in enumerate(itGroups):
      fSets.append(ItemSet(grp1.items, grp1.sup))
      subGroups = []
      for idx2, grp2 in enumerate(itGroups[idx1+1:]):
         newItems = grp1.items | grp2.items
         diffTids = grp1.tids - grp2.tids if topCall else grp2.tids - grp1.tids
         print(f"{newItems} has diffs {diffTids}")
         sup = grp1.sup - len(diffTids)
         if sup >= minSup:
            subGroups.append(ITGroup(newItems, diffTids, sup))
      if len(subGroups):
         dEclat(subGroups, minSup, fSets, False)

def main():
   supSets = pd.read_pickle(sys.argv[1])
   minSup = int(sys.argv[2])
   fSets = [];

   itmSets = list(map(lambda v: ITGroup(set([v[0]]), v[1], len(v[1])),
    enumerate(map(set, filter(lambda s: len(s) >= minSup, supSets["userIds"])))))
   print("Filtered and listed")

   dEclat(itmSets, minSup, fSets, True)

   print(list(filter(lambda s: len(s.items) > 1, fSets)))

main()