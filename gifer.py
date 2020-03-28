import imageio
import pathlib
from datetime import datetime
import natsort
import glob
from tkinter import *
import tkinter as tk
from tkinter.filedialog import askdirectory


def make_gif(image_directory: pathlib.Path, frames_per_second: float, reversin: bool, namin: str, **kwargs):

    assert isinstance(image_directory, pathlib.Path), "input must be a pathlib object"
    image_type = kwargs.get('type', 'png')

    #names the resulting gif
    gif_dir = image_directory.joinpath(namin + ".gif")

    print('Started making GIF')
    print('Please wait...\n\n\n')

    imglist = image_directory.glob('*.' + image_type)
    imglist = natsort.natsorted(imglist,reverse=reversin)

    images = []
    for file_name in imglist:
        images.append(imageio.imread(image_directory.joinpath(file_name)))
    imageio.mimsave(gif_dir.as_posix(), images, fps=frames_per_second)

    print('Finished making GIF!')
    print('GIF can be found at: ' + gif_dir.as_posix())

def main(lePath, leFps, leReverse, leName):
    namin = leName
    reversin = leReverse
    fps = leFps
    png_dir = pathlib.Path(lePath)
    make_gif(png_dir, fps, reversin, namin)


window = Tk()
window.title("GIFER")
window.geometry('600x250')
window.resizable(width=False, height=False)

v = tk.IntVar()

lbl = Label(window, text="Choose source folder")
lbl.grid(column=0, row=0)

def clickedpath():
    foldername = askdirectory(title='Select Folder')

    lbl1 = Label(window, text= "Selected path:")
    lbl1.grid(column=0, row=1)

    lbl2 = Label(window, text=foldername)
    lbl2.grid(column=1, row=1)

    lbl3 = Label(window, text= "FPS:")
    lbl3.grid(column=0, row=2)

    txt = Entry(window,width=10)
    txt.grid(column=1, row=2)

    #asks for name
    lbl3 = Label(window, text= "Name:")
    lbl3.grid(column=0, row=3)

    txt1 = Entry(window,width=30)
    txt1.grid(column=1, row=3)

    lbl3 = Label(window, text= ".gif")
    lbl3.grid(column=2, row=3)

    #asks for reversal
    lbl4 = Label(window, text="Reverse image order?")
    lbl4.grid(column=0, row=4)

    btn = Radiobutton(window, text="yes", variable=v, value=True)
    btn.grid(column=0, row=5)

    btn1 = Radiobutton(window, text="no", variable=v, value=False)
    btn1.grid(column=0, row=6)

    def clicked():
        pathy = foldername
        fpsy = txt.get()
        namy = txt1.get()
        reversy = v.get()
        lbl5 = Label(window, text= main(pathy, fpsy, reversy, namy))
        lbl5.grid(column=0, row=8)
        lbl6 = Label(window, text= "All done!")
        lbl6.grid(column=0, row=9)

    btn2 = Button(window, text="Make GIF", command=clicked)
    btn2.grid(column=0, row=7)

btn3 = Button(window, text="...", command=clickedpath)
btn3.grid(column=1, row=0)

window.mainloop()
