# ItemSets Coding Project
This project will produce high-confidence inferences from the per-user itemsets provided
by the electronics-store ks.csv file provided via Canvas.  It has several phases,
roughly reflecting the typical phases of a professional data analysis project.

## Phase 1 Clean and organize the data

### P1 Step 1 Plan the data reorganization (due 10p 9/7)
The provided file does not provide a direct mapping from user id to sets of
purchased product ids by that user.  And not all rows are even useful to an
itemset analysis seeking useful association rules.

A good data science process includes a careful review of the data, and a plan to
"clean" it in appropriate ways.  Review the provided csv files (you may find
the Orders100.csv an easier starting point).  Determine which rows are actually
useful.  (At least two filters are needed to eliminate nonuseful rows).  

Then, determine what final dataframe structure you'd like in order to best 
support a Eclat/dEclat algorithm.  (Consider the three structures in our
example database.)

Create a subdirectory Itemsets in your repo. Create a short file Analysis.md in
that subdirectory summarizing your results.  Submit this md file and the
corresponding HTML file to the relevant Canvas assignment for my approval 
before proceeding.

(Learn MD if you haven't already.  It's an excellent format for Git repository 
documentation since it merges well.  Edit your Markdown in VSCode, using 
ctl-K V to show a preview and ctl-K , to generate HTML)

### P2 Step 2 Write the program to produce your desired format
Use Pandas to write a program that inputs a given CSV file (first commandline argument)
and prints basic stats on the products, orders and customers.  It then performs 
the cleaning and reorganization you planned in the prior step, 
producing a Pandas Dataframe as its final product.  It writes the DataFrame to
the specified output file (second commandline argument), and then reads it back
in and prints it, to confirm successful file save. 

A few important points:
 * Do not write any loops or if-statements in this code.  Use Pandas Dataframes,
 groupBy, etc to do the work.  My implementation is **10 lines long**.  Yours
 should be comparably brief.
 * You may choose any file format you like, but be sure it loads and saves quickly with the full dataset.

```
clint@rifle:~/DataScience/Projects/Sandbox$python3 Analyze.py Orders10000.csv Orders10000.zip
Reading Orders10000.csv
Number of products: 3186
Number of orders: 8260
Number of customers: 6763
Read/write check 
product_id
1515966223509088493                              [1.515915625512659e+18]
1515966223509088497                             [1.5159156254510305e+18]
1515966223509088498    [1.5159156254556063e+18, 1.5159156254506296e+1...
1515966223509088499    [1.515915625453577e+18, 1.515915625456618e+18,...
1515966223509088502                             [1.5159156254429404e+18]
                                             ...                        
2273948319141068839      [1.515915625455605e+18, 1.5159156254514947e+18]
2298437344820200326                             [1.5159156254541414e+18]
2298437346070102964                             [1.5159156254449859e+18]
2298437347152233469                             [1.5159156254748726e+18]
2298437347429056895                             [1.5159156254580431e+18]
Name: user_id, Length: 2185, dtype: object
```