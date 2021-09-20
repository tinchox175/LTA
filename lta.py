import tkinter as tk
from PIL import ImageTk, Image
import pyperclip as pc
import numpy as np
import requests
import os
from io import BytesIO

lx = tk.Tk()
lx.title('Late(ne)x Adentro')
lx.configure(bg='#1c212e')
lx.geometry('500x230+50+50')

def printInput(text):
    pc.copy(text)
w1 = 11

ftop = tk.StringVar()
fbot = tk.StringVar()
fn_size = tk.Entry(lx, textvariable = ftop, width=5, bg='#647ab5').grid(row=1,column=1)
fm_size = tk.Entry(lx, textvariable = fbot, width=5, bg='#647ab5').grid(row=1,column=2)
def fraccion():
    limitearriba = ftop.get()
    limiteabajo = fbot.get()
    return(limitearriba,limiteabajo)
frac = tk.Button(lx, text='Fraccion', command=lambda *args: printInput('\\frac{'+fraccion()[0]+'}{'+fraccion()[0]+'}'), height=1, width=w1, bg='#647ab5')
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

stop = tk.StringVar()
sbot = tk.StringVar()
sn_size = tk.Entry(lx, textvariable = stop, width=5, bg='#647ab5').grid(row=3,column=1)
sm_size = tk.Entry(lx, textvariable = sbot, width=5, bg='#647ab5').grid(row=3,column=2)
def sumatoria():
    limitearriba = stop.get()
    limiteabajo = sbot.get()
    return(limitearriba,limiteabajo)
sum = tk.Button(lx, text='Sumatoria', command=lambda *args: printInput('\displaystyle \sum_{n='+sumatoria()[0]+'}^{'+sumatoria()[1]+'}'), height=1, width=w1, bg='#647ab5')
sum.grid(row=3,column=0)

ptop = tk.StringVar()
pn_size = tk.Entry(lx, textvariable = ptop, width=5, bg='#647ab5').grid(row=4,column=1)
def potencia():
    limitearriba = ptop.get()
    return(limitearriba)
pwr = tk.Button(lx, text='Potencia', command=lambda *args: printInput('^{'+potencia()+'}'), height=1, width=w1, bg='#647ab5')
pwr.grid(row=4,column=0)

rtop = tk.StringVar()
rn_size = tk.Entry(lx, textvariable = rtop, width=5, bg='#647ab5').grid(row=5,column=1)
def raiz():
    limitearriba = rtop.get()
    return(limitearriba)
sqrt = tk.Button(lx, text='Raiz', command=lambda *args: printInput('\sqrt{'+raiz()+'}'), height=1, width=w1, bg='#647ab5')
sqrt.grid(row=5,column=0)

mtop = tk.StringVar()
mbot = tk.StringVar()
mn_size = tk.Entry(lx, textvariable = mtop, width=5, bg='#647ab5').grid(row=6,column=1)
mm_size = tk.Entry(lx, textvariable = mbot, width=5, bg='#647ab5').grid(row=6,column=2)
def multiplicatoria():
    limitearriba = mtop.get()
    limiteabajo = mbot.get()
    return(limitearriba,limiteabajo)
bpi = tk.Button(lx, text='Multiplicatoria', command=lambda *args: printInput('\displaystyle \prod_{i='+multiplicatoria()[0]+'}^{'+multiplicatoria()[1]+'}'), height=1, width=w1, bg='#647ab5')
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
    menumtx.menu.add_command(label = "Nada", command=lambda *args:  printInput('\\begin{matrix}'+fill()+'\end{matrix}'))
    menumtx.menu.add_command(label = "Parentesis", command=lambda *args:  printInput('\\begin{pmatrix}'+fill()+'\end{pmatrix}'))
    menumtx.menu.add_command(label = "Corchetes", command=lambda *args:  printInput('\\begin{bmatrix}'+fill()+'\end{bmatrix}'))
    menumtx.menu.add_command(label = "Llaves", command=lambda *args:  printInput('\\begin{Bmatrix}'+fill()+'\end{Bmatrix}'))
    menumtx.menu.add_command(label = "Verticales", command=lambda *args:  printInput('\\begin{vmatrix}'+fill()+'\end{vmatrix}'))
    menumtx.menu.add_command(label = "Dosverticales", command=lambda *args:  printInput('\\begin{Vmatrix}'+fill()+'\end{Vmatrix}'))
    menumtx.grid(row=n+2,column=0)

opm = tk.Button(lx, text='Matriz', command=openmatrix, height=1, width=w1, bg='#647ab5')
opm.grid(row=7,column=0)

ectxt = tk.StringVar()
ectxt_entry = tk.Entry(lx, textvariable = ectxt, width=26, bg='#647ab5').grid(row=1,column=6)
def fectxt():
    limitearriba = ectxt.get()
    return(limitearriba)
ecname = tk.StringVar()
ecname_entry = tk.Entry(lx, textvariable = ecname, width=10, bg='#647ab5').grid(row=1,column=7)
def name():
    limitearriba = ecname.get()
    return(limitearriba)
ec = tk.Button(lx, text='Ecuación', command=lambda *args: printInput('\\begin{equation}'+fectxt()+'\label{eq:'+name()+'}\end{equation}'), height=1, width=w1, bg='#647ab5')
ec.grid(row=1,column=5)

