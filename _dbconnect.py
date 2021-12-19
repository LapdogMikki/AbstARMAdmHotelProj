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
    crs.execute("SELECT rooms.nmb_room,type_room.t_room,type_room.price FROM rooms,type_room WHERE rooms.id_type_room=type_room.id_type")
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
    crs.execute("SELECT FIO FROM client")
    data=[]
    for row in crs.fetchall():
        data.append(row[0])
    con.close()
    return data
def cbx_selectnmrs():
    con=connectDB()
    crs=con.cursor()
    crs.execute("SELECT nmb_room FROM rooms")
    data=[]
    for row in crs.fetchall():
        data.append(row[0])
    con.close()
    return data
def cbx_selectuslgs():
    con=connectDB()
    crs=con.cursor()
    crs.execute("SELECT name_usluga FROM uslugs")
    data=[]   
    for row in crs.fetchall():
        data.append(row[0])
    con.close()
    return data
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
def delete_bron(table):
    def del_brn():
        if table.selection():
            con=connectDB()
            crs=con.cursor()
            curItem = table.focus()
            contents =(table.item(curItem))
            selecteditem = contents['values']
            table.delete(curItem)
            crs.execute("DELETE FROM nmb_room WHERE ",(selecteditem[0],))
            con.commit()
            con.close()
            
        else:
            mb.showerror('Ошибка','Не выделена запись')
    return del_brn

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
            view_tab_rec_kli(table)
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
            crs.execute("DELETE FROM  WHERE =(?)",(selecteditem[0],))
            con.commit()
            con.close()
            
        else:
            mb.showerror('Ошибка','Не выделена запись')
    return del_okusl