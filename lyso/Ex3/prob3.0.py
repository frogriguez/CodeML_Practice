# Imports
from Bio.Phylo.PAML import codeml

#CodeML Path
cmlpath = r"C:\Users\Zach\bin\codeml.exe"

#Initialization
cml = codeml.Codeml()

cml.alignment = "lysozyme.nuc"  #tells codeML the alignment name
cml.tree = "lysozyme.tree"       #tells codeML the tree name
cml.working_dir = "./workingdir"   #sets working directory to store output files
cml.read_ctl_file("codeml.ctl")
cml.run(command=cmlpath, verbose=True)
