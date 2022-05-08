import sys
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import fonction

import serial.tools.list_ports


def menubar(root):
    menu_bar = tk.Menu(root)
    menu_file = tk.Menu(menu_bar)
    menu_file.add_command(label="Open",command=menubar_file_open)
    menu_file.add_command(label="Save")
    menu_file.add_command(label="Exit")
    menu_help = tk.Menu(menu_bar)
    menu_help.add_command(label="About",command=menubar_help_about)
    menu_bar.add_cascade(label="File",menu=menu_file)
    menu_bar.add_cascade(label="Help",menu=menu_help)
    root.config(menu=menu_bar)


def menubar_file_open():
    print("appui sur File->Open")


def menubar_help_about():
    tkinter.messagebox.showinfo(title="About",message="Made by ghost54770")
