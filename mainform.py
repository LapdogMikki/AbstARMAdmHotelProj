import tkinter as tkntr
import tkinter.ttk as tkttk
import _dbconnect as dbcon
import _Components as comp

def main():
    root = tkntr.Tk()
    root.title("АРМ администратора")
    note = tkttk.Notebook(root)
    n=int(4)
    brn = comp.MFormTabFrame(root,headings=('Номер','Клиент','Дата заселения','Дата выселения'),rows=dbcon.showtabbron(),btns=comp.MFormTabFrame.create_btns(root,n))
    note.add(brn, text = "Бронирование номеров")
    kli = comp.MFormTabFrame(root,headings=('ФИО','Телефон','Гражданство','Уд.личности','Серия','Номер','Виза (п.н)','Дата нач.действия','Дата оконч.действия'),rows=dbcon.showtabkli())
    note.add(kli, text = "Клиенты")
    rms = comp.MFormTabFrame(root,headings=('Номер','Тип номера','Цена'),rows=dbcon.showtabrms())
    note.add(rms, text = "Номера")
    tprms = comp.MFormTabFrame(root,headings=('Тип номера','Кол-во мест','Цена'),rows=dbcon.showtabtprms())
    note.add(tprms, text = "Типы номеров")
    uslg = comp.MFormTabFrame(root,headings=('Услуга','Ед.измерения','Цена'),rows=dbcon.showtabusl())
    note.add(uslg, text = "Услуги")
    okusl = comp.MFormTabFrame(root,headings=('Услуга','Клиент','Количество','Дата','Цена'),rows=dbcon.showtabokusl())
    note.add(okusl, text = "Оказанные услуги")
    note.pack()
    root.mainloop()
    

if __name__=='__main__':
    main()