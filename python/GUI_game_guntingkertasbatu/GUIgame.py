import tkinter
from tkinter import *
from tkinter import messagebox
import random
from PIL import ImageTk

def proses(pemain): #proses game berjalan
    pilihan = ["gunting", "kertas", "batu"]
    komputer = random.choice(pilihan)
    #printhasil = None
    if pemain == komputer:
        printhasil = "Kamu memilih "+pemain.upper()+"\nKomputer memilih "+komputer.upper()+ "\nHASIL SERI"
        print(printhasil)
        #(print("Kamu memilih "+pemain.upper() ),
        #print("Komputer memilih "+komputer.upper()),
        #print("Seri"))
        messagebox.showinfo(title='HASIL SERI!!!',
                            message= printhasil,)
    elif pemain == "batu":
        if komputer == "kertas":
            printhasil = "Kamu memilih "+pemain.upper()+"\nKomputer memilih "+komputer.upper()+ "\nHASIL KALAH"
            #print("Kamu memilih " + pemain.upper())
            #print("Komputer memilih " + komputer.upper())
            #print("Kamu Kalah")
            messagebox.showinfo(title='KALAH :(',
                                message=printhasil)
        elif komputer == "gunting":
            printhasil = "Kamu memilih " + pemain.upper() + "\nKomputer memilih " + komputer.upper() + "\nHASIL MENANG!"
            #print("Kamu memilih " + pemain.upper())
            #print("Komputer memilih " + komputer.upper())
            #print("Kamu Menang!")
            messagebox.showinfo(title='MENANG!!!',
                                message=printhasil)

    elif pemain == "gunting":
        if komputer == "kertas":
            printhasil = "Kamu memilih " + pemain.upper() + "\nKomputer memilih " + komputer.upper() + "\nHASIL MENANG!"
            #print("Kamu memilih " + pemain.upper())
            #print("Komputer memilih " + komputer.upper())
            #print("Kamu Menang!")
            messagebox.showinfo(title='MENANG!!!',
                                message=printhasil)
        elif komputer == "batu":
            printhasil = "Kamu memilih " + pemain.upper() + "\nKomputer memilih " + komputer.upper() + "\nHASIL KALAH"
            #print("Kamu memilih " + pemain.upper())
            #print("Komputer memilih " + komputer.upper())
            #print("Kamu Kalah")
            messagebox.showinfo(title='KALAH :(',
                                message=printhasil)

    elif pemain == "kertas":
        if komputer == "gunting":
            printhasil = "Kamu memilih " + pemain.upper() + "\nKomputer memilih " + komputer.upper() + "\nHASIL KALAH"
            #print("Kamu memilih " + pemain.upper())
            #print("Komputer memilih " + komputer.upper())
            #print("Kamu Kalah")
            messagebox.showinfo(title='KALAH :(',
                                message=printhasil)
        elif komputer == "batu":
            printhasil = "Kamu memilih " + pemain.upper() + "\nKomputer memilih " + komputer.upper() + "\nHASIL MENANG!"
            #print("Kamu memilih " + pemain.upper())
            #print("Komputer memilih " + komputer.upper())
            #print("Kamu Menang!")
            messagebox.showinfo(title='MENANG!!!',
                                message=printhasil)

def gunting():
    proses("gunting")

def kertas():
    proses("kertas")

def batu():
    proses("batu")

def hasil(inputhasil):
    messagebox.showinfo(title='HASIL', message= inputhasil)


#window utama
window = Tk()
window.geometry("550x500")
#window.eval('tk::PlaceWindow . center')
window.title("GUI game batu gunting kertas")
#window utama


bg = ImageTk.PhotoImage(file= 'blackcat moonmini.png')
label1 = Label(window, image=bg)
label1.pack()

label0 = Label(window,
               text='SELAMAT BERMAIN!!!\n Silahkan pilih GUNTING / KERTAS / BATU',
               font= 'monoid',
               bg='dark grey',
               fg='white')
label0.place(x=150)

pbatu = PhotoImage(file= 'mbatu.png')
pgunting = PhotoImage(file= 'mgunting.png')
pkertas = PhotoImage (file= 'mkertas.png')
# button
bgunting = Button(window,
                  #text= 'GUNTING',
                  command=gunting,
                  image=pgunting)
bgunting.place(x=25, y=300)
#bgunting.pack(side=LEFT)

bkertas = Button(window,
                  #text= 'KERTAS',
                  command=kertas,
                 image=pkertas)
bkertas.place(x=225, y=300)
#bkertas.pack()

bbatu = Button(window,
                  #text= 'BATU',
                  command=batu,
               image=pbatu)
bbatu.place(x=425, y=300)
#bbatu.pack()
# button

# window utama
icon = PhotoImage(file='bblackcat.png')
window.iconphoto(True,icon)
#window.config(background='black')
window.mainloop()
# window utama