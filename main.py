from itertools import count
import re
import os
from glob import glob
import subprocess

class Back_to_the_instance():
    def __init__(self,launch=False):
         self.path="C:\\Program Files (x86)\\Steam\\steamapps\\common\\VRChat\\launch.exe"#default path to VR chat launcher
         self.vrchat_logfolder="\AppData\LocalLow\VRChat\VRChat\\"    #Log files of VRC is stored in \AppData\LocalLow\VRChat\VRChat
         self.userpath=os.environ['USERPROFILE']
         self.logpath=self.userpath+self.vrchat_logfolder#Logfiles of VRC is located here
         self.get_latest_log()
         self.get_world()
         self.id_choice=0
         if launch==True:
             self.launch_game()

    #Get world id and instance in a log file
    def get_world(self):
        self.id_list=[]#initilaze lists
        self.name_list=[]
        self.time_list=[]
        self.count=0
        for file in self.latest_file:
            with open(file,"r",encoding="UTF") as f:
                sentences=f.read()
                self.get_lists(sentences,0)#0:instance id ,1:instance name 2:joined time
                self.get_lists(sentences,1)
                self.get_lists(sentences,2)
            self.count+=1
            if self.count>30:
                break

    def get_lists(self,sentences,format_type):
        text_list=("Joining w.*\n",'Entering Room.*\n','.*Entering Room')
        m=re.finditer(text_list[format_type],sentences)#Find worlds' and instances' id in a log fille
        temp_list=list(reversed(list(m)))
        if format_type==0:
            self.id_list+=list(map(lambda x:x.group().removeprefix("Joining ").strip("\n"),temp_list))#Process the sentencet to an instance id
        elif format_type==1:
            self.name_list+=list(map(lambda x:x.group().removeprefix("Entering Room:").strip("\n"),temp_list))#Process the sentencet to the world name
        elif format_type==2:
            self.time_list+=list(map(lambda x:str(x.group())[10:16],temp_list))#Process the sentencet to the joinning time

    #Get the latest log file of VRC
    #Names of log files are like output_log_15-24-16.txt
    def get_latest_log(self):
        self.list_of_files =glob(self.logpath+'*.txt')
        self.latest_file = sorted(self.list_of_files, key=os.path.getctime, reverse=True)#Get the log files 

    def launch_game(self):
        id="vrchat://launch?id="+self.id_list[self.id_choice]
        subprocess.run([self.path,id],shell=True)

if __name__=="__main__":
    Back_to_the_instance(launch=True)
    print()