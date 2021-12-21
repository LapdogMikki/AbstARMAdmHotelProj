import sqlite3
import os
from sqlite3.dbapi2 import Error
from tkinter import messagebox as mb
def connectDB():
    try:
        cnct=sqlite3.connect("gst.db")
        return cnct
    except Error:
        print(Error)
def showtabbron():
    con=connectDB()
    crs=con.cursor()
    crs.execute("SELECT rooms.nmb_room,client.FIO,resrvd.date_chckin,resrvd.date_evict FROM rooms,client,resrvd WHERE client.id_klient=resrvd.id_client and rooms.id_room=resrvd.id_room")
    data=(row for row in crs.fetchall()) 
    con.close()
    return data   
def showtabkli():
    con=connectDB()
    crs=con.cursor()
    crs.execute("SELECT FIO,phone,grzhd,udostlich,seria,nomer,visa,visa_beg_dat,visa_end_date FROM client")
    data=(row for row in crs.fetchall()) 
    con.close()
    return data   
def showtabrms():
    con=connectDB()
    crs=con.cursor()
    crs.execute("SELECT type_room.t_room,rooms.nmb_room,type_room.price FROM rooms,type_room WHERE rooms.id_type_room=type_room.id_type")
    data=(row for row in crs.fetchall()) 
    con.close()
    return data 
def showtabtprms():
    con=connectDB()
    crs=con.cursor()
    crs.execute("SELECT t_room,kolvo_mest,price FROM type_room")
    data=(row for row in crs.fetchall()) 
    con.close()
    return data 
def showtabusl():
    con=connectDB()
    crs=con.cursor()
    crs.execute("SELECT name_usluga,ed_izm,price FROM uslugs")
    data=(row for row in crs.fetchall()) 
    con.close()
    return data 
def showtabokusl():
    con=connectDB()
    crs=con.cursor()
    crs.execute("SELECT uslugs.name_usluga,client.FIO,ispolz_uslug.kol_vo,ispolz_uslug.date_usg,ispolz_uslug.price FROM client,uslugs,ispolz_uslug WHERE client.id_klient=ispolz_uslug.id_client and uslugs.id_usluga=ispolz_uslug.id_usluga")
    data=(row for row in crs.fetchall()) 
    con.close()
    return data 
def cbx_selectklts():
    con=connectDB()
    crs=con.cursor()
    con.row_factory = lambda crs,row:(str(row[0])+". "+row[1], row[0])
    crs.execute("SELECT id_klient,FIO FROM client")
    rows = {r[0]:r[1] for r in crs}
    con.close()
    return rows
def upd_cbx_selectklts(cbbx):
    def upd_cbx_selkl():
        cbbx["values"]=''
        data=cbx_selectklts()
        cbbx["values"]=list(data.values()) 
    return upd_cbx_selkl
def cbx_selectnmrs():
    con=connectDB()
    crs=con.cursor()
    con.row_factory = lambda row:(str(row[0])+". "+row[1], row[0])
    crs.execute("SELECT id_room,nmb_room FROM rooms")
    rows = {r[0]:r[1] for r in crs}
    con.close()
    return rows
def upd_cbx_selectnmrs(cbbx):
    def upd_cbx_selnmr():
        cbbx["values"].delete()
        data=cbx_selectnmrs()
        cbbx["values"]=list(data.values())  
    return upd_cbx_selnmr 
def cbx_tpnmrs():
    con=connectDB()
    crs=con.cursor()
    con.row_factory = lambda crs, row:(str(row[0])+". "+row[1], row[0])
    crs.execute("SELECT id_type,t_room FROM type_room")
    rows = {r[0]:r[1] for r in crs}
    con.close()
    return rows
def upd_cbx_tpnmrs(cbbx):
    def upd_cbx_tpnmb():
        cbbx["values"]=''
        data=cbx_tpnmrs()
        cbbx["values"]=list(data.values())  
    return upd_cbx_tpnmb
def cbx_selectuslgs():
    con=connectDB()
    crs=con.cursor()
    con.row_factory = lambda crs, row:(str(row[0])+". "+row[1], row[0])
    crs.execute("SELECT id_usluga,name_usluga FROM uslugs")
    rows = {r[0]:r[1] for r in crs}
    con.close()
    return rows
def upd_cbx_selectuslgs(cbbx):
    def upd_cbx_selusl():
        cbbx["values"]=''
        data=cbx_selectuslgs()
        cbbx["values"]=list(data.values()) 
    return upd_cbx_selusl   
def insert_kli(itms,table): 
    def ins_kli():
        con=connectDB()
        crs=con.cursor()
        crs.execute("INSERT INTO client(FIO,phone,grzhd,udostlich,seria,nomer,visa,visa_beg_dat,visa_end_date) VALUES(?,?,?, ?, ?,?,?,?,?)",(str(itms[0].get()),str(itms[1].get()),str(itms[2].get()),str(itms[3].get()),str(itms[4].get()),str(itms[5].get()),str(itms[6].get()),str(itms[7].get()),str(itms[8].get())))
        con.commit()  
        con.close()
        view_tab_rec_kli(table)
    return ins_kli     
        
def view_tab_rec_kli(table):
    con=connectDB()
    crs=con.cursor()
    crs.execute("SELECT FIO,phone,grzhd,udostlich,seria,nomer,visa,visa_beg_dat,visa_end_date FROM client")
    [table.delete(i) for i in table.get_children()] 
    [table.insert('','end',values=row) for row in crs.fetchall()] 
     
