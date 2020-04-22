import os
import glob
import base64
import imageio
import pathlib
import natsort
import webbrowser
import tkinter as tk
from tkinter import *
from PIL import Image
from io import BytesIO
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

def tagbtn():
    webbrowser.open("http://sahasramesh.com")
#styling
fam = 'rubik'
n = 20
textw = 17

#images
Image.open(BytesIO(base64.b64decode("""iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7
MK6iAAAA2UlEQVRIS+2XTQ6CMBCFH0s4gS7adY8CSQ/kz1r0PizgKqy70COwq+mERkSiacxUEtvV8JL
267zMlEyGxzoBOEy+OcKzZ2Tj6VcAGw7Swpk3AFsHrgHsI0E9pnZgGxlKuASO5nqyOlnN5sA6i6ssS7
RtS1l3XYeqqigO1Zdse5uxtc+vqZQSxhiE6l+DlVLo+/4F/EkPBjdNA6017RuGAXmeUxyqB4PdBiEEi
qKgTKcrVJ/D11nVbE2c/sec1qbi+s92ijG6zGvr8tMRxt/GDVQ75pZy49LRMe4kF3QT8XQY4gAAAABJ
RU5ErkJggg==""")
)).save('path.png', 'PNG')

Image.open(BytesIO(base64.b64decode("""iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7
MK6iAAAB6ElEQVRIS82WPU8CQRCGH046EqCmQXsaNWKjBYbaivg3jBYWWmthofFnCJVakmihjRK1olY
ragIdHpi5ZMlx3u7tHUfCdpedfZ+Z2Y97M9iPMnAJHGiW3AOHwLeNZMYi6Ao4sojzh1wAZ6Y1JvA68A
7YJBfGcIEt4DNsUif6CNRiVqkLfwO2g5Nh4GdgJyWoknkBdv2aQfArUE0ZquSegD314QfLnn4sCKpkN
9Se+8G/wMqCwRPAEYYCnwOnC4Yq+WvgWIElk1RGvV6n3W5TKpXo9Xo6zYyAV4GvNKiNRoNWqzWVMsBX
BXwH7M8LVpUqncFgQKFQYDIJbWZTwHO3OQjt9/sUi0VjLZHg4XBIrVaj0+mECgXbK5Xm8/nIBhrBAs3
lcp5ItVr9B4/Z3plkrMGyqlKp0O12PYEk7Q0+mcY99letKi+XyzOn17a9scASrDmZnk7E6dXutbT61u
AqpguDlcuEzenVkB8ELJbGyq6MRiOy2ey0UpvTqwGvxXoyHcfBdd3E7fUl4T2ZMqx9lcDH43HkPTUEe
H7M/1sUtaT+yjYR8WHeXi2FEZBE0jR5wS7MmL6lMXsqyzRN34zJU4AoQy+/pKQ+TJ7izbiG3r8/SfyY
56tMRz3O9RGLdGNwK03gBPixuVt/2uyhs6iaDrkAAAAASUVORK5CYII=""")
)).save('filled.png', 'PNG')

Image.open(BytesIO(base64.b64decode("""iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7
MK6iAAACTElEQVRIS+2XMa/SUBTH/7XwKSD4+AIQnlEXHXSHhMWRhMBudHAQSP8N4OCgcYeQsPkWIuw
6PBd9EQNfACXwKUqtadPbtPeVUix5Lq8Tvefc87899557fiiI+bRarbvpdPotgGd7pkwBPCf5K05I5Z
ATyXcAXhzyk+xvSLai5uwV7nQ6JVVVfwA4uLgwAUVRzN1ud7/b7f4MtYcNkvwM4InfpqoqCoUCKpVK6
IdMp1Msl0uYpinbv5N8KA9e+xqSlwAe+R2bzSYymUysbG82GwyHQ9n3K8nH/sGAMMlvAB4Ih3w+j1qt
FktQdhqNRliv1/7hLySfigFP2N3TuTDYaa1Wq/8kKiZNJhMn/eIxTfNc7LknrOv6zrIs1XbK5XKo1+u
JRMXk8XiM1WolXi2Sd+wXR5hkH8BrYdU07SSiIoiu6/5470m+FMKWsDQaDWSz2ZMKb7dbDAYDLyZJRS
F5BsDJhV0y7Xb7pKIiWK/X80rNMIwzW/gTAKc4S6XS3jpNuprZbIb53Du7F7awl+ZT7628WP9e3won3
crI+bep/iio4gbLaaa4SOPgyk1dIADy167MY3pv3JMo92jnynSbRICrTn2RSE3C4TGvLZL8I7pVEgCI
AgKbwzRNS3lt0f7x30DATXkA8pIAgQQAdvgA9MWCvWN6tNx73dRHw57YHxn6RKkVi0WUy+XQw2y3vcV
iEYa3AcgTkyOBPpVKXQkOi1s6Pj/LNM17RwG9X0TmsZgLcLgqyjf23xMXkT4IWgkJemEYxqt+v/87zu
L+AkCKFrMb5tNUAAAAAElFTkSuQmCC""")
)).save('empty.png', 'PNG')

