import tkinter as tk
from tkinter import messagebox
from main import *
import threading

# アプリの定義
class ListBoxApp(tk.Frame,Back_to_the_instance):
    # 初期化
    def __init__(self, master=None,bti: Back_to_the_instance=Back_to_the_instance()):
        tk.Frame.__init__(self, master, width=440, height=200)
        # タイトルの表示
        self.master.title('ワールドの選択')
        # リストボックス
        self.name_list=bti.name_list
        self.id_list=bti.id_list
        self.time_list=bti.time_list
        self.path=bti.path
        self.result=[t1+" "+t2 for t1,t2 in zip(self.time_list,self.name_list)]
        self.list_box = tk.Listbox(self, listvariable=tk.StringVar(value=self.result), selectmode='browse',font=150)
        self.list_box.bind('<<ListboxSelect>>', lambda e: self.on_select_box())
        self.list_box.place(x=10, y=10, width=250, height=200)
        self.button1 =tk.Button(self,text=u'Run',command=self.on_select_button1)
        self.button1.place(x=300, y=30, width=120, height=60)
        self.button2 =tk.Button(self,text=u'Self invite',command=self.on_select_button2)
        self.button2.place(x=300, y=110, width=120, height=60)
        #toolbox

       
    # 選択時に呼ばれる
    def on_select_box(self):
        for i in self.list_box.curselection():
            self.id_choice=i
    def on_select_button1(self):
            self.launch_game()
            self.master.destroy()    

    def on_select_button2(self):
            # self.pack_forget()
            self.master.destroy()

            
# アプリの実行

if __name__=="__main__":
    app = ListBoxApp()
    app.pack()

    app.mainloop()