import tkinter as tk
from tkinter import messagebox
from main import *

# アプリの定義
class ListBoxApp(tk.Frame):
    # 初期化
    def __init__(self, master=None):
        tk.Frame.__init__(self, master, width=440, height=60)

        # タイトルの表示
        self.master.title('ワールドの選択')
       
        # リストボックス
        self.a,self.items=get_world(is_list=True)
        # items = ['アイテム1', 'アイテム2']
        self.list_box = tk.Listbox(self, listvariable=tk.StringVar(value=self.items), selectmode='browse')
        self.list_box.bind('<<ListboxSelect>>', lambda e: self.on_select())
        self.list_box.place(x=10, y=10, width=440, height=60)
       
    # 選択時に呼ばれる
    def on_select(self):
        for i in self.list_box.curselection():
            messagebox.showinfo('情報', self.a[i]+'を選択しました')   

# アプリの実行
app = ListBoxApp()
app.pack()
app.mainloop()