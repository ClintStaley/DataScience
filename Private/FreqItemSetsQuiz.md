# Frequent Itemsets Coding Quiz

The code below loads a dataframe comprising a single column "userIds" giving lists of user ids who have bought a given product, and with row labels giving the ID of the purchased product.

It produces a list of `ItemSet`s with support at least "minSup", each giving an itemset of product IDs, and a support count for that itemset. Importantly, it identifies products by their cardinal row number starting with row 0, rather than by their larger product IDs.

There are 4 missing parts, and 3 bugs in this code, each worth 5 pts on average.  Fill in the missing parts and find and fix the bugs by editing on the code.  Do not add lines of code, and do not fix anything that isn't wrong; doing so will cost points.  You may use standard Python references online.
```
import sys
import pandas as pd
import collections as cll;

ITGroup = cll.namedtuple('ITGroup', 'items, tids, sup')
ItemSet = cll.namedtuple('ItemSet', 'items, sup')

# Performe an Eclat/dEclat recursion on itGroups, a list of ITGroup tuples.
# Drop itemsets with support < minSup.  Add newly found itemsets to set fSets.  
# If topCall is true, treat itGroups as providing tidsets (top level call),
# otherwise as providing diffSets (all non-top level calls)

def dEclat(itGroups, minSup, fSets, topCall):
   for idx1, grp1 in enumerate(itGroups):
      fSets.append(____________________________)  
      subGroups = []
      for idx2, grp2 in enumerate(itGroups[_______________]): 
         newItems = grp1.items | grp2.items

         diffTids = ______________________ if topCall else grp2.tids - grp1.tids
         sup = len(diffTids) 
         if sup >= minSup:
            subGroups.append(ITGroup(newItems, diffTids, sup))
      if len(subGroups):
         dEclat(subGroups, minSup, fSets, True)

def main():
   supSets = pd.read_pickle(sys.argv[1])
   minSup = int(sys.argv[2])
   fSets = [];
   itmSets = list(________(lambda v: ITGroup(set([v[0]]), v[1], (v[1])),
    enumerate(map(set, filter(lambda s: len(s) >= minSup, supSets["userIds"])))))

   dEclat(itmSets, minSup, fSets, True)

   print(list(filter(lambda s: len(s.items) > 1, fSets)))

main()
```