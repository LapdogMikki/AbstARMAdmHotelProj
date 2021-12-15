import tkinter as tkntr
from tkinter.constants import HORIZONTAL
import tkinter.ttk as tkttk

class MFormTabFrame(tkntr.Frame):
    def __init__(self,parent,headings=tuple(), rows=tuple()):
        tkntr.Frame.__init__(self,parent,background="white")
        self.parent = parent
        tablecomps=tkntr.Frame(self,background="white")
        table = tkttk.Treeview(tablecomps, show="headings", selectmode="browse")
        table["columns"] = headings
        table["displaycolumns"] = headings
        for head in headings:
            table.heading(head, text=head, anchor=tkntr.CENTER)
            table.column(head, anchor=tkntr.CENTER)
        for row in rows:
            table.insert('', tkntr.END, values=tuple(row))
        scrolltable = tkntr.Scrollbar(tablecomps, command=table.yview)
        xscrolltable = tkntr.Scrollbar(tablecomps, command=table.xview, orient=HORIZONTAL)
        table.configure(yscrollcommand=scrolltable.set)
        table.configure(xscrollcommand=xscrolltable.set)
        scrolltable.pack(side=tkntr.RIGHT, fill=tkntr.Y)
        xscrolltable.pack(side=tkntr.BOTTOM, fill=tkntr.X)
        table.pack(expand=tkntr.YES, fill=tkntr.BOTH)
        tablecomps.pack(side=tkntr.TOP,fill=tkntr.X)
        datecomps=tkntr.Frame(self,background='black')
        a=tkntr.Label(datecomps,text="АААА")
        self.btns=list()
        a.pack(side=tkntr.RIGHT)
        datecomps.pack(side=tkntr.BOTTOM,fill=tkntr.BOTH)
        self.initUI() 
    
    def create_btns(self,g):
        listhdbtns=['Добавить','Сохранить','Удалить','Отмена','Поиск','Обновление']
        for i in range(0,g):
            self.btns.append(tkntr.Button(text=listhdbtns[i])) 
        for btn in self.btns:
            btn.pack(side=tkntr.BOTTOM,anchor=tkntr.S)  
                   
    def initUI(self):
        self.pack(fill=tkntr.BOTH,expand=1) 