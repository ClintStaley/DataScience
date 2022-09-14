import sys
import pandas as pd
import collections as cll;

ITGroup = cll.namedtuple('ITGroup', 'items, tids')
ItemSet = cll.namedtuple('ItemSet', 'items, sup')

def dEclat(itGroups, minSup, fSets):
   print(type(itGroups))
   print(f"Analyze {itGroups}, for {minSup}");
   for idx1, grp1 in enumerate(itGroups):
      fSets.add(ItemSet(grp1.items, len(grp1.tids)))
      for idx2, grp2 in enumerate(itGroups[idx1+1:]):
         print(idx1, idx2) 


def main():
   supSets = pd.read_pickle(sys.argv[1])
   minSup = int(sys.argv[2])
   fSets = set();

   itmSets = list(map(lambda v: ITGroup(set([v[0]]), v[1]),
    enumerate(map(set, filter(lambda s: len(s) >= minSup, supSets["userIds"])))))

   dEclat(itmSets, minSup, fSets)

main()