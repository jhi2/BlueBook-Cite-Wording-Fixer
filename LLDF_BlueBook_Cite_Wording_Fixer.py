print("JohnnyTech LLDF BlueBook Cite Wording Fixer - running imports...")
import csv
import tkinter as tk
from tkinter import ttk
import urllib
print("Definiiing varibles...")
spacewords = ["District of Columbia","Los Angeles","New York","San Francisco"]
def readconfig():
    reader = csv.DictReader(open('BlueBook.csv'))
    for row in reader:
        return
print("Reading configuration table...")
config = readconfig()
print("Initalizing GUI...")
window = tk.Tk()
print("Initalizing GUI elements...")
header = ttk.Label(window,text="JohnnyTech LLDF BlueBook Cite Wording Fixer")
brokencite = tk.Text(window,text="Enter your bad cite here...")
print("Definiiing varibles...")
def fixcite():
    print("Making varribles global...")
    global config,spacewords
    
    
fixbutton = ttk.Button(window,text="Fix this cite")

window.mainloop()