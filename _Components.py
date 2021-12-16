import tkinter as tkntr
from tkinter.constants import HORIZONTAL
import tkinter.ttk as tkttk

class MFormTabFrame(tkntr.Frame):
    def __init__(self,parent,headings=tuple(), rows=tuple(),hb=int(),he=int(),btns=list(),lbls=list(),empts=list()):
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
        datecomps=tkntr.Frame(self,background="white")
        btnframe=tkntr.Frame(datecomps,background="white")
        lblframe=tkntr.Frame(datecomps,background="white")
        emptsframe=tkntr.Frame(datecomps,background="white")
        btns=create_btns(btnframe,hb)
        self.btns=btns
        lbls=create_lbls(lblframe,headings)
        self.lbls=lbls
        empts=create_txts(emptsframe,he)
        self.empts=empts
        btnframe.pack(anchor=tkntr.N,fill=tkntr.BOTH)
        lblframe.pack(side=tkntr.LEFT,anchor=tkntr.SE,fill=tkntr.BOTH)
        emptsframe.pack(side=tkntr.RIGHT,anchor=tkntr.SW,fill=tkntr.BOTH)
        datecomps.pack(fill=tkntr.BOTH)
        self.initUI() 
            
                   
    def initUI(self):
        self.pack(fill=tkntr.BOTH,expand=1) 
        
def create_btns(frame,g):
    btns=[]
    listhdbtns=['Добавить','Сохранить','Удалить','Отмена','Поиск','Обновление']
    for i in range(0,g):
        btns.append(tkntr.Button(frame,text=listhdbtns[i])) 
    for btn in btns:
        btn.pack(side=tkntr.LEFT,anchor=tkntr.S,padx=100,ipadx=20,pady=5)  
    return btns
def create_lbls(frame,nheadings):
    lbls=[]
    listhdlbls=list(nheadings)
    for i in range(0,len(listhdlbls)):
        lbls.append(tkntr.Label(frame,text=listhdlbls[i],background="white")) 
    for lbl in lbls:
        lbl.pack(side=tkntr.TOP,anchor=tkntr.S,padx=75,ipadx=30,pady=3) 
    return lbls 
def create_txts(frame,g):
    entrs=[]
    for i in range(0,g):
        entrs.append(tkntr.Entry(frame)) 
    for entr in entrs:
        entr.pack(side=tkntr.TOP,anchor=tkntr.S,padx=180,ipadx=150,pady=4) 
    return entrs 