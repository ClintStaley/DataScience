import sys
import pandas as pd
import collections as cll;

ITGroup = cll.namedtuple('ITGroup', 'items, tids')
ItemSet = cll.namedtuple('ItemSet', 'items, sup')

def dEclat(itGroups, minSup, fSets):
   # print(f"Analyze {itGroups}, for {minSup}");
   for idx1, grp1 in enumerate(itGroups):
      fSets.append(ItemSet(grp1.items, len(grp1.tids)))
      subGroups = []
      for idx2, grp2 in enumerate(itGroups[idx1+1:]):
         newItems = grp1.items | grp2.items
         newTids = grp1.tids & grp2.tids
         if len(newTids) >= minSup:
            subGroups.append(ITGroup(newItems, newTids))
      if len(subGroups):
         dEclat(subGroups, minSup, fSets)

def main():
   supSets = pd.read_pickle(sys.argv[1])
   minSup = int(sys.argv[2])
   fSets = [];

   print("Done reading")
   itmSets = list(map(lambda v: ITGroup(set([v[0]]), v[1]),
    enumerate(map(set, filter(lambda s: len(s) >= minSup, supSets["userIds"])))))
   print("Filtered and listed")

   dEclat(itmSets, minSup, fSets)

   print(list(filter(lambda s: len(s.items) > 1, fSets)))

main()