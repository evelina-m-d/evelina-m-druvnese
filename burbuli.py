from tkinter import *
from random import *
from math import *

logs = Tk()
garums = 700
platums = 700
logs.title('Burbuļu spridzinātājs')

a = Canvas(logs, width=platums, height=garums, bg='#427D9D')
a.pack()
kuga_id = a.create_oval(0,0,100,100,outline='#9BBEC8', width=5)





mainloop()