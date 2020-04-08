import os
import imageio
import pathlib
import natsort
import glob
from tkinter import *
import tkinter as tk
from tkinter.filedialog import askdirectory


def make_gif(image_directory: pathlib.Path, destin: pathlib.Path, frames_per_second: float, namin: str, **kwargs):

    assert isinstance(image_directory, pathlib.Path), "input must be a pathlib object"
    image_type = kwargs.get('type', 'png')

    assert isinstance(destin, pathlib.Path), "input must be a pathlib object"
    #names the resulting gif
    gif_dir = destin.joinpath(namin + ".gif")

    print('Started making GIF')
    print('Please wait...\n\n\n')

    imglist = image_directory.glob('*.' + image_type)
    imglist = natsort.natsorted(imglist)

    images = []
    for file_name in imglist:
        images.append(imageio.imread(image_directory.joinpath(file_name)))
    imageio.mimsave(gif_dir.as_posix(), images, fps=frames_per_second)

    print('Finished making GIF!')
    print('GIF can be found at: ' + gif_dir.as_posix())

def main(lePath, leDestin, leFps, leName):
    png_dir = pathlib.Path(lePath)
    destin = pathlib.Path(leDestin)
    fps = leFps
    namin = leName
    make_gif(png_dir, destin, fps, namin)


window = Tk()
window.title("GIFER")
#window.geometry('555x207')
window.geometry('675x300')
window.resizable(width=False, height=False)

def clearbtn():
    txt.delete(0, END)
    txt.insert(0, "")
    txt1.delete(0, END)
    txt1.insert(0, "")
    txt2.delete(0, END)
    txt2.insert(0, "")
    txt3.delete(0, END)
    txt3.insert(0, "")
    lbl.configure(text="All Clear!                              ")
    return lbl

def pathbtn():
    foldername = askdirectory(title='Select Folder')
    v1 = StringVar(window, value=foldername)
    txt1.delete(0, END)
    txt1.insert(0, foldername)

    return foldername, v1, txt1

def destbtn():
    destname = askdirectory(title='Select Folder')
    v2 = StringVar(window, value=destname)
    txt3.delete(0, END)
    txt3.insert(0, destname)

    return destname, v2, txt3

def openbtn():
    os.chdir(txt3.get())
    os.system('open .')

def gifbtn():
    fpsy = txt.get()
    pathy = txt1.get()
    namy = txt2.get()
    desty = txt3.get()
    main(pathy, desty, fpsy, namy)
    lbl.configure(text= "Done! Open GIF or Clear")
    btn3.config(state='normal')

def gifAble(*args):
    u = stringvar.get()
    x = stringvar1.get()
    y = stringvar2.get()
    z = stringvar3.get()

    if u and x and y and z:
        btn2.config(state='normal')
        lbl.configure(text="Click 'Make GIF'                ")
    else:
        try:
            btn2.config(state='disabled')
        except NameError:
            pass
        lbl.configure(text="Make Selections               ")

    if x:
        lbl3.configure(image=filledimgy)
    else:
        try:
            lbl3.configure(image=emptyimgy)
        except NameError:
            pass

    if y:
        lbl5.configure(image=filledimgy)
    else:
        try:
            lbl5.configure(image=emptyimgy)
        except NameError:
            pass

    if z:
        lbl8.configure(image=filledimgy)
    else:
        try:
            lbl8.configure(image=emptyimgy)
        except NameError:
            pass

#styling
fam = 'rubik'
n = 20
textw = 17

#images
pathimgy = PhotoImage(file="path.png")
fpsimgy = PhotoImage(file="fps.png")
emptyimgy = PhotoImage(file="empty.png")
filledimgy = PhotoImage(file="filled.png")
infoimgy = PhotoImage(file="info.png")

#center tkinter window
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())

#vars check if text boxes are populated
stringvar = tk.StringVar(window)
stringvar1 = tk.StringVar(window)
stringvar2 = tk.StringVar(window)
stringvar3 = tk.StringVar(window)
v = StringVar(window, value='30')

stringvar.trace("w", gifAble)
stringvar1.trace("w", gifAble)
stringvar2.trace("w", gifAble)
stringvar3.trace("w", gifAble)

