from sys import *
from os import *
                

def main():
    print("-----------Marvallous Infosystem Automation------------")
    print("Automation script started with name : ",argv[0])

    if (len(argv)!=2):
        print("Error : Insufficient arguments ")
        print("use -h for help and use -u for usage of the script")
        exit()


    if (argv[1]=="-h")or (argv[1]=="-H"):
        print("Help : This script is used to perform______ ")
        exit()

    if (argv[1]=="-u")or (argv[1]=="-U"):
        print("Usage : Provide______ number of argument as")
        print("first Argument as : _______")
        print("Second Argument as : _______")
        exit()    

if __name__ == "__main__":
    main()