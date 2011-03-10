import os  
import time  
import sys  
 
from java.util import Date  
from java.text import SimpleDateFormat  

t = Date()  
today=SimpleDateFormat("dd_MMM_HH:mm").format(Date())  
user='weblogic'
URL='127.0.0.1' 

src="/home/danyboy/apps/nxtcomp/wl10mp3/bck"  
bksrc="/home/danyboy/apps/nxtcomp/wl10mp3/bck"  
dpath="/home/danyboy/apps/wl10mp3/user_projects/domains/wlsnxt2"  
ECODE='\033[0m \n'  
G='\033[1;40;32m'  
R='\033[1;40;31m'  
deploylist=['FillOrderWeb.war','ServiciosOE.war']  

def backup():  
    try:  
        # Creating the Backup with Date And Time   
         command = "cp -R "+src+" "+bksrc+today  
         os.system(command)  
    except:  
          print R+'   Code Backup FAILED!! '+ECODE  
          print dumpStack()  
  
def getCode():  
        try:  
             #   GETTING THE Fresg Code from build location   
           #    os.system('scp user@hostname:/home/user/Code_Ioc/*.*ar '+src)  
                os.system('cp /home/danyboy/apps/paDeployar/*.*ar '+src)
                print G+'    THE CODE COPIED SUCCESSFULLY  '+ECODE  
        except:
                print R+'   THE CODE COPYING FAILED?!?!?'+ECODE  
                print dumpStack()  
                exit()  
def conn():  
        try:  
#                  CONNECTING TO THE SERVER ....   
                #connect(userConfigFile=UCF, userKeyFile=UKF, url=URL)  
                connect('weblogic','nextel123','t3://127.0.0.1:7101')
        except:  
                print R+'  CONNECTION FAILED....',+ECODE  
                print dumpStack()  
                exit()  
def editing():  
        edit()  
        startEdit()  
   
def activating():  
    save()  
    activate()  
   
def stoppingApp():  
    deploylist.reverse()  
    for s in deploylist:  
        try:  
            editing()  
            progress=stopApplication(s,timeout=360000)  
            progress.printStatus()  
            activating()  
        except:  
            print R+'  FAILED TO STOP THE APPLICATION  '+ECODE  
            print dumpStack()  
     
    print G+'  APPLICATION STOPPED  '+ECODE  
   
def pUndeploy():  
     deploylist.reverse()  
     for s in deploylist:  
        try:  
                editing()  
                progress=undeploy(s, timeout=360000)  
                progress.printStatus()  
                activating()  
        except:  
                print R+'  FAILED TO UNDEPLOY THE APPLICATION  '+ECODE  
                print dumpStack()  
     print G+'  APPLICATION UNDEPLOYED   '+ECODE  
   
# This module is optional   
def clearCache():  
        try:  
                print G+'  CLEARING THE CACHE  '+ECODE  
                command = "rm -rf "+dpath+"/servers/AdminServer/tmp/*.*"  
                os.system(command)  
                print G+'  CLEARED THE CACHE   '+ECODE  
        except:  
                print R+'  FAILED TO CLEAR CACHE '+ECODE  
 
def pDeploy():  
     for s in deploylist:  
        try:  
            editing()  
            progress=deploy(s,src+"/"+s,target='AdminServer',timeout=360000)  
            progress.printStatus()  
            activating()  
        except:  
            print R+'FAILED TO DEPLOY THE APPLICATION'+ECODE  
            print dumpStack()  
     print G+'  APPLICATION DEPLOYED  '+ECODE  
 
def startingApp():  
     for s in deploylist:  
        try:  
                editing()  
                startApplication(s,timeout=360000)  
                activating()  
        except:  
            print R+'FAILED TO START THE APPLICATION '+ECODE  
     print G+'APPLICATION STARTED SUCCESSFULLY '+ECODE  
  
if __name__== "main":  
        backup()  
        getCode()  
        conn()  
        stoppingApp()  
        pUndeploy()  
        clearCache()  
        pDeploy()  
        startingApp()  
        print G+' ....DEPLOYMENET DONE...'+ECODE  
