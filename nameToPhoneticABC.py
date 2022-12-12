import phonetic_alphabet as alpha 
from tkinter import * #import GUI lib

def nameToPhoneticABC() :
    given_name = name.get()
    response = alpha.read(given_name)
    display.config(text=str(response).capitalize())

#use GUI module
root = Tk()
root.title("Name to Phonetic ABC")
root.geometry("650x400")

name = StringVar()

# Adding title
title = Label(root, text="Name to Phonetic ABC",
               fg="Blue", font=("Arial", 20, 'bold')).place(x=150, y=10)

# Options
formats_label = Label(root, text="Formats supported :  ",
               fg="green", font=("Arial", 10, 'bold')).place(x=100, y=70)
str_format_label = Label(root, text="1. Strings ",
               fg="green", font=("Arial", 10, 'bold')).place(x=200, y=90)
num_format_label = Label(root, text="2. Numbers ",
               fg="green", font=("Arial", 10, 'bold')).place(x=200, y=110)


name_entry_label = Label(root, text="Enter a name :",
               fg="Blue", font=("Arial", 15, 'bold')).place(x=50, y=200)
name_entry = Entry(root,textvariable=name,width=30).place(x=220, y=200)


btn = Button(master=root, text="convert",fg="green", font=("Arial", 10, 'bold')
             ,command=nameToPhoneticABC).place(x=280,y=230)


display = Label(root, text="",fg="black", font=("Arial", 10, 'bold'))
display.place(x=10, y=300)


photo = PhotoImage(file = "nameToPhoneticABC/phoneticABC.png")
root.iconphoto(False, photo)

root.mainloop()