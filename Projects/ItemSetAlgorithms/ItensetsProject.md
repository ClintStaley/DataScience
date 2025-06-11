# Itemsets Project

## Overview
In this project, you'll analyze a large set of transactions with many items, and search for two patterns: 

 * itemsets that comprise a unit -- all appear together in transactions
 * association rules where two items result in the presence of a third

## Specification

You'll use two files, supplying the filenames in response to an initial prompt:

`Enter config file name: config1.json`\
`Enter data file name: cstaley_items.txt`

### Configuration file
The configuration file specifies various parameters surrounding the two searches described in the overview.  

Read this file using the javax.json package; don't write your own JSON parser!  And arrange to obtain that package by building a Maven project, and including the javax.json as a dependency, so Maven will automatically fetch it for you.  (It's not in the standard libraries.)

### Data file
You'll get a data file specific to you, named `<login>_items.txt`.  It has the format:

```
<numItems>
<transaction lists>
```

The `<numItems>` gives the number of different items, which are identified by id numbers from 0 to <numItems>-1.  Be ready to accommodate values up to 30,000.  

The `<transaction lists>` give transactions, one per line.  Each transaction is a blank-separated list of item IDs, not necessarily in sorted order, and possibly with repeated items.  Ignore the repeats if so.  Expect transaction counts up to 100,000,000 and transaction sizes averaging up to 30.  Identify transactions by their row number, from 0.

### Computation
You are seeking within these transactions two things

1. Maximal itemsets of at least 5 with whole-itemset lift and leverage as specified in the config file.  With the right lift and leverage, these can be seen as purchase units, e.g. the parts for some device, or spices for a recipe.

2. Causal relationships of form AB -> C, where a pair items results in the third item, again with lift and leverage as specified in the config file.

The configuration file will specify which algorithm to use for these: Aprior, eClat/deClat, or FPGrowth.  Use an OO Strategy pattern, setting up a general interface with three implementations.  Part of the exercise is to test the relative speed and effectiveness of these algorithms.

### Output
Print to standard output:

1. All itemsets meeting criterion 1, starting with their lift and leverage and followed by the item numbers, in sorted order.  For each, also indicate whether it is productive or nonproductive as an itemset, e.g.

`Lift: 2.0  Lvr: .2  98 132 453 751 887 998 nonproductive`

2. All association rules meeting criterion 2, in form:\
 `<lift> <leverage> AB -> C`, e.g.

`Lift 2.0 Lvr: .1  42 987 -> 886`

