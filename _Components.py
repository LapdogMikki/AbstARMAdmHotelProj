import tkinter as tkntr
from tkinter.constants import HORIZONTAL
import tkinter.ttk as tkttk

class MFormTabFrame(tkntr.Frame):
    def __init__(self,parent,headings=tuple(), rows=tuple()):
        tkntr.Frame.__init__(self,parent,background="white")
        self.parent = parent
        table = tkttk.Treeview(self, show="headings", selectmode="browse")
        table["columns"] = headings
        table["displaycolumns"] = headings
        for head in headings:
            table.heading(head, text=head, anchor=tkntr.CENTER)
            table.column(head, anchor=tkntr.CENTER)
        for row in rows:
            table.insert('', tkntr.END, values=tuple(row))
        scrolltable = tkntr.Scrollbar(self, command=table.yview)
        xscrolltable = tkntr.Scrollbar(self, command=table.xview, orient=HORIZONTAL)
        table.configure(yscrollcommand=scrolltable.set)
        table.configure(xscrollcommand=xscrolltable.set)
        scrolltable.pack(side=tkntr.RIGHT, fill=tkntr.Y)
        xscrolltable.pack(side=tkntr.BOTTOM, fill=tkntr.X)
        table.pack(expand=tkntr.YES, fill=tkntr.BOTH)
        self.initUI()  
    def initUI(self):
        self.pack(fill=tkntr.BOTH,expand=1) 