def imagenadd():
    w2 = 10
    imagen = tk.Toplevel(lx)
    imagen.configure(bg='#1c212e')
    imagen.attributes('-topmost',True)
    label = tk.Frame(imagen, bg='#1c212e')
    label.pack(side='top')
    muestra = tk.Frame(imagen, bg='#1c212e')
    muestra.pack(side='left')
    botones = tk.Frame(imagen, bg='#1c212e')
    botones.pack(side='bottom')
    lbl = tk.StringVar(value='fig')
    lbl_entry = tk.Entry(label, textvariable = lbl, width=30, bg='#647ab5').grid(row=1,column=1)
    def laibel():
        leibel = 'label{fig:'+lbl.get()+'}'
        return(leibel)
    label = tk.Label(label, text='Label', relief='ridge', width=9, bg='#647ab5')
    label.grid(row=1,column=0)
    url = tk.StringVar(value='figura.png')
    url_entry = tk.Entry(muestra, textvariable = url, width=30, bg='#647ab5')
    url_entry.grid(row=1,column=0)
    def link():
        uerreele = url.get()
        return(uerreele)
    def posicion(lugar):
        global position; position = lugar
        return(position)
    menupos = tk.Menubutton(botones, text = "Posición", width=10, relief='raised', bg='#647ab5')
    menupos.menu = tk.Menu(menupos, selectcolor='#647ab5', activebackground='#647ab5', bg='#647ab5', bd='0')
    menupos["menu"] = menupos.menu
    menupos.menu.add_command(label = "Derecha", command=lambda *args:  posicion('\\raggedright'))
    menupos.menu.add_command(label = "Centrado", command=lambda *args:  posicion('\\centering'))
    menupos.menu.add_command(label = "Izquierda", command=lambda *args:  posicion('\\raggedleft'))
    menupos.grid(row=0,column=0)
    def plcmnt(lugardoc):
        global posdoc; posdoc = '['+lugardoc+']'
        return(posdoc)
    menuplc = tk.Menubutton(botones, text = "Lugar", width=10, relief='raised', bg='#647ab5')
    menuplc.menu = tk.Menu(menuplc, selectcolor='#647ab5', activebackground='#647ab5', bg='#647ab5', bd='0')
    menuplc["menu"] = menuplc.menu
    menuplc.menu.add_command(label = "Arriba", command=lambda *args:  plcmnt('t'))
    menuplc.menu.add_command(label = "Acá", command=lambda *args:  plcmnt('h'))
    menuplc.menu.add_command(label = "Abajo", command=lambda *args:  plcmnt('b'))
    menuplc.grid(row=1,column=0)
    ttl = tk.StringVar()
    ttl_entry = tk.Entry(botones, textvariable = ttl, width=30, bg='#647ab5').grid(row=2,column=1)
    def titulo():
        tetele = '\\textbf{'+ttl.get()+'}\par\medskip'
        return(tetele)
    titulo_imagen = tk.Label(botones, text='Título', relief='ridge', width=9, bg='#647ab5')
    titulo_imagen.grid(row=2,column=0)
    cpt = tk.StringVar()
    cpt_entry = tk.Entry(botones, textvariable = cpt, width=30, bg='#647ab5').grid(row=3,column=1)
    def caption():
        cepete = '\\caption{'+cpt.get()+'}'
        return(cepete)
    caption_imagen = tk.Label(botones, text='Epígrafe', relief='ridge', width=9, bg='#647ab5')
    caption_imagen.grid(row=3,column=0)
    szz = tk.StringVar(value='1')
    szz_entry = tk.Entry(botones, textvariable = szz, width=3, bg='#647ab5').grid(row=4,column=1)
    def size():
        esezeze = '[scale='+szz.get()+']'
        return(esezeze)
    caption_imagen = tk.Label(botones, text='Tamaño', relief='ridge', width=9, bg='#647ab5')
    caption_imagen.grid(row=4,column=0)
    plcmnt('h')
    posicion('\centering')
    exportar = tk.Button(muestra, text='Exportar', command=lambda *args: printInput('\\begin{figure}'+posdoc+position+titulo()+'\includegraphics'+size()+'{'+link()+'}'+caption()+'\\'+laibel()+'\end{figure}'), height=1, width=w1, bg='#647ab5')
    exportar.grid(row=0,column=0)

    
img = tk.Button(lx, text='Imagen', command=imagenadd, height=1, width=w1, bg='#647ab5')
img.grid(row=2,column=5)

nil = tk.Label(lx, textvariable='', font=("Comic Sans",8), width=3, bg='#1c212e')
nil.grid(row=1,column=4)

def clipboard():
    w2 = 10
    cleep = tk.Toplevel(lx)
    cleep.configure(bg='#1c212e')
    cleep.attributes('-topmost',True)
    inutil = tk.StringVar(value='Escribí acá')
    escribiaca = tk.Text(cleep, bg='#647ab5').pack()
cb = tk.Button(lx, text='Clipboard', command=clipboard, height=1, width=w1, bg='#647ab5')
cb.grid(row=9,column=0)

# asdasdasd = tk.StringVar()
# cc = tk.Label(lx, textvariable=asdasdasd, font=("Comic Sans",8), bg='#647ab5')
# cc.grid(column=5,row=7)
# asdasdasd.set('Martín Sattler 2021')

lx.attributes('-topmost',True)
lx.mainloop()