def insert_tab_trooms(itms,table): 
    def ins_trooms():
        con=connectDB()
        crs=con.cursor()
        crs.execute("INSERT INTO type_room(t_room,kolvo_mest,price) VALUES(?,?,?)",(str(itms[0].get()),str(itms[1].get()),float(itms[2].get())))
        con.commit()  
        con.close()
        view_tab_rec_trooms(table)
    return ins_trooms

def insert_tab_uslgs(itms,table): 
    def ins_uslgs():
        con=connectDB()
        crs=con.cursor()
        crs.execute("INSERT INTO uslugs(name_usluga,ed_izm,price) VALUES(?,?,?)",(str(itms[0].get()),str(itms[1].get()),float(itms[2].get())))
        con.commit()  
        con.close()
        view_tab_rec_uslgs(table)
    return ins_uslgs

def view_tab_rec_uslgs(table):
    con=connectDB()
    crs=con.cursor()
    crs.execute("SELECT name_usluga,ed_izm,price FROM uslugs")    
    [table.delete(i) for i in table.get_children()] 
    [table.insert('','end',values=row) for row in crs.fetchall()]  

def view_tab_rec_trooms(table):
    con=connectDB()
    crs=con.cursor()
    crs.execute("SELECT t_room,kolvo_mest,price FROM type_room")
    [table.delete(i) for i in table.get_children()] 
    [table.insert('','end',values=row) for row in crs.fetchall()]
    
def view_tab_rec_rooms(table):
    con=connectDB()
    crs=con.cursor()
    crs.execute("SELECT type_room.t_room,rooms.nmb_room,type_room.price FROM rooms,type_room WHERE rooms.id_type_room=type_room.id_type")
    [table.delete(i) for i in table.get_children()] 
    [table.insert('','end',values=row) for row in crs.fetchall()]
    
def view_tab_rec_okuslgs(table):
    con=connectDB()
    crs=con.cursor()
    crs.execute("SELECT uslugs.name_usluga,client.FIO,ispolz_uslug.kol_vo,ispolz_uslug.date_usg,ispolz_uslug.price FROM client,uslugs,ispolz_uslug WHERE client.id_klient=ispolz_uslug.id_client and uslugs.id_usluga=ispolz_uslug.id_usluga")
    [table.delete(i) for i in table.get_children()] 
    [table.insert('','end',values=row) for row in crs.fetchall()]
    
  
def delete_bron(table):
    def del_brn():
        if table.selection():
            con=connectDB()
            crs=con.cursor()
            curItem = table.focus()
            contents =(table.item(curItem))
            selecteditem = contents['values']
            table.delete(curItem)
            crs.execute("DELETE FROM nmb_room WHERE rooms.nmb_room=?",(selecteditem[0],))
            con.commit()
            con.close()    
        else:
            mb.showerror('Ошибка','Не выделена запись')
    return del_brn
def view_tab_rec_bron(table):
    con=connectDB()
    crs=con.cursor()
    crs.execute("SELECT rooms.nmb_room,client.FIO,resrvd.date_chckin,resrvd.date_evict FROM rooms,client,resrvd WHERE client.id_klient=resrvd.id_client and rooms.id_room=resrvd.id_room") 
    [table.delete(i) for i in table.get_children()] 
    [table.insert('','end',values=row) for row in crs.fetchall()]  

def delete_clnt(table):
    def del_cl():
        if table.selection():
            con=connectDB()
            crs=con.cursor()
            curItem = table.focus()
            contents =(table.item(curItem))
            selecteditem = contents['values']
            table.delete(curItem)
            crs.execute("DELETE FROM client WHERE FIO=(?)",(selecteditem[0],))
            con.commit()
            con.close()
        else:
            mb.showerror('Ошибка','Не выделена запись')
    return del_cl

def delete_nmb(table):
    def del_nmb():
        if table.selection():
            con=connectDB()
            crs=con.cursor()
            curItem = table.focus()
            contents =(table.item(curItem))
            selecteditem = contents['values']
            table.delete(curItem)
            crs.execute("DELETE FROM rooms WHERE nmb_room=(?)",(selecteditem[0],))
            con.commit()
            con.close()    
        else:
            mb.showerror('Ошибка','Не выделена запись')
    return del_nmb

def delete_tproom(table):
    def del_tproom():
        if table.selection():
            con=connectDB()
            crs=con.cursor()
            curItem = table.focus()
            contents =(table.item(curItem))
            selecteditem = contents['values']
            table.delete(curItem)
            crs.execute("DELETE FROM type_room WHERE t_room=(?)",(selecteditem[0],))
            con.commit()
            con.close()
            
        else:
            mb.showerror('Ошибка','Не выделена запись')
    return del_tproom

def delete_uslgs(table):
    def del_uslgs():
        if table.selection():
            con=connectDB()
            crs=con.cursor()
            curItem = table.focus()
            contents =(table.item(curItem))
            selecteditem = contents['values']
            table.delete(curItem)
            crs.execute("DELETE FROM uslugs WHERE usluga=(?)",(selecteditem[0],))
            con.commit()
            con.close()
            view_tab_rec_uslgs(table)
        else:
            mb.showerror('Ошибка','Не выделена запись')
    return del_uslgs
def delete_okusl(table):
    def del_okusl():
        if table.selection():
            con=connectDB()
            crs=con.cursor()
            curItem = table.focus()
            contents =(table.item(curItem))
            selecteditem = contents['values']
            table.delete(curItem)
            crs.execute("DELETE FROM okusl WHERE uslugs.name_usluga=(?)",(selecteditem[0],))
            con.commit()
            con.close()
            
        else:
            mb.showerror('Ошибка','Не выделена запись')
    return del_okusl

