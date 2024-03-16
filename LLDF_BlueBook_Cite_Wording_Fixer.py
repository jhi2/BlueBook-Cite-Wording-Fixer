
import csv
import tkinter as tk
from tkinter import ttk
import urllib
def readconfig():
    reader = csv.DictReader(open('BlueBook.csv'))
    for row in reader:
        return

config = readconfig()
window = tk.Tk()

header = ttk.Label(window,text="JohnnyTech LLDF BlueBook Cite Wording Fixer\nEnter unabbreviated cite below:")
brokencite = tk.Text(window)
def fixcite(cite):
    global config,output
    
    def replace_from_config(config, cite):
        try:
            for key, value in config.items():
                input_string = input_string.replace(key, value)
            return input_string
        except:
            pass
    try:
        fixedcite = replace_from_config(config,cite)

    except:
        pass
    try:
        output = fixedcite
    except:
        print("ERROR: THE SYSTEM CANNOT IMPORT THE FIXED CONTENT")
    

def fxc():
    fixcite(brokencite.get(1.0,"end"))
    if output == None:
        print("ERROR: INTERNAL DATA PROCESESING ERROR!\nPLEASE CONTACT JOHNNYTECH.")
    else:
        print("output:\n",output)
    
    
fixbutton = ttk.Button(window,text="Fix this cite",command= lambda:fxc())
header.pack()
brokencite.pack()
fixbutton.pack()
window.mainloop()