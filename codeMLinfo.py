#Practice using PAML


# Imports

from Bio.Phylo.PAML import codeml
from Bio.Phylo.PAML import baseml
from Bio.Phylo.PAML import yn00
from Bio.Phylo.PAML.chi2 import cdf_chi2 

# 1. Intro

# 1.1 Initialization:

	# Notes: The interface is implemented as an object which maintains program options. 
	#        In order to run codeml, typically one provides (1) a control file which indicates 
	#        the locations of an alignment file, (2) a tree file and (3) an output file, along with 
	#        a series of options dictating how the software is to be run. In the Codeml object, 
	#        the three file locations are stored as string attributes. The three file locations, 
	#        as well as the location of the desired working directory, may be specified in the 
	#        Codeml constructor as follows:


#Alternatively: cml = codeml.Codeml(alignment = "align.phylip", tree = "species.tree", out_file = "results.out", working_dir = "./scratch")
.alignment = "align.phylip"  #tells codeML the alignment name
.tree = "species.tree"       #tells codeML the tree name
.out_file = "results.out"    #sets output file name
.working_dir = "./scratch"   #sets working directory to store output files

# 1.2 Options: 
#	.print_options()             #prints options
#	.get_option("option")        #retrieves option values
#	.set_options(option = value) #set option to a value. 
#		>Note: Setting option to "None" will cause codeml to ignore option
#	.write_ctl_file()            #writes options to control file
#		>Note: This is done automatically when you run()
#	.read_ctl_file("codeml.ctl") #reads in options from control file

# 1.2.2 Set Options
verbose = None
CodonFreq = None
cleandata = None
fix_blength = None
NSsites = None
fix_omega = None
clock = None
ncatG = None
runmode = None
fix_kappa = None
fix_alpha = None
Small_Diff = None
method = None
Malpha = None
aaDist = None
RateAncestor = None
aaRatefile = None
icode = None
alpha = None
seqtype = None
omega = None
getSE = None
noisy = None
Mgene = None
kappa = None
model = None
ndata = None

# 1.3 Running the program

.run()	#runs codeml with current options

#	verbose (boolean)   #set this argument to True to see all of the output as it is generated. This is useful if codeml is failing and you need to see its error messages.
#	parse (boolean)     #set to False to skip parsing the results. run() will instead return None
#	.read_ctl_file (string)   #provide a path to an existing control file to execute. The file is not 
#						>parsed and read into Codeml's options dictionary. If set to None (default), the options dictionary is written to a control file, which is then used by codeml.
#	command (string)    #provide a path to the codeml executable. This is set to "codeml" by default, so if the program is in your system path, that should suffice. 
#						>If it's not in your system path or, for example, if you use multiple versions of PAML, you may instead provide the full path to the executable.

# 1.4 Results

results = .read()
dict.get(key)  #returns a specific dictionary result, based on desired key

# 2.0 CodeML
cml = codeml.Codeml()

cml.alignment = "align.phylip"  #tells codeML the alignment name
cml.tree = "species.tree"       #tells codeML the tree name
cml.out_file = "results.out"    #sets output file name
cml.working_dir = "./scratch"   #sets working directory to store output files

cml.run()

# 3.0 BaseML
bml = baseml.Baseml()
#	>Note: use same methods/attributes as CodeML, just replace with 'bml'

# 4.0 yn00
yn = yn00.Yn00()
#	>Note: use same methods/attributes as CodeML, replace with 'yn' 
#	>Note: you do not need a tree file


# 5.0 Chi-Squared
df = 2	#sets degrees of freedom
statistic = 7.21  #sets chi2 test statistic
cdf_chi2(df, statistic)   #returns chi2 value
