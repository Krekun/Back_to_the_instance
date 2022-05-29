import re
import os
from glob import glob
import subprocess

class Back_to_the_instance():
    def __init__(self,launch=False):
         self.path="C:\\Program Files (x86)\\Steam\\steamapps\\common\\VRChat\\launch.exe"
         self.vrchat_logfolder="\AppData\LocalLow\VRChat\VRChat\\"
         self.userpath=os.environ['USERPROFILE']
         self.logpath=self.userpath+self.vrchat_logfolder#Logfiles of VRC is located here
         self.get_latest_log()
         self.get_world()
         self.id_choice=0
         if launch==True:
             self.launch_game()

    #Get world id and instance in a log file
    def get_world(self):
        with open(self.latest_file,"r",encoding="UTF") as f:
            self.sentences=f.read()
            m=re.finditer('Joining w.*\n',self.sentences)#Find worlds' and instances' id in a log fille
            self.id_list=list(m)
            self.id_list=list(map(lambda x:x.group().strip("Joining ").strip("\n"),self.id_list))
            m=re.finditer('Entering Room.*\n',self.sentences)#Find worlds' names in a log fille
            self.name_list=list(m)
            self.name_list=list(map(lambda x:x.group().strip("Entering Room:").strip("\n"),self.name_list))
    #Get the latest log file of VRC
    #Log files of VRC is stored in \AppData\LocalLow\VRChat\VRChat
    #Names of log files is like output_log_15-24-16.txt
    def get_latest_log(self):
        self.list_of_files =glob(self.logpath+'*.txt')
        self.latest_file = max(self.list_of_files, key=os.path.getctime)#Get the lates created log file 

    def launch_game(self):
        id="vrchat://launch?id="+self.id_list[self.id_choice]
        subprocess.run([self.path,id],shell=True)

if __name__=="__main__":
    Back_to_the_instance(launch=True)
    # wrld,instance=get_world()
    # path="C:\\Program Files (x86)\\Steam\\steamapps\\common\\VRChat\\launch.exe"
    # id="vrchat://launch?id="+wrld+":"+instance
    # subprocess.run([path,id],shell=True)