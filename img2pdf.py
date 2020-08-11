from tkinter import *
from tkinter import ttk
from PIL import Image
from tkinter.filedialog import askopenfile

root = Tk()
root.geometry("680x460")
root.resizable(width=False,height=False)
root.configure(bg="lavender")
img = []                # adding image full location
count = 0
imagestack = []        # collecting pill images.End product
imgname = []           # not using right now. but this is for collecting img names.
def makepdf(x):         # this function creates pdf
    print(x)
    for i in img:
        image = Image.open(i)
        im = image.convert('RGB')
        imagestack.append(im)
    if x ==1:                                               # for 1 pdf of multiple selected images
        im.save(r'combine.pdf',save_all=True,append_images=imagestack)
    else:                                                  # for 1 pdf for each selected images.
        for i in imagestack:
            i.save(r'1.pdf')

def open_file():                  # get file locations
    global count
    file = askopenfile(mode='r',filetypes=[('png/jpg/jpeg files','*.*')])
    file = str(file)
    loc = file.split()[1].split('=')[1]
    loc = loc[1:-1]
    if loc.split('/')[-1] != 0:  # placing image name in left side of UI.
        labbott = Label(text=str(loc.split('/')[-1]),bg="white",fg="Blue")# for linux
        labbott.place(x=40,y=120+20*count)
    else:
        labbott= Label(text=str(loc.split('\\')[-1]),bg="white",fg="Blue")  # for windows 
        labbott.place(x=40,y=120+20*20) 
    count +=1
    if "png" in  loc or "jpeg" in loc or "jpg" in loc or "PNG" in loc or "JPG" in loc or "JPEG" in loc:
        img.append(loc)
    else:
        print("Forget it")

labtop = Label(root,text="COOL-TOOL",font=("Verdana",16),padx=300,pady=5,bg="orange",fg="black")
labtop.place(x=0,y=0)

btn = Button(root,text='Browse',font=("Verdana",14),command= lambda:open_file())
btn.place(x=35,y=60)

var1 = IntVar()
checkbut1 = Checkbutton(root,font=("Verdana",14),text="One PDF for multiple Selected images",bg="lavender",fg="black",variable=var1)
checkbut1.place(x=250,y=68)



labright = Label(root,text="Instructions\n 1.Selected Images are shown in Left Box.\n 2.By Default it will generate 1 PDF for each\n images. \n 3.Fill the check box to generate one PDF for\n all images.\n. Thanks for using.",font=(12),bg="lavender",fg="black")
labright.place(x=250,y=130)


btn2 = Button(root,text="Convert",font=(12),bg="orange",fg="black",command= lambda:makepdf(var1.get()))
btn2.place(x=35,y=380)
mainloop()


