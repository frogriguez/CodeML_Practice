# This script returns the p-value from chi2 distributions
# for likelihood ratio tests

# Imports
from Bio.Phylo.PAML.chi2 import cdf_chi2

l1 = -5985.635237
l0 = -6018.63301

df = 1
statistic = 2*(l1 - l0)
chi2 = cdf_chi2(df, statistic)
print ("Chi2:",chi2)