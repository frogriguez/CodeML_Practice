# Imports

from Bio.Phylo.PAML import codeml
from Bio.Phylo.PAML import baseml
from Bio.Phylo.PAML import yn00
from Bio.Phylo.PAML.chi2 import cdf_chi2 

#CodeML Path
#cmlpath = r"C:\Users\Zach\paml4.8\bin\codeml"
#cmlpath = r"C:\Users\Zach\Anaconda3\Lib\site-packages\Bio\Phylo\PAML\codeml"
cmlpath = r"C:\Users\Zach\bin\codeml.exe"

#Initialization
cml = codeml.Codeml()

#cml.alignment = "lysozyme.nuc"  #tells codeML the alignment name
#cml.tree = "lysozyme.tree"       #tells codeML the tree name
cml.working_dir = "./workingdir"   #sets working directory to store output files
cml.read_ctl_file("lysozyme_M0.ctl") #sets control file
#cml.out_file = "null.out"    #sets output file name
cml.run(command=cmlpath, verbose=True)
