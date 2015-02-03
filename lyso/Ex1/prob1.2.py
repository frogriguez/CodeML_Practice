# Imports

from Bio.Phylo.PAML import codeml
from Bio.Phylo.PAML import baseml
from Bio.Phylo.PAML import yn00
from Bio.Phylo.PAML.chi2 import cdf_chi2 

#CodeML Path
cmlpath = r"C:\Users\Zach\bin\codeml.exe"

#Initialization
cml = codeml.Codeml()

cml.alignment = "lysozyme.nuc"  #tells codeML the alignment name
cml.tree = "lysozyme_tagged.tree"       #tells codeML the tree name
cml.out_file = "results.out"    #sets output file name
cml.working_dir = "./workingdir"   #sets working directory to store output files
cml.read_ctl_file("lysozyme_Branch.ctl") #sets control file
results=cml.run(command=cmlpath, verbose=True) #run program, sets codeml path, displays output
