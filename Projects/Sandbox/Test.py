import sys
import numpy as np

print(sys.argv[4])
set1 = {2, 3, 1}
set2 = {3,  2, 1}
print(set1, set2, set1 == set1)

list = [1, 2, 3, 4, 5]
idx = 0
while idx < len(list):
    print(idx, list[idx])
    if list[idx] == 3:
        del list[idx]
    else:
       idx += 1

print(list)
