from tkinter import *
from PIL import Image,ImageTk

top = Tk()
top.geometry("700x350")
top.title("Automatic Weighing Machine")

textBox = Text(top,height=2,width=50,highlightbackground="red",highlightthickness=2).place(x=20,y=20)
b0=Button(top,bg="red",width=20,height=2,text="SEARCH",fg="white",activeforeground="red").place(x=450,y=20)

f1=Frame(top,bg="red",width=410,height=250).place(x=20,y=80)
#image1
p1=Image.open("C:/Desktop Wallpapers/2517915.jpg")
p1=p1.resize((130,130),Image.ANTIALIAS)
photoimg=ImageTk.PhotoImage(p1)
lbl_img=Label(image=photoimg)
lbl_img.place(x=30,y=90,width=110,height=70)
box1=Text(f1,height=2,width=25).place(x=150,y=110)
b2=Button(f1,height=2,width=5,text="+").place(x=370,y=110)
#image2
p2=Image.open("C:/Desktop Wallpapers/2517915.jpg")
p2=p2.resize((130,130),Image.ANTIALIAS)
photoimg2=ImageTk.PhotoImage(p2)
lbl_img2=Label(image=photoimg2)
lbl_img2.place(x=30,y=170,width=110,height=70)
#image3
p3=Image.open("C:/Desktop Wallpapers/2517915.jpg")
p3=p3.resize((130,130),Image.ANTIALIAS)
photoimg3=ImageTk.PhotoImage(p3)
lbl_img3=Label(image=photoimg3)
lbl_img3.place(x=30,y=250,width=110,height=70)

box1=Text(f1,height=2,width=25).place(x=150,y=110)
b2=Button(f1,height=2,width=5,text="+").place(x=370,y=110)
box1=Text(f1,height=2,width=25).place(x=150,y=110)
b2=Button(f1,height=2,width=5,text="+").place(x=370,y=110)
box1=Text(f1,height=2,width=25).place(x=150,y=190)
b3=Button(f1,height=2,width=5,text="+").place(x=370,y=190)

box1=Text(f1,height=2,width=25).place(x=150,y=270)
b3=Button(f1,height=2,width=5,text="+").place(x=370,y=270)

top.mainloop()
