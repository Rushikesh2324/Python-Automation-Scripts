import os
import time
import psutil
import urllib3
import smtplib
import schedule
from sys import *
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

def is_Connected():
    try:
        urllib3.urlopen('http://216.58.192.142',timeout=1)
        return True
    except urllib3.URLError as err:
        return False


def Mailsender(filename,time):
    try:
        fromaddr="withvision2022@gmail.com"
        toaddr="gambhirerushikesh.grs@gmail.com"

        msg=MIMEMultipart()

        msg['from']=fromaddr
        msg['To']=toaddr
    
    
        body="""
        Hello %s,
        Welcome to Marvallous Infosystem.
        please find attached document which contains log of Running process
        log file is created at : %s

        This is auto generated mail.

        Thinks & Regards,
        Rushikesh Gambhire
        Marvallous Infosystem
        """%(toaddr,time)

        Subject="""
        Marvallous Infosystem Process log generated at:%s
        """%(time)

        msg['Subject']=Subject
        msg.attach(MIMEText(body,'plain'))
        attachment=open(filename,"rb")
        P=MIMEBase('application','octet-stream')
        P.set_payload((attachment).read())
        encoders.encode_base64(P)
        P.add_header('Content-Disposition',"attachment; filename=%s" % filename)
        msg.attach(P)

        s=smtplib.SMTP('smpt.gmail.com',587)
        s.starttls()
        s.login(fromaddr,"withvision2022@gmail.com")

        text=msg.as_string()
        s.sendmail(fromaddr,toaddr,text)
        s.quit()
        print("Log file successfully sent through mail")
    except Exception as E:
        print("Unable to send mail.",E)


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

    print("Log file is Sucessfully generated at location %s"%(log_path))

    connected=is_Connected

    if connected:
        startTime=time.time()
        Mailsender(log_path,time.ctime())
        endTime=time.time()

        print('Took %s second to send mail'% (endTime-startTime))
    else:
        print("There is no internet connection ")    


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