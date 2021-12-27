import sqlite3
import os
from datetime import *
from sqlite3.dbapi2 import PARSE_COLNAMES, Error
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
    crs.execute("SELECT FIO,phone,grzhd,udostlich,seria,nomer,visa,visabegdat,visaenddate FROM client")
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
        cbbx["values"]=''
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

def insert_brons(itms,table): 
    def ins_bron():
        con=connectDB()
        crs=con.cursor()
        slv_kl=cbx_selectklts()
        slv_room=cbx_selectnmrs()
        nm_rm=int(itms[0].get())
        for key in slv_room.keys():
            if nm_rm==slv_room[key]:
                id_rm=key
        nm_cl=str(itms[1].get())
        for key in slv_kl.keys():
            if nm_cl==slv_kl[key]:
                id_kl=key
        crs.execute("INSERT INTO resrvd(id_client,date_chckin,date_evict,id_room) VALUES(?,?,?,?)",(id_kl,itms[2].get(),itms[3].get(),id_rm))
        con.commit()  
        con.close()
        view_tab_rec_bron(table)
    return ins_bron  

def insert_okusls(itms,table): 
    def ins_okusl():
        con=connectDB()
        crs=con.cursor()
        slv_kl=cbx_selectklts()
        nm_cl=str(itms[1].get())
        for key in slv_kl.keys():
            if nm_cl==slv_kl[key]:
                id_kl=key
        slv_uslgs=cbx_selectuslgs()
        nm_usl=str(itms[0].get())
        for key in slv_uslgs.keys():
            if nm_usl==slv_uslgs[key]:
                id_usl=key
        crs.execute("Select price from uslugs WHERE id_usluga=?",(id_usl,))
        price=crs.fetchone()
        kol=int(itms[2].get())
        prc=float(price[0])*kol
        crs.execute("INSERT INTO ispolz_uslug(id_usluga,id_client,date_usg,kol_vo,price) VALUES(?,?,?,?,?)",(int(id_usl),int(id_kl),itms[3].get(),kol,prc))
        con.commit()  
        con.close()
        view_tab_rec_okuslgs(table)
    return ins_okusl  

def insert_rooms(itms,table): 
    def ins_room():
        con=connectDB()
        crs=con.cursor()
        slv_troom=cbx_tpnmrs()
        nm_trm=str(itms[0].get())
        for key in slv_troom.keys():
            if nm_trm==slv_troom[key]:
                id_trm=key
        crs.execute("Select price from type_room WHERE id_type=?",(id_trm,))
        prc=crs.fetchone()
        crs.execute("INSERT INTO rooms(id_type_room,nmb_room) VALUES(?,?)",(id_trm,str(itms[1].get()),))
        con.commit()  
        con.close()
        view_tab_rec_rooms(table)
    return ins_room 
def insert_kli(itms,table): 
    def ins_kli():
        con=connectDB()
        crs=con.cursor()
        crs.execute("INSERT INTO client(FIO,phone,grzhd,udostlich,seria,nomer,visa,visabegdat,visaenddate) VALUES(?,?,?, ?, ?,?,?,?,?)",(str(itms[0].get()),str(itms[1].get()),str(itms[2].get()),str(itms[3].get()),str(itms[4].get()),str(itms[5].get()),str(itms[6].get()),str(itms[7].get()),str(itms[8].get())))
        con.commit()  
        con.close()
        view_tab_rec_kli(table)
    return ins_kli             
