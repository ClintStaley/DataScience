# Ukkonen Project Spec

## Overview
Implement a Ukknonen tree in Java, or if you like, C/C++, to represent a set of very large
strings, and then search for patterns in those strings.

## Program Operation
The program prompts for the name of a text file giving the strings to search, and reads that file to form a Ukkonen tree.  The file's first line gives an alphabet of characters, followed by one or more successive lines giving (large) strings of that alphabet.  Number the strings from 0, based on the lines.  Assume no more than 255 distinct chars in the alphabet, and that $ will *not* be one of them. Example:

```
gatc                         (standard alphabet for DNA sequences)
gataccagattaccag .... cagt   (possinbly multimillion character string 0)
ggattccagattcgaa .... ccct   (possinbly multimillion character string 1)
etc
```

The program then repeatedly prompts for the name of other files, which are similarly structured but with shorter strings, and without
the preceding alphabet line.  Label these 'A', 'B', etc.   For each test string it reports all locations in which it appears in the original large string set, e.g.:

```
String A appears at: (0, 2033) (0, 343221) (1, 10) (2, 2033)
String B appears at: (0, 314455) (2, 34) (2, 593829)
...
```
Report locations sorted first by data string, and then by offset within the string.


