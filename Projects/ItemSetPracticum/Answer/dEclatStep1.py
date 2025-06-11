import sys
import pandas as pd

ItemSet = namedtuple('ItemSet', 'items, tids')

def dEclat(itmSets, minSup, fSets):
    print(f"Analyze {itmSets}, for {minSup}");
    # for idx, set in enumerate(itmSets):
    #   fSets.add({'set': set[0], 'sup': len(set[1])})


def main():
    supSets = pd.read_pickle(sys.argv[1])
    minSup = int(sys.argv[2])
    fSets = set();

    itmSets = list(map(lambda v: ItemSet(set(v[0]), v[1]),
        enumerate(map(set, filter(lambda s: len(s) >= minSup, supSets["prdIds"])))))

    dEclat(itmSets, minSup, fSets)

main()