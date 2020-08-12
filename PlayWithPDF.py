from tkinter import *
from tkinter import ttk
from PIL import Image
from tkinter.filedialog import askopenfile

root = Tk()
root.geometry("680x460")
root.resizable(width=False,height=False)
root.configure(bg="lavender")

fr = Frame(root)
fr.pack(side=LEFT)

img = []
count = 1
imagestack = []
imgname = []

sbr = Scrollbar(fr,bg="red")
sbr.pack(side=RIGHT,fill="y")

lbx = Listbox(fr,font=("Verdona",14),bg="lavender blush",fg="black")
lbx.pack(side=LEFT,fill="x",expand=True)

def makepdf(x):
    for i in img:
        image = Image.open(i)
        im = image.convert('RGB')
        imagestack.append(im)
    print(imagestack)
    if x ==1:
        im.save(r'combine.pdf',save_all=True,append_images=imagestack)
    else:
        for i in range(len(imagestack)):
            imagestack[i].save(str(i)+".pdf")
    done = Label(text="Done",bg="lavender",fg="Green")
    done.place(x=180,y=385)

def open_file():
    global count
    file = askopenfile(mode='r',filetypes=[('png/jpg/jpeg files','*.*')])
    file = str(file)
    loc = file.split()[1].split('=')[1]
    loc = loc[1:-1]
    if loc.split('/')[-1] != 0:  # placing image name in left side of UI.
        lbx.insert(count,str(loc.split('/')[-1]))
    else:
        lbx.insert(count,str(loc.split('\\'[-1])))
    count +=1
    if "png" in  loc or "jpeg" in loc or "jpg" in loc or "PNG" in loc or "JPG" in loc or "JPEG" in loc:
        img.append(loc)
    else:
        print("Forget it")

sbr.config(command=lbx.yview)

labtop = Label(root,text="PlayWithPDF",font=("Verdana",16),padx=300,pady=5,bg="orange",fg="black")
labtop.place(x=0,y=0)

btn = Button(root,text='Browse',font=("Verdana",14),command= lambda:open_file())
btn.place(x=35,y=60)

var1 = IntVar()
checkbut1 = Checkbutton(root,font=("Verdana",14),text="One PDF for multiple Selected images",bg="lavender",fg="black",variable=var1)
checkbut1.place(x=250,y=68)

#lavbott = Label(root,text="Test",font=("Verdana",10),bg="white",fg="blue")
#lavbott.place(x=40,y=130)

labright = Label(root,text="Instructions\n 1.Selected Images are shown in Left Box.\n 2.By Default it will generate 1 PDF for each\n images. \n 3.Fill the check box to generate one PDF for\n all images.\n. Thanks for using.",font=(12),bg="lavender",fg="black")
labright.place(x=260,y=130)


btn2 = Button(root,text="Convert",font=(12),bg="orange",fg="black",command= lambda:makepdf(var1.get()))
btn2.place(x=35,y=380)
mainloop()


