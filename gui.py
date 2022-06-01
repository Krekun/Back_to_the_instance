import tkinter as tk
from tkinter import messagebox
from unicodedata import name
from main import *
import threading
from invite import *
# from form2 import *
import os,sys

# アプリの定義
class ListBoxApp(Back_to_the_instance):
    # 初期化
    def __init__(self, bti: Back_to_the_instance=Back_to_the_instance()):
        self.root=tk.Tk()
        self.root.title('ワールドの選択')
        # self.root.iconphoto=(False,tk.PhotoImage(file="VRC2.ico"))
        self.root.iconbitmap(self.find_data_file("VRC.ico"))
        self.master=tk.Frame(self.root, width=440, height=200)
        # タイトルの表示
        self.name_list=bti.name_list
        self.id_list=bti.id_list
        self.time_list=bti.time_list
        self.path=bti.path
        self.path_to_id=self.find_data_file("id.json")
        self.result=[t1+" "+t2 for t1,t2 in zip(self.time_list,self.name_list)]
        self.id_choice=0
        self.create_widgets()
        self.master.pack()

    def create_widgets(self):
        self.list_box = tk.Listbox(self.root, listvariable=tk.StringVar(value=self.result), selectmode='browse',font=150)
        self.list_box.bind('<<ListboxSelect>>', lambda e: self.on_select_box())
        self.list_box.place(x=10, y=10, width=250, height=200)
        self.button1 =tk.Button(self.root,text=u'Run',command=self.on_select_button1,font=("",25))
        self.button1.place(x=300, y=30, width=120, height=60)
        self.button2 =tk.Button(self.root,text=u'Self invite',command=self.on_select_button2,font=("",20))
        self.button2.place(x=300, y=110, width=120, height=60)

    def find_data_file(self,filename):
        if getattr(sys, "frozen", False):
            # The application is frozen
            datadir = os.path.dirname(sys.executable)
        else:
            # The application is not frozen
            # Change this bit to match where you store your data files:
            datadir = os.path.dirname(__file__)
        return os.path.join(datadir, filename)
    # 選択時に呼ばれる
    def on_select_box(self):
        for i in self.list_box.curselection():
            self.id_choice=i
    def on_select_button1(self):
            self.launch_game()
            self.master.destroy()
    def make_id_file(self):
            with open(self.path_to_id, 'w') as f:
                f.write('{\n"username":"",\n"password":""\n}')
            subprocess.run(["notepad.exe",self.path_to_id],shell=True)

    def on_select_button2(self):
            id=self.id_list[self.id_choice]
            invite=Invite(id,self.path_to_id)
            if not (invite.password or invite.username):
                    # print("You need your name and  your password of VR chat to use self-invite")
                    messagebox.showerror('エラー', 'Self inviteの利用にはusernameとpasswordが必要です。')
                    # print(find_data_file("id.json"))
                    self.make_id_file()
            else:
                result=invite.send_invite()
                if result==False:                
                    self.make_id_file()
            # self.master.destroy()
            
# アプリの実行
if __name__=="__main__":
    app=ListBoxApp()
    app.root.mainloop()  