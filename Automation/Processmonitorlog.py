
from sys import *
from os import *
import time

import psutil
import os




def ProcessDisplay(log_dir="Marvallous "):
    listprocess=[]

    if not os.path.exist(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass    

    Separator="-"*80
    log_path=os.path.join(log_dir,"MarvallousLog%s.log"%(time.ctime()))        
    f=open(log_path,'w')
    f.write(Separator+"\n")
    f.write("Maevellous Infosystems Process Logger : "+time.ctime()+"\n")
    f.write(Separator+"\n")

    for proc in psutil.process_iter():
        try:
            pinfo=proc.as_dict(attrs=['pid','name','username'])
            vms= proc.memory_info().vms/(1024*1024)
            pinfo['vms']=vms
            listprocess.append(pinfo);
        except(psutil.NoSuchprocess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    for element in listprocess:
        f.write("%s\n" % element)    


def main():
    print("----------- Marvellous Infosystems Automations -----------")

    print("Automation script started with name : ", argv[0])

    if(len(argv) != 2):
        print("Error : Insufficient arguments")
        print("Use -h for help and use -u for usage of the script")
        exit()

    if((argv[1] == "-h") or (argv[1] == "-H")):
        print("Help : This script is used to perform _____________")
        exit()

    if((argv[1] == "-u") or (argv[1] == "-U")):
        print("Usage : Application Name Absolutepath_of_Directory")
       
        exit()

    try:
        ProcessDisplay((argv[1]))
    except ValueError:
        print("Error : Invalid datatype of input")    
    except Exception:
        print("Error : Invalid input")    

if __name__ == "__main__":
    main()