# https://www.youtube.com/watch?v=nvyX8JfoOWY
import sys
import tkinter
from tkinter import ttk
import fonction
from functools import partial
import serial.tools.list_ports
import function_menubar

# --------------Declaration des variables-----------------
bool_COM_open = False
couleur_principal = "#41B77F"

# parametrage de la fenetre principale
root = tkinter.Tk()
root.title("Sniffeur COM")
# root.state("zoomed")  # la fenetre est agrandi au demarrage
root.geometry("800x600")  # fenetre en resolution 800x600
root.config(background=couleur_principal)

# https://stackoverflow.com/questions/41522427/get-combobox-value-in-python

# --------------AJOUT DES CHAMPS---------------------------
Frame_param_uart = tkinter.Frame(root,bg='pink')
Frame_param_uart.pack(fill='both',side='left',expand=True)
# -----PORT
lab_port = tkinter.Label(Frame_param_uart,text="Port")
lab_port.place()


# ----------------WIDGET PORT COM-----------------
def get_port():
    content = fonction.get_port_com()
    combo_com_port.config(values=content)
    print("get_port()")


def test(*args):
    print(var_combo_com_com.get())


lab_com_port = tkinter.Label(Frame_param_uart,text="COM")
lab_com_port.pack()
arr_combo_com_com = []  # fonction.get_port_com()
var_combo_com_com = tkinter.StringVar()
var_combo_com_com.trace("w",test)
"""
combo_com_port = ttk.Combobox(Frame_param_uart,textvariable=var_combo_com_com,values=arr_combo_com_com,
                              state='readonly',postcommand=get_port)  # clique sur le combobox  
"""
combo_com_port = ttk.Combobox(Frame_param_uart,textvariable=var_combo_com_com,values=arr_combo_com_com,
                              state='readonly',postcommand=get_port)  # clique sur le combobox
# combo_com_port.bind("<<ComboboxSelected>>",get_port)  # selection d'un port
combo_com_port.pack()

# ----------------WIDGET BAUDRATE----------------
lab_baud = tkinter.Label(Frame_param_uart,text="Baudrate")
lab_baud.pack()
arr_combo_com_baud = [50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200,230400,460800,
                      500000,576000,921600,1000000,1152000,1500000,2000000,2500000,3000000,3500000,4000000]
var_combo_com_baud = tkinter.StringVar()
combo_com_baud = ttk.Combobox(Frame_param_uart,textvariable=var_combo_com_baud,values=arr_combo_com_baud,
                              state='readonly')
combo_com_baud.pack()

# ----------------WIDGET BYTESIZE----------------
lab_baud = tkinter.Label(Frame_param_uart,text="ByteSize")
lab_baud.pack()
arr_combo_com_bytesize = ["5","6","7","8"]
var_combo_com_bytesize = tkinter.StringVar()
combo_com_bytesize = ttk.Combobox(Frame_param_uart,textvariable=var_combo_com_bytesize,values=arr_combo_com_bytesize,
                                  state='readonly')
combo_com_bytesize.pack()
a = 1
b = 1
# ----------------WIDGET PARITY----------------
lab_parity = tkinter.Label(Frame_param_uart,text="Parity")
lab_parity.pack()
arr_combo_com_parity = ["none","even","odd","mark","space"]
var_combo_com_parity = tkinter.StringVar()
combo_com_parity = ttk.Combobox(Frame_param_uart,textvariable=var_combo_com_parity,values=arr_combo_com_parity,
                                state='readonly')
combo_com_parity.pack()

# ----------------WIDGET BITSTOP----------------
lab_bitstop = tkinter.Label(Frame_param_uart,text="bit de stop")
lab_bitstop.pack()
arr_combo_com_bitstop = ["1","1.5","2"]
var_combo_com_bitstop = tkinter.StringVar()
combo_com_bitstop = ttk.Combobox(Frame_param_uart,textvariable=var_combo_com_bitstop,values=arr_combo_com_bitstop,
                                 state='readonly')
combo_com_bitstop.pack()


# # ----------------WIDGET OUVERTUR/FERMETURE COM---
def call_com_ouvrir():
    # print("call_com_ouvrir" + combo_com_port.get())
    fonction.com_ouvrir(combo_com_port.get(),combo_com_baud.get(),combo_com_bytesize.get(),combo_com_parity.get(),
                        combo_com_bitstop.get(),bouton_com_ouvrirFermer)


bouton_com_ouvrirFermer = ttk.Button(Frame_param_uart,text="Ouvrir COM",command=call_com_ouvrir)
bouton_com_ouvrirFermer.pack()

# ----------WIDGET MENU BAR
function_menubar.menubar(root)

root.mainloop()
