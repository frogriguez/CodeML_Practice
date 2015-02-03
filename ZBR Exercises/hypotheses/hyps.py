# Imports
from Bio.Phylo.PAML import codeml

#CodeML Path
cmlpath = r"C:\Users\Zach\bin\codeml.exe"

#Initialization
cml = codeml.Codeml()
cml.working_dir = "./workingdir"   #sets working directory to store output files
cml.read_ctl_file("h1.ctl")

#runs codeml
cml.run(command=cmlpath, verbose = True)
