import requests
import json
from tkinter import messagebox

class Invite():
    def __init__(self,id,path):
        self.apiKey   = 'JlE5Jldo5Jibnk5O5hTx6XVqsJu4WJ26'#APIkey to use VRCAPI
        self.data     = {'apiKey':self.apiKey}
        self.headers  = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'}# use header of chrome
        self.id=id
        try:#check username and password are loaded correctly
            with open(path,"r") as f:
                data_load=json.load(f)
                self.username = data_load['username']
                self.password = data_load['password']
        except:
            self.username = False
            self.password = False

    def send_invite(self):#Function to send self-invite 
        try:
            response = requests.get('https://api.vrchat.cloud/api/1/auth/user', data=self.data, headers=self.headers, auth=(self.username,self.password))#Log in to VR Chat
            if response.status_code!=200:
                messagebox.showerror('エラー', 'ログインに失敗しました。')
                return False
            authToken= response.cookies["auth"]
            url="https://vrchat.com/api/1/instances/"+self.id+"/invite"
            response=requests.post(url,data=self.data, headers=self.headers, params={"authToken": authToken})#Send self-invite using VR chat API
            if response.status_code!=200:
                messagebox.showerror('エラー', 'セルフインバイトに失敗しました。')
        except:
            messagebox.showerror('エラー', '想定外のエラーです。')            