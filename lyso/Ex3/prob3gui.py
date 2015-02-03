#imports
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.backend_bases import key_press_handler
import random
from matplotlib.figure import Figure as plot
from tkinter import *
import numpy as np
from Bio.Phylo.PAML import codeml

#CodeML Path
cmlpath = r"C:\Users\Zach\bin\codeml.exe"
cml = codeml.Codeml()

#calculates lambda given Ne & k (gene copies)
def calc(Ne,k):
	n = 4*Ne #numerator
	d = (k*(k-1)) #denominator
	y = n/d
	lambd = (1/y)
	return lambd

def codeml:
	cml.alignment = "lysozyme.nuc"  #tells codeML the alignment name
	cml.tree = "lysozyme.tree"       #tells codeML the tree name
	cml.working_dir = "./workingdir"   #sets working directory to store output files
	cml.read_ctl_file("codeml.ctl")
	cml.run(command=cmlpath)

# I don't think I did this correctly. Just because k1 & k2 coalesce after 10 generations
# doesn't mean that k3 & k4 cannot also coalesce after 10 generations
# right now I have it set where if k1 & k2 coalesce after 10 generations, as well as K3 & k4
# the current generation time will be 20. I think I need to only keep the largest coalescent time.
	
def simulation():
	gentimes = []   #array to hold generation times for total coalescence
	first = []		#array to hold times for first coalescent event
	Ne = float(e1.get())  #sets Ne to whatever the user typed in
	k = float(e2.get())   #sets k to whatever the user typed in
	
	for x in range(5000):
		one,mrca = generations(Ne,k)
		gentimes.append(mrca)   #appends total to array (gentimes)
		first.append(one)		#appends time for first coalescent event to array (first)
	np.sort(gentimes)
	m = np.mean(gentimes)
	firstavg = np.mean(first)
	
	
	a = f.add_subplot(111)
	a.clear()    #clear figure so you can graph again
	a.hist(gentimes)
	a.set_title("Coalescent Distribution")
	a.set_xlabel("Generations")
	a.set_ylabel("Frequencies")
	canvas.show()
	print ("average generations to MRCA:",m)
	print ("average generations for first coalescent:",firstavg)


#create Widget Grid (gui) named "gui"
gui = Tk()
gui.title("Coalescent Parameters") #grid title


Label(gui, text="Ne:").grid(row=0)  #Labels entry1: "Ne"
Label(gui, text="k:").grid(row=1)   #Lables entry2: "k"

#defines user entry spots
e1 = Entry(gui)
e2 = Entry(gui)
e1.grid(row=0, column=1) #puts an Ne entry spot in 0,1
e2.grid(row=1, column=1) #puts a k entry spot in 1,1

#Makes buttons
Button(gui, text='Quit', command=gui.quit).grid(row=3, column=1, sticky=W, pady=4)  #Creates a quit button
Button(gui, text='Graph', command=simulation).grid(row=3, column=2, sticky=W, pady=4)  #creates a graph button, executes simulation function on press

#creates figure frame
frame=Frame(gui)
frame.grid(row=0,rowspan=5, column=3)
f = plot(figsize=(6,5), dpi=100)

#Plots figure (graph) into gui
canvas = FigureCanvasTkAgg(f, master=frame)
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
gui.mainloop( )
