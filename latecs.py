import tkinter as tk
import pyperclip as pc
import numpy as np

lx = tk.Tk()
lx.title('Late(ne)x Adentro')
lx.configure(bg='#1c212e')
lx.geometry('200x200+510+510')

def printInput(text):
    pc.copy(text)
w1 = 11
frac = tk.Button(lx, text='Fraccion', command=lambda *args: printInput('\\frac{}{}'), height=1, width=w1, bg='#647ab5')
frac.grid(row=1,column=0)

inttop = tk.StringVar()
intbot = tk.StringVar()
n_size = tk.Entry(lx, textvariable = inttop, width=5, bg='#647ab5').grid(row=2,column=1)
m_size = tk.Entry(lx, textvariable = intbot, width=5, bg='#647ab5').grid(row=2,column=2)
def integral():
    limitearriba = inttop.get()
    limiteabajo = intbot.get()
    return(limitearriba,limiteabajo)
int = tk.Button(lx, text='Integral', command=lambda *args: printInput('\displaystyle \int\limits^{'+integral()[0]+'}_{'+integral()[1]+'}'), height=1, width=w1, bg='#647ab5')
int.grid(row=2,column=0)

sum = tk.Button(lx, text='Sumatoria', command=lambda *args: printInput('\displaystyle \sum_{n=}^{}'), height=1, width=w1, bg='#647ab5')
sum.grid(row=3,column=0)

pwr = tk.Button(lx, text='Potencia', command=lambda *args: printInput('^{}'), height=1, width=w1, bg='#647ab5')
pwr.grid(row=4,column=0)

sqrt = tk.Button(lx, text='Raiz', command=lambda *args: printInput('\sqrt{}'), height=1, width=w1, bg='#647ab5')
sqrt.grid(row=5,column=0)

bpi = tk.Button(lx, text='Multiplicatoria', command=lambda *args: printInput('\displaystyle \prod_{i=}^{}'), height=1, width=w1, bg='#647ab5')
bpi.grid(row=6,column=0)

no=tk.IntVar(value=1)
mo=tk.IntVar(value=1)
n_size = tk.Entry(lx, textvariable = mo, width=2, bg='#647ab5').grid(row=7,column=1)
m_size = tk.Entry(lx, textvariable = no, width=2, bg='#647ab5').grid(row=7,column=2)

def openmatrix():
    n = no.get()
    m = mo.get()
    matriz = tk.Toplevel(lx)
    matriz.configure(bg='#1c212e')
    matriz.attributes('-topmost',True)
    for j in np.arange(1,m+1,1):
        for i in np.arange(1,n+1,1):
            exec(f'global noi{i}{j};noi{i}{j} = tk.StringVar(value=''0'')')
            exec(f'global a_{i}{j}; a_{i}{j} = tk.Entry(matriz, textvariable = noi{i}{j}, bg="#647ab5").grid(row=i,column=j)')
    def fill():
        inside = ''
        for j in np.arange(1,m+1,1):
            for i in np.arange(1,n+1,1):
                exec(f'global add;add = noi{i}{j}.get()')
                inside += add
                inside += '&'
            inside = inside[:-1]
            inside += '\\\\'
        return(inside)
    menumtx = tk.Menubutton(matriz, text = "Copiar (estilo)", relief='raised', bg='#647ab5')
    menumtx.menu = tk.Menu(menumtx, selectcolor='#647ab5', activebackground='#647ab5', bg='#647ab5', bd='0')
    menumtx["menu"] = menumtx.menu
    menumtx.menu.add_checkbutton(label = "Nada", command=lambda *args:  printInput('\\begin{matrix}'+fill()+'\end{matrix}'))
    menumtx.menu.add_checkbutton(label = "Parentesis", command=lambda *args:  printInput('\\begin{pmatrix}'+fill()+'\end{pmatrix}'))
    menumtx.menu.add_checkbutton(label = "Corchetes", command=lambda *args:  printInput('\\begin{bmatrix}'+fill()+'\end{bmatrix}'))
    menumtx.menu.add_checkbutton(label = "Llaves", command=lambda *args:  printInput('\\begin{Bmatrix}'+fill()+'\end{Bmatrix}'))
    menumtx.menu.add_checkbutton(label = "Verticales", command=lambda *args:  printInput('\\begin{vmatrix}'+fill()+'\end{vmatrix}'))
    menumtx.menu.add_checkbutton(label = "Dosverticales", command=lambda *args:  printInput('\\begin{Vmatrix}'+fill()+'\end{Vmatrix}'))
    menumtx.grid(row=n+2,column=0)

opm = tk.Button(lx, text='Matriz', command=openmatrix, height=1, width=w1, bg='#647ab5')
opm.grid(row=7,column=0)

lx.attributes('-topmost',True)
lx.mainloop()