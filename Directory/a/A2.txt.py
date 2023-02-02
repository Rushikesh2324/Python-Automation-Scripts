import os
from sys import*

def 

def main():
    print("Directory watcher application ")

    if (len(argv)<2):
        print("Insufficient arguments ")
        exit()


    if (argv[1]=="-h"):
        print("This script will travel directory and display the names of all entries")
        exit()

    if (argv[1]=="-u"):
        print("Usage : Application_name Directory_Name")
        exit()

if __name__=="__main__":
    main()    
