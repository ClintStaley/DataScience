# Read a numpy array from the tsv file provided as the first argument. 
# Compute the correlation matrix of the columns of that array, zero out the
# diagonal, and print the argmax of the absolute values of each row, one per line.

import numpy as np
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python CheckCorrelation.py Data.tsv")
        sys.exit(1)
        
    data = np.loadtxt(sys.argv[1])
    correlation = np.corrcoef(data, rowvar=False)
    np.fill_diagonal(correlation, 0)
    max_correlation = np.argmax(np.abs(correlation), axis=1)
    # Print each row of max_correlation, one per line
    print("\n".join(max_correlation[:].astype(str)))