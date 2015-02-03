# This script returns the p-value from chi2 distributions
# for likelihood ratio tests

# Imports
from Bio.Phylo.PAML.chi2 import cdf_chi2


df = 1
statistic = 24.26
chi2 = cdf_chi2(df, statistic)
print ("Chi2:",chi2)