def view_tab_rec_kli(table):
    con=connectDB()
    crs=con.cursor()
    crs.execute("SELECT FIO,phone,grzhd,udostlich,seria,nomer,visa,visabegdat,visaenddate FROM client")
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
    
  
def delete_bron(itms,table):
    def del_brn():
        if table.selection():
            con=connectDB()
            crs=con.cursor()
            curItem = table.focus()
            contents =(table.item(curItem))
            selecteditem = contents['values']
            slv_kl=cbx_selectklts()
            slv_room=cbx_selectnmrs()
            nm_rm=int(itms[0].get())
            for key in slv_room.keys():
                if nm_rm==slv_room[key]:
                    id_rm=key
            nm_cl=str(itms[1].get())
            for key in slv_kl.keys():
                if nm_cl==slv_kl[key]:
                    id_kl=key
            crs.execute("DELETE FROM resrvd WHERE id_client=? and date_chckin=? and date_evict=? and id_room=?",(id_kl,selecteditem[2],selecteditem[3],id_rm))
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
def update_bron(itms,table):
    def upd_brn():
        if table.selection():
            con=connectDB()
            crs=con.cursor()
            curItem = table.focus()
            contents =(table.item(curItem))
            selecteditem = contents['values']
            slv_kl=cbx_selectklts()
            slv_room=cbx_selectnmrs()
            nm_rm=int(itms[0].get())
            nm_rmsel=int(selecteditem[0])
            for key in slv_room.keys():
                if nm_rm==slv_room[key]:
                    id_rm=key
                if nm_rmsel==slv_room[key]:
                    id_rmsel=key
            nm_cl=str(itms[1].get())
            nm_clsel=str(selecteditem[1])
            for key in slv_kl.keys():
                if nm_cl==slv_kl[key]:
                    id_kl=key
                if nm_clsel==slv_kl[key]:
                    id_clsel=key
            crs.execute("UPDATE resrvd SET id_client=?,date_chckin=?,date_evict=?,id_room=? WHERE id_client=? and date_chckin=? and date_evict=? and id_room=?",(id_kl,itms[2].get(),itms[3].get(),id_rm,id_clsel,selecteditem[2],selecteditem[3],id_rmsel))
            con.commit()
            con.close() 
            view_tab_rec_bron(table)   
        else:
            mb.showerror('Ошибка','Не выделена запись')
    return upd_brn

def update_clnt(table,itms):
    def upd_cl():
        if table.selection():
            con=connectDB()
            crs=con.cursor()
            curItem = table.focus()
            contents =(table.item(curItem))
            selecteditem = contents['values']
            crs.execute("UPDATE client SET FIO=?,phone=?,grzhd=?,udostlich=?,seria=?,nomer=?,visa=?,visabegdat=?,visaenddate=? WHERE FIO=(?)",(str(itms[0].get()),str(itms[1].get()),str(itms[2].get()),str(itms[3].get()),str(itms[4].get()),str(itms[5].get()),str(itms[6].get()),str(itms[7].get()),str(itms[8].get()),selecteditem[0],))
            con.commit()
            con.close()
            view_tab_rec_kli(table)
        else:
            mb.showerror('Ошибка','Не выделена запись')
    return upd_cl

def update_trooms(table,itms):
    def upd_trm():
        if table.selection():
            con=connectDB()
            crs=con.cursor()
            curItem = table.focus()
            contents =(table.item(curItem))
            selecteditem = contents['values']
            crs.execute("UPDATE trooms SET t_room=?,kolvo_mest=?,price=? WHERE t_room=(?)",(str(itms[0].get()),str(itms[1].get()),float(itms[2].get()),selecteditem[0]))
            con.commit()
            con.close()
            view_tab_rec_trooms(table)
        else:
            mb.showerror('Ошибка','Не выделена запись')
    return upd_trm
def update_uslgs(table,itms):
    def upd_usl():
        if table.selection():
            con=connectDB()
            crs=con.cursor()
            curItem = table.focus()
            contents =(table.item(curItem))
            selecteditem = contents['values']
            crs.execute("UPDATE uslugs SET name_usluga=?,ed_izm=?,price=? WHERE name_usluga=?",(str(itms[0].get()),str(itms[1].get()),str(itms[2].get()),selecteditem[0],))
            con.commit()
            con.close()
            view_tab_rec_uslgs(table)
        else:
            mb.showerror('Ошибка','Не выделена запись')
    return upd_usl



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

