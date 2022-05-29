import tkinter as tk
from tkinter import messagebox
from main import *

# アプリの定義
class ListBoxApp(tk.Frame,Back_to_the_instance):
    # 初期化
    def __init__(self, master=None,bti: Back_to_the_instance=Back_to_the_instance()):
        tk.Frame.__init__(self, master, width=440, height=60)
        # タイトルの表示
        self.master.title('ワールドの選択')
        # リストボックス
        self.name_list=bti.name_list
        self.id_list=bti.id_list
        self.path=bti.path
        self.list_box = tk.Listbox(self, listvariable=tk.StringVar(value=self.name_list), selectmode='browse')
        self.list_box.bind('<<ListboxSelect>>', lambda e: self.on_select())
        self.list_box.place(x=10, y=10, width=440, height=60)
       
    # 選択時に呼ばれる
    def on_select(self):
        for i in self.list_box.curselection():
            self.id_choice=i
            messagebox.showinfo('情報', self.name_list[i]+'を選択しました') 
            self.launch_game()
            
# アプリの実行

if __name__=="__main__":
    app = ListBoxApp()
    app.pack()
    app.mainloop()