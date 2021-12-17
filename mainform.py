
import tkinter as tkntr
from tkinter.constants import COMMAND
import tkinter.ttk as tkttk

import _dbconnect as dbcon
import _Components as comp

def main():
    root = tkntr.Tk()
    root.title("АРМ администратора")
    width=root.winfo_screenwidth() 
    height=root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))
    root.resizable(width=False, height=False)
    note = tkttk.Notebook(root)
    brn = comp.MFormTabFrame(root,headings=('Номер','Клиент','Дата заселения','Дата выселения'),rows=dbcon.showtabbron(),hb=5,hcbx=2,he=2)
    note.add(brn, text = "Бронирование номеров")
    kli = comp.MFormTabFrame(root,headings=('ФИО','Телефон','Гражданство','Уд.личности','Серия','Номер','Виза (п.н)','Дата нач.действия','Дата оконч.действия'),rows=dbcon.showtabkli(),hb=5,he=9)
    note.add(kli, text = "Клиенты")
    rms = comp.MFormTabFrame(root,headings=('Номер','Тип номера','Цена'),rows=dbcon.showtabrms(),hb=5,he=3)
    note.add(rms, text = "Номера")
    tprms = comp.MFormTabFrame(root,headings=('Тип номера','Кол-во мест','Цена'),rows=dbcon.showtabtprms(),hb=5,he=3)
    note.add(tprms, text = "Типы номеров")
    uslg = comp.MFormTabFrame(root,headings=('Услуга','Ед.измерения','Цена'),rows=dbcon.showtabusl(),hb=5,he=3)
    note.add(uslg, text = "Услуги")
    okusl = comp.MFormTabFrame(root,headings=('Услуга','Клиент','Количество','Дата','Цена'),rows=dbcon.showtabokusl(),hb=5,hcbx=2,he=3)
    note.add(okusl, text = "Оказанные услуги")
    note.pack()
    root.mainloop()

if __name__=='__main__':
    main()