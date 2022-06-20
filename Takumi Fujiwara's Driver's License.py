# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 18:31:16 2022

@author: ramit
"""

from tkinter import *
from tkinter.font import Font
root = Tk()
root.title("Takumi Fujiwara's Driver's Licence")
root.geometry("860x239")
root.iconbitmap('f:/ra.jpeg')
root.configure(background='Black')
btn_dl = Button(root, text="運転免許証", width=1000, bg="Red", font=("Arial", 40), fg="White")
label_id = Label(root, text="ID：666666666", font=("Courier New", 30), fg="white", bg="black")
label_first_name = Label(root, text="名：匠", font=("Courier New", 30), fg="white", bg="black")
label_last_name = Label(root, text="姓：藤原", font=("Courier New", 30), fg="white", bg="black")
label_date_of_birth = Label(root, text="生年月日：1998年4月18日", font=("Courier New", 30), fg="white", bg="black")
label_pin = Label(root, text="ピン: 86-239", font=("Courier New", 30), fg="white", bg="black")
label_address = Label(root, text="住所：2167-4 Yorii、Shibukawa、Gunma 377-0008、Japan", font=("Courier New", 30), fg="white", bg="black")
label_autorization_to_drive_the_following_vehicles = Label(root, text="次の車両を運転する許可：コンパクトスポーツ", font=("Courier New", 20), fg="white", bg="black")
btn_dl.pack()
label_id.place(relx=0.5, rely=0.3, anchor=CENTER)
label_first_name.place(relx=0.5, rely=0.4, anchor=CENTER)
label_last_name.place(relx=0.5, rely=0.5, anchor=CENTER)
label_date_of_birth.place(relx=0.5, rely=0.6, anchor=CENTER)
label_pin.place(relx=0.5, rely=0.7, anchor=CENTER)
label_address.place(relx=0.5, rely=0.8, anchor=CENTER)
label_autorization_to_drive_the_following_vehicles.place(relx=0.5, rely=0.9, anchor=CENTER)
root.mainloop()