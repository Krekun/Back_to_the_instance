from itertools import count
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
        self.id_list=[]
        self.name_list=[]
        self.time_list=[]
        count=0
        for file in self.latest_file:
            with open(file,"r",encoding="UTF") as f:
                sentences=f.read()
                self.get_id_list(sentences)
                self.get_name_list(sentences)
                self.get_time_list(sentences)
            count+=1
            if count>30:
                break

    def get_id_list(self,sentences):
        m=re.finditer('Joining w.*\n',sentences)#Find worlds' and instances' id in a log fille
        temp=list(m)
        temp=list(map(lambda x:x.group().strip("Joining ").strip("\n"),temp))
        self.id_list+=temp
    
    def get_name_list(self,sentences):
        m=re.finditer('Entering Room.*\n',sentences)#Find worlds' names in a log fille
        temp=list(m)
        temp=list(map(lambda x:x.group().strip("Entering Room:").strip("\n"),temp))
        self.name_list+=temp
    def get_time_list(self,sentences):
        m=re.finditer('.*Entering Room',sentences)#Find worlds' names in a log fille
        temp=list(m)
        temp=list(map(lambda x:str(x.group())[10:16],temp))
        self.time_list+=temp

    #Get the latest log file of VRC
    #Log files of VRC is stored in \AppData\LocalLow\VRChat\VRChat
    #Names of log files is like output_log_15-24-16.txt
    def get_latest_log(self):
        self.list_of_files =glob(self.logpath+'*.txt')
        # self.latest_file = max(self.list_of_files, key=os.path.getctime)#Get the lates created log file 
        self.latest_file = sorted(self.list_of_files, key=os.path.getctime, reverse=True)#Get the lates created log file 
        # self.latest_file = [self.logpath+"output_log_11-09-11.txt"]#Get the lates created log file 

    def launch_game(self):
        id="vrchat://launch?id="+self.id_list[self.id_choice]
        subprocess.run([self.path,id],shell=True)

if __name__=="__main__":
    Back_to_the_instance(launch=True)