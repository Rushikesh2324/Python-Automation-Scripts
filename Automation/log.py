#importing the module 
import logging 
import psutil
#now we will Create and configure logger 
logging.basicConfig(filename="std.log", 
					format='%(asctime)s %(message)s', 
					filemode='w') 

#Let us Create an object 
logger=logging.getLogger() 

#Now we are going to Set the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG) 

def ProcessDisplay():
    listprocess=[]
    
    for proc in psutil.process_iter():
        try:
            pinfo=proc.as_dict(attrs=['pid','name','username'])

            listprocess.append(pinfo);
        except(psutil.NoSuchprocess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    return listprocess        


#some messages to test
def main():
   print("Marvallous Infosystem : Python Automation & Machine Learning")

   print("Process Moniter ")

   listprocess=ProcessDisplay()
   #logger.debug(listprocess)
   for elem in listprocess:
    logger.debug(elem)

if __name__ == "__main__":
    main()