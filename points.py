# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 07:28:26 2023

Version 1, using only tkinter.

@author: i-JL
"""

from tkinter import *

win=Tk()

win.iconbitmap("ico_name.ico")  # Change with your desired icon's absolute path
win.title("Points Calculator")
win.geometry("258x210") # 258 is the minimum to fit in the entirety of the title

def key_press(e):
    exact_label.config(text=cal_output())

def cal_output():
   t1 = int(a.get())
   confidence_level = scale_bar.get() / 100
   t1 *= 0.375 * confidence_level
   r1 = round(t1)
   exact_label.config(text=t1)
   rounded_label.config(text=r1)

a=Entry(win, width=20)
a.pack(pady=15)
    
rounded_label = Label(win, text="(Enter current points)", font=('Calibri 15 bold'))
rounded_label.pack(pady=2)

exact_label = Label(win, text="(Non-rounded result)", font=('Calibri 8'))
exact_label.pack(pady=10)

scale_bar = Scale(win, from_=0, to=100, tickinterval=50, resolution=5, label="Condifence (%)", orient=HORIZONTAL, font=('Calibri 10'), command=key_press)
scale_bar.set(100)
scale_bar.pack()

win.bind('<KeyPress>',key_press)

win.mainloop()
