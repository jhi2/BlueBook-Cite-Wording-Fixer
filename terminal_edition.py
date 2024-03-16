print("TERMINAL(LITE) EDITION OPENED!")
import csv
csvpath = input("ENTER ABSOLUTE PATH OF CONFIGURATION FILE(BlueBook.csv)")
def readconfig():
    reader = csv.DictReader(open(csvpath))
    for row in reader:
        return row
config = readconfig()
def fixcite():
    global config,output

    cite = input("Enter your old(unabbriviated) cite below:")
    def replace_from_config(config, input_string):
        print("Going through items...")
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
    try:

        print("Your fixed cite is below:\n%s")%output
    except:
        print("ERROR")
fixcite()
