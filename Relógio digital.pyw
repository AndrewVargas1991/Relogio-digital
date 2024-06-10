from tkinter import *
from tkinter.ttk import *
from time import strftime

janela = Tk()
janela.title('Relogio digital')
janela.resizable('False', 'False')

def tempo():
	var = strftime(f'%H:%M:%S - %d/%m/%y')
	hora.config(text=var)
	hora.after(1000, tempo)

hora = Label(janela, font=('Times New Roman', 30))
hora.pack(anchor='center')
tempo()

janela.mainloop()