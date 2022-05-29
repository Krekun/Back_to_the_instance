import requests
import json
from tkinter import messagebox

class Invite():
    def __init__(self,id,path):
        self.apiKey   = 'JlE5Jldo5Jibnk5O5hTx6XVqsJu4WJ26'
        self.data     = {'apiKey':self.apiKey}
        self.headers  = {'User-Agent': 'SunaFH/1.0.5'}
        self.id=id
        try:
            with open(path,"r") as f:
                data_load=json.load(f)
                self.username = data_load['username']
                self.password = data_load['password']
        except:
            self.username = False
            self.password = False


    def Send_invite(self):
        # messagebox.showerror('エラー', self.username)
        try:
            response = requests.get('https://api.vrchat.cloud/api/1/auth/user', data=self.data, headers=self.headers, auth=(self.username,self.password))
            if response.status_code!=200:
                messagebox.showerror('エラー', 'ログインに失敗しました。')
                return False
            authToken= response.cookies["auth"]
            url="https://vrchat.com/api/1/instances/"+self.id+"/invite"
            response=requests.post(url,data=self.data, headers=self.headers, params={"authToken": authToken})
            if response.status_code!=200:
                messagebox.showerror('エラー', 'セルフインバイトに失敗しました。')
        except:
            messagebox.showerror('エラー', '想定外のエラーです。')            


        
if __name__=="__main__":
    Invite(1,2).Send_invite()
