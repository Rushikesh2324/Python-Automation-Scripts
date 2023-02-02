import os
from sys import *

def Directory_Watcher(Dir_Name):
    print("Inside directory watcher method")
    print("Name of input directory : ",Dir_Name)

    for foldername, subfolder, Filenames in os.walk(Dir_Name):
        print("Folder name is : "+foldername)
        for subf in subfolder:
            print("Subfolder name of "+foldername+" is "+subf)
        for fnames in Filenames:
            print("File inside folder "+foldername+" is "+fnames)
        print(" ")

def main():
    print("Directory watcher application")

    if(len(argv) < 2):
        print("Insufficient arguments")
        exit()

    if(argv[1] == "-h"):
        print("This script will travel the directory and display the names of all entries")
        exit()

    if(argv[1] == "-u"):
        print("Usage : Application_name Direcory_Name")
        exit()

    Directory_Watcher(argv[1])

if(__name__ == "__main__"):
    main()