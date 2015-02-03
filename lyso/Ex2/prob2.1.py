#Practice Site-Specific Positive Selection

# Imports
from Bio.Phylo.PAML import codeml

#CodeML Path
cmlpath = r"C:\Users\Zach\bin\codeml.exe"

#Initialization
cml = codeml.Codeml()
cml.working_dir = "./workingdir"   #sets working directory to store output files
cml.read_ctl_file("HIVenvSweden.ctl") #sets control file
cml.run(command=cmlpath, verbose = True)