Image.open(BytesIO(base64.b64decode("""iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7
MK6iAAABsklEQVRIS+2XO07DQBBAX7DvgX2EgDANlhIOQEkZRcoBEBQUUENBAeIAkZKSdEBPIpEGIiA
3sDlHwkdjsZJjOWY2MYKCrRJ5Zt56du19rqAfq8AZsDsn5QbYA2JNyYoi6BzYV8SlQ06B46KcInAVeA
I0k8tjvAEbwEvexXlF74C65V3OC38ENrMX88D3wFZJUFNmCITpmlnwAxCUDDXl+sC2+ZMGy5o+/xDUl
F0za54GTwFHC55OpziOQxiGDIfSSdX4AFYk0oBPgCNVKtBoNOh2u0n4eDymWpVmqccFcGDAMhOrMZlM
cF2XIAgYjUZWuXLDAvaAyDZzyXhPwNfAjk0h3/dptVpJShRFtNttm3SJ7QnYus21Wo1+X54OGAwG1Ov
275p/sGqt/lu96Oa6KrCK3NaX0Opb2dWiNCpdMbMoAewv9MosAZy8MmVYedWS4MTH0sfiu9avPM+j2W
wmM47jmE6no3oMAfEwN30syu9fEwGBlyl52S7MSN+fkT0zyzKlb0byDOA7oRe1UHtYprdy3K7bCn26h
pWPfSUmXlW01W0+T0SRLgtspQccAq+aZ+sT1nOPs54tNbMAAAAASUVORK5CYII=""")
)).save('info.png', 'PNG')

Image.open(BytesIO(base64.b64decode("""iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7
MK6iAAABwUlEQVRIS+1XPYvCQBB9EUH8xEL0DiFY6A/wj1iIhaWdhYWW3p0QEPSuERTsrKwt7PwdNtY
2yp1i5UckCHrMchs10RAumOMg0yTLzr4382aSZQScrQHg9WL9iNd3ziH8oH8CeHoE0w3MLwDPRNwE8G
ITKadpEvHJZlJG5xDbproj9f+W2u/3I5VKYTKZ4HA43ExGV+NyuYx2u61zTqfTGI/HOJ30n70kSajX6
+zMbreDz+dTz282G4RCIR3eXWJB4H/T6zNEXCgU0O/32cZ0OkUikQD5d7tdlEolxGIxLJdLRKNRLBYL
DIdDZLPZKyDLxLlcDoPBAPF4HK1WC/l8nmVImRrZXeJGgy6rs9VqNba4zNjlcrGMIpEIy9jr9UKWZeZ
HxKPRiAVyy0zXmEuvrTGti8Uier2eip/JZNDpdFgJyOi9UqlYl5pACExr4XAYiqJgv9+rWzxQbc/8qs
b3iNfrNYLBoNpcvDT0fCixx+PBdruF2+1WMz4ejxBFEfP53Fhqw1Y0uRkIBJBMJjGbzbBarcw1l0lsy
27O7WRZQrMAjtRmlbLsR1LbMbpoA/340xGGR0MDVdWyhsYANC69kcs3fcfLE6kyui0AAAAASUVORK5C
YII=""")
)).save('fps.png', 'PNG')

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

#(1, 5) tag
btn4 = Button(window, text="Sahas Ramesh", fg='#FF4500', anchor=W, highlightbackground='white', highlightcolor='white', highlightthickness=0, command=tagbtn, font=('Courier', 10))
btn4.grid(column=3, row=5, pady=(10,0), sticky=W)

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
btn3.grid(column=3, row=4, padx=(0,0), sticky=W)
btn3.config(state='disabled')

#(1, 5) tag
tag = Label(window, text="An original project by ", font=('Courier', 10))
tag.grid(column=2, row=5, pady=(10,0), sticky=E)

window.mainloop()

#pyinstaller --onefile --windowed --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' --icon=logo.ico gifer.py