def update_nmb(itms,table):
    def upd_nmb():
        if table.selection():
            con=connectDB()
            crs=con.cursor()
            curItem = table.focus()
            contents =(table.item(curItem))
            selecteditem = contents['values']
            slv_troom=cbx_tpnmrs()
            nm_trm=str(itms[0].get())
            nm_trm_sel=str(selecteditem[0])
            for key in slv_troom.keys():
                if nm_trm==slv_troom[key]:
                    id_trm=key
                if nm_trm_sel==slv_troom[key]:
                    id_trm_sel=key
            crs.execute("Select price from type_room WHERE id_type=?",(id_trm,))
            prc=crs.fetchone()
            crs.execute("UPDATE rooms SET id_type_room=?,nmb_room=? WHERE id_type_room=? and nmb_room=?",(id_trm,itms[1].get(),id_trm_sel,selecteditem[1]))
            con.commit()
            con.close()
            view_tab_rec_rooms(table)    
        else:
            mb.showerror('Ошибка','Не выделена запись')
    return upd_nmb

def delete_nmb(table):
    def del_nmb():
        if table.selection():
            con=connectDB()
            crs=con.cursor()
            curItem = table.focus()
            contents =(table.item(curItem))
            selecteditem = contents['values']
            table.delete(curItem)
            crs.execute("DELETE FROM rooms WHERE nmb_room=(?)",(selecteditem[1],))
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
            slv_kl=cbx_selectklts()
            nm_cl=str(selecteditem[1])
            for key in slv_kl.keys():
                if nm_cl==slv_kl[key]:
                    id_kl=key
            slv_uslgs=cbx_selectuslgs()
            nm_usl=str(selecteditem[0])
            for key in slv_uslgs.keys():
                if nm_usl==slv_uslgs[key]:
                    id_usl=key
            crs.execute("DELETE FROM ispolz_uslug WHERE id_usluga=? and id_client=? and kol_vo=? and date_usg=? and price=?",(id_usl,id_kl,selecteditem[2],selecteditem[3],selecteditem[4]))
            con.commit()
            con.close()
            
        else:
            mb.showerror('Ошибка','Не выделена запись')
    return del_okusl

def update_okusl(itms,table):
    def upd_okusl():
        if table.selection():
            con=connectDB()
            crs=con.cursor()
            curItem = table.focus()
            contents =(table.item(curItem))
            selecteditem = contents['values']
            table.delete(curItem)
            slv_kl=cbx_selectklts()
            nm_cl=str(itms[1].get())
            nm_cl_sel=str(selecteditem[1])
            for key in slv_kl.keys():
                if nm_cl==slv_kl[key]:
                    id_kl=key
                if nm_cl_sel==slv_kl[key]:
                    id_kl_sel=key
            slv_uslgs=cbx_selectuslgs()
            nm_usl=str(itms[0].get())
            nm_usl_sel=str(selecteditem[0])
            for key in slv_uslgs.keys():
                if nm_usl==slv_uslgs[key]:
                    id_usl=key
                if nm_usl_sel==slv_uslgs[key]:
                    id_usl_sel=key                
            crs.execute("Select price from uslugs WHERE id_usluga=?",(id_usl,))
            price=crs.fetchone()
            kol=int(itms[2].get())
            prc=float(price[0])*kol
            crs.execute("UPDATE ispolz_uslug SET id_usluga=?,id_client=?,date_usg=?,kol_vo=?,price=? WHERE id_usluga=? and id_client=? and kol_vo=? and date_usg=? and price=?",(int(id_usl),int(id_kl),itms[3].get(),kol,prc,id_usl_sel,id_kl_sel,selecteditem[2],selecteditem[3],selecteditem[4]))
            con.commit()
            con.close()
            view_tab_rec_okuslgs(table)
        else:
            mb.showerror('Ошибка','Не выделена запись')
    return upd_okusl

