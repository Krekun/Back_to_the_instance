import re
import os
from glob import glob
import subprocess

#Get world id and instance in a log file
def get_world():
    log_addres=get_latest_log()
    with open(log_addres,"r",encoding="UTF") as f:
        sentences=f.read()
        m=re.finditer('Joining w.*\n',sentences)#Find world and instance id in a log fille
        temp_tex=list(m)
        temp_tex=temp_tex[-1].group().strip("Joining ").strip("\n")#select the latest world and instance
        wrld,instance=temp_tex.split(":")
    return wrld,instance
#Get the latest log file of VRC
#Log files of VRC is stored in \AppData\LocalLow\VRChat\VRChat
#Names of log files is like output_log_15-24-16.txt
def get_latest_log():
    userpath=os.environ['USERPROFILE']
    vrchat_logfolder="\AppData\LocalLow\VRChat\VRChat\\"
    logpath=userpath+vrchat_logfolder#Logfiles of VRC is located here
    list_of_files =glob(logpath+'*.txt')
    latest_file = max(list_of_files, key=os.path.getctime)#Get the lates created log file 
    return latest_file

if __name__=="__main__":
    wrld,instance=get_world()
    path="C:\\Program Files (x86)\\Steam\\steamapps\\common\\VRChat\\launch.exe"
    id="vrchat://launch?id="+wrld+":"+instance
    subprocess.run([path,id],shell=True)