#(0,0) info symbol
lbl1 = Label(window, image=infoimgy)
lbl1.grid(column=0, row=0, padx=(0,0), pady=(10, 30), sticky=E)

#(1,0) helper text
lbl = Label(window, text="Make Selections               ", font=(fam, n))
lbl.grid(column=1, row=0, pady=(10, 30), padx=(10,0), sticky=W)

#(2,0) text box for fps
txt = Entry(window, width=2, textvariable=stringvar, font=(fam, n))
txt.insert(END, '30')
txt.grid(column=2, row=0, pady=(10, 30), sticky=E)

#(3,0) fps label
lbl2 = Label(window, image=fpsimgy)
lbl2.grid(column=3, row=0, pady=(10, 30), padx=(5,0), sticky=W)

#(0,1) source folder checkbox
lbl3 = Label(window, image=emptyimgy, font=(fam, n, 'bold'))
lbl3.grid(column=0, row=1, padx=(10, 0), pady=(0,15), sticky=E)

#(1,1) source folder prompt text
lbl4 = Label(window, text="  Source folder", font=(fam, n, 'bold'))
lbl4.grid(column=1, row=1, pady=(0,15), sticky=W)

#(2,1) source folder text box
txt1 = Entry(window, width=textw, textvariable=stringvar1, font=(fam, n))
txt1.grid(column=2, row=1, pady=(0,15), sticky=E)

#(3,1) source folder button
btn = Button(window, image=pathimgy, bg="black", command=pathbtn)
btn.grid(column=3, row=1, pady=(0,15), padx=(5,0), sticky=W)

#(0,2) name checkbox
lbl5 = Label(window, image=emptyimgy, font=(fam, n, 'bold'))
lbl5.grid(column=0, row=2, padx=(10, 0), pady=(0,15), sticky=E)

#(1,2) name prompt text
lbl6 = Label(window, text="  Name", font=(fam, n, 'bold'))
lbl6.grid(column=1, row=2, pady=(0,15), sticky=W)

#(2,2) name text box
txt2 = Entry(window,width=textw, textvariable=stringvar2, font=(fam, n))
txt2.grid(column=2, row=2, pady=(0,15), sticky=E)

#(3,2) .gif prompt text
lbl7 = Label(window, text=".GIF", font=(fam, n, 'bold'))
lbl7.grid(column=3, row=2, pady=(0,15), padx=(0,0), sticky=W)

#(0,3) destination folder checkbox
lbl8 = Label(window, image=emptyimgy, font=(fam, n, 'bold'))
lbl8.grid(column=0, row=3, padx=(10, 0), pady=(0,30), sticky=E)

#(1,3) destination folder prompt text
lbl9 = Label(window, text="  Destination folder", font=(fam, n, 'bold'))
lbl9.grid(column=1, row=3, pady=(0,30), sticky=W)

#(2,3) destination folder text box
txt3 = Entry(window,width=textw, textvariable=stringvar3, font=(fam, n))
txt3.grid(column=2, row=3, pady=(0,30), sticky=E)

#(3,3) destination folder button
btn1 = Button(window, image=pathimgy, command=destbtn)
btn1.grid(column=3, row=3, pady=(0,30), padx=(5,0), sticky=W)

#new button module for last three buttons
from tkmacosx import Button

#(1,4) clear button
btn1 = Button(window, text="Clear", disabledbackground='gray', disabledforeground='white', bg="black", fg="white", borderless=1, command=clearbtn, font=(fam, n, 'bold'))
btn1.grid(column=1, row=4, sticky=W)

#(2,4) make gif button
btn2 = Button(window, text="Make GIF", disabledbackground='gray', disabledforeground='white', bg="black", fg="white", borderless=1, command=gifbtn, font=(fam, n, 'bold'))
btn2.grid(column=2, row=4, sticky=W)
btn2.config(state='disabled')

#(3,4) open button
btn3 = Button(window, text="Open", disabledbackground='gray', disabledforeground='white', bg="black", fg="white", borderless=1, command=openbtn, font=(fam, n, 'bold'))
btn3.grid(column=3, row=4, padx=(0,0), sticky=E)
btn3.config(state='disabled')

window.mainloop()
