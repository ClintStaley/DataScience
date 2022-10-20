# Spade Algorithm Quiz #

<div style="text-align: right">Name ________________________________________</div>

Here is an initial level of the Spade algorithm for a set of sequences over the GATC alphabet.  

1. **10 pts** Reconstruct the actual set of sequences, including filling in the missing X and Y values on the second and third rows.  (Check this carefully)
2. **20 pts** Use Spade to construct all subsequences beginning with A or C having minsup 3,
showing all generated nodes in the Spade tree for those subsequences. (There are 6 such subsequences including A and C)

```
A           C            G               T
2,4,6       1            5,7             3
2,5,7       6            1               3, Y
2, X        3, 8         5               1, 4, 7
```

Actual database of sequences:

X = 6, Y = 4

$S_1$: CATAGAG\
$S_2$: GATTACA\
$S_3$: TACTGATC

Spade tree for subsequences having A or C as initial symbol:

**General idea: 4pts, Correct nodes 16pts, -4 per incorrect**

```
A           C            G               T
2,4,6       1            5,7             3
2,5,7       6            1               3, 4
2, 6        3, 8         5               1, 4, 7


AA      AC    AG     AT              CA     CC    CG    CT
4,6     -     5,7    3               2,4,6  -     5,7   3
5,7     6     -      3,4             7      -     -     -
6       3,8   5      4,7             6      8     5    4,7


AAA     AAT   ATA    ATT             CAA
6       -     4,6    -               4,6
7       -     5,7    4               -
-       7     6      7               -

              ATAA
              6
              7
              -
```
