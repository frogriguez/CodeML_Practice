# Imports
from Bio.Phylo.PAML import codeml
from Bio.Phylo.PAML.chi2 import cdf_chi2

def chi2 (df, statistic):
chi2 = cdf_chi2(df, statistic)
return (chi2)


#CodeML Path
cmlpath = r"C:\Users\Zach\bin\codeml.exe"

#Initialization
cml = codeml.Codeml()
cml.working_dir = "./workingdir"   #sets working directory to store output files
cml.read_ctl_file("filename.ctl")  #runs codeml using options in this control file

#runs codeml
cml.run(command=cmlpath, verbose = True)

lnL1 = dict.get(lnL) #returns lnL value




