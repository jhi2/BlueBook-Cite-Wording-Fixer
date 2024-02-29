print("JohnnyTech LLDF BlueBook Cite Wording Fixer - Running imports...")
import csv
import tkinter as tk
from tkinter import ttk
import urllib
print("Definiiing varibles...")
def readconfig():
    reader = csv.DictReader(open('BlueBook.csv'))
    for row in reader:
        return row
print("Reading configuration table...")
config = readconfig()
print("Initalizing GUI...")
window = tk.Tk()
window.title("JohnnyTech LLDF BlueBook Cite Wording Fixer")
window.geometry("500x500")
print("Initalizing GUI elements...")
header = ttk.Label(window,text="JohnnyTech LLDF BlueBook Cite Wording Fixer")
brokencite = tk.Text(window)
cflbl = ttk.Label(window,text="Your fixed cite is here:")
fxc = tk.Text(window)
print("Definiiing varibles...")
def fixcite():
    print("Making varribles global...")
    global config
    print("Getting cite from input box...")
    cite = brokencite.get("1.0","end-1c")
    print("Searching string...")
    print("Defineing varribles...")
    def replace_from_config(config, input_string):
        print("Going through items...")
        for key, value in config.items():
            print("Replacing...")
            input_string = input_string.replace(key, value)
        return input_string
    print("Calling fucction...")    
    fixedcite = replace_from_config(config,cite)
    fxc.insert("1.0",fixedcite) 
    
    

    
    
    
    
print("Initalizing GUI elements...")   
fixbutton = ttk.Button(window,text="Fix this cite",command=lambda: fixcite())
print("Applying GUI elements...")
header.pack()
brokencite.pack()
fixbutton.pack()
cflbl.pack()
fxc.pack()


window.mainloop()