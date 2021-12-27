from sqlite3.dbapi2 import SQLITE_SELECT
import tkinter as tkntr
from tkinter.constants import COMMAND, HORIZONTAL
import tkinter.ttk as tkttk
import _dbconnect as dbcon
class MFormTabFrame(tkntr.Frame):
    def __init__(self,parent,headings=tuple(), rows=tuple(),hb=int(),hcbx=int(),he=int(),tid=int()):
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
        self.table=table
        table.pack(expand=tkntr.YES, fill=tkntr.BOTH)
        tablecomps.pack(side=tkntr.TOP,fill=tkntr.X)
        datecomps=tkntr.Frame(self,background="white")
        btnframe=tkntr.Frame(datecomps,background="white")
        lblframe=tkntr.Frame(datecomps,background="white")
        emptsframe=tkntr.Frame(datecomps,background="white")
        self.tid=tid
        lbls=create_lbls(lblframe,headings,tid)
        self.lbls=lbls
        cbbxs=create_cbbxs(emptsframe,hcbx,headings)
        self.cbbxs=cbbxs
        empts=create_txts(emptsframe,he)
        self.empts=empts       
        self.tid=tid
        itms=[]
        for cbbx in cbbxs:
            itms.append(cbbx)
        for empt in empts:
            itms.append(empt)
        self.itms=itms
        table.bind('<<TreeviewSelect>>', self.on_select_item)
        btns=create_btns(btnframe,hb,table,tid,itms)
        self.btns=btns
        btnframe.pack(anchor=tkntr.N,fill=tkntr.BOTH)
        lblframe.pack(side=tkntr.LEFT,anchor=tkntr.SE,fill=tkntr.BOTH)
        emptsframe.pack(side=tkntr.RIGHT,anchor=tkntr.SW,fill=tkntr.BOTH)
        datecomps.pack(fill=tkntr.BOTH)
        self.initUI()
    def on_select_item(self,event):
        for self.itm in self.itms:
            self.itm.delete(0,'end')
        curItem = self.table.focus()
        contents =(self.table.item(curItem))
        selecteditem = contents['values']
        if ((self.tid==2) | (self.tid==5)):ln=len(selecteditem)-1
        else:ln=len(selecteditem)
        for i in range(0,ln):
            self.itms[i].insert(0,selecteditem[i])
    def initUI(self):
        self.pack(fill=tkntr.BOTH,expand=1) 
             
def create_btns(frame,g,ttable,tabid,itms):
    btns=[]
    funcbuttons=[[dbcon.insert_brons(itms,ttable),dbcon.update_bron(itms,ttable),dbcon.delete_bron(itms,ttable)],[dbcon.insert_kli(itms,ttable),dbcon.update_clnt(ttable,itms),dbcon.delete_clnt(ttable)],[dbcon.insert_rooms(itms,ttable),dbcon.update_nmb(itms,ttable),dbcon.delete_nmb(ttable)],[dbcon.insert_tab_trooms(itms,ttable),dbcon.update_trooms(ttable,itms),dbcon.delete_tproom(ttable)],[dbcon.insert_tab_uslgs(itms,ttable),dbcon.update_uslgs(ttable,itms),dbcon.delete_uslgs(ttable)],[dbcon.insert_okusls(itms,ttable),dbcon.update_okusl(itms,ttable),dbcon.delete_okusl(ttable)]]
    listhdbtns=['Добавить','Изменить','Удалить']
    for i in range(0,g):
        btns.append(tkntr.Button(frame,text=listhdbtns[i],command=funcbuttons[tabid][i]))
    for btn in btns:
        btn.pack(side=tkntr.LEFT,anchor=tkntr.S,padx=150,ipadx=20,pady=5)  
    return btns
def create_lbls(frame,nheadings,tid):
    lbls=[]
    listhdlbls=list(nheadings)
    if ((tid==2)|(tid==5)):ln=len(listhdlbls)-1
    else: ln=len(listhdlbls)
    for i in range(0,ln):
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
def create_cbbxs(frame,g,lheadings):
    cbbxs=[]
    vls=[]
    updts=[]
    if (lheadings[0]=='Тип номера'):
        vls.append(dbcon.cbx_tpnmrs())
    elif (lheadings[0]=='Номер'):
        vls.append(dbcon.cbx_selectnmrs())
    elif (lheadings[0]=='Услуга'):
        vls.append(dbcon.cbx_selectuslgs())
    if (lheadings[1]=='Клиент'):   
        vls.append(dbcon.cbx_selectklts())
    for i in range(0,g):
        cbbxs.append(tkttk.Combobox(frame))
        rows=vls[i]
        cbbxs[i]["value"]=list(rows.values()) 
    for cbbx in cbbxs:
        if (cbbx==cbbxs[0]):
            if (lheadings[0]=='Тип номера'):
                updts.append(dbcon.upd_cbx_tpnmrs(cbbx))
                cbbx.configure(postcommand=updts[0])
            elif (lheadings[0]=='Номер'):
                updts.append(dbcon.upd_cbx_selectnmrs(cbbx))
                cbbx.configure(postcommand=updts[0])
            elif (lheadings[0]=='Услуга'):
                updts.append(dbcon.upd_cbx_selectuslgs(cbbx))
                cbbx.configure(postcommand=updts[0])
        elif(cbbx==cbbxs[1]):
            if (lheadings[1]=='Клиент'):   
                updts.append(dbcon.upd_cbx_selectklts(cbbx))
                cbbx.configure(postcommand=updts[1])
        cbbx.pack(side=tkntr.TOP,anchor=tkntr.S,padx=180,ipadx=150,pady=4) 
    return cbbxs 
