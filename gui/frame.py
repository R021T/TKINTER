l=[]
arr=["apple","tomato","potato"]
arr2 ={'apple':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/apple.jpg",
       'banana':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/banana.jpg",
       'beetroot':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/beetroot.jpg",
       'bell pepper':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/bell pepper.jpg",
       'cabbage':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/cabbage.jpg",
       'capsicum':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/capsicum.jpg",
       'carrot':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/carrot.png",
       'cauliflower':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/cauliflower.jpg",
       'chilli pepper':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/chilli.jpg",
       'corn':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/corn.jpg",
       'cucumber':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/cucumber.jpg",
       'eggplant':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/eggplant.jpg",
       'garlic':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/garlic.jpg",
       'ginger':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/ginger.jpg",
       'grapes':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/grapes.jpg",
       'jalepeno':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/jalapeno.jpg",
       'kiwi':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/kiwi.jpg",
       'lemon':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/lemon.jpg",
       'lettuce':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/lettuce.jpeg",
       'mango':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/mango.png",
       'onion':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/onion.jpg",
       'orange':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/orange.jpg",
       'paprika':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/paprika.jpg",
       'pear':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/pear.jpg",
       'peas':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/peas.jpg",
       'pineapple':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/pineapple.jpg",
       'pomegranate':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/pomegranate.jpg",
       'potato':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/potato.jpg",
       'raddish':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/raddish.jpg",
       'soy beans':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/soy beans.jpg",
       'spinach':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/spinach.jpg",
       'sweetcorn':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/sweet corn.jpg",
       'sweetpotato':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/sweet potato.jpg",
       'tomato':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/tomato.jpg",
       'turnip':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/turnip.jpg",
       'watermelon':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/watermelon.jpg"}

from tkinter import *
from PIL import Image,ImageTk

top = Tk()
top.geometry("970x350")
top.title("Automatic Weighing Machine")

name=StringVar()
n1=StringVar()
n2=StringVar()
n3=StringVar()
n4=StringVar()

def search():
       f2=Frame(top,bg="green",width=230,height=250).place(x=450,y=80)

       #image4
       p4=Image.open(arr2[name.get()])
       p4=p4.resize((70,70),Image.ANTIALIAS)
       global photoimg4
       photoimg4=ImageTk.PhotoImage(p4)
       lbl_img4=Label(image=photoimg4,background="white")
       lbl_img4.place(x=510,y=90,width=110,height=70)
       box4=Entry(f2,textvariable=n4,font=('Arial 20'),width=13)
       box4.insert(INSERT,name.get())
       box4.config(state="disabled")
       box4.place(x=463,y=190)
       b4=Button(f2,height=2,width=5,text="+",command=add4).place(x=543,y=270)

label=Label(top,text="LIST",font=('Arial',20)).place(x=790,y=20)
box5=Listbox(top,width=40,height=15,highlightbackground="red",highlightthickness=2)
box5.place(x=700,y=80)

def add1():
       l.append(n1.get())
       print("List: ",l)
       global i
       for i in l:
              box5.insert(END,i)

def add2():
       l.append(n2.get())
       print("List: ",l)
       global i
       for i in l:
              box5.insert(END,i)

def add3():
       l.append(n3.get())
       print("List: ",l)
       global i
       for i in l:
              box5.insert(END,i)

def add4():
       l.append(n4.get())
       print("List: ",l)
       global i
       for i in l:
              box5.insert(END,i)

textBox = Entry(top,textvariable=name,font=('Arial 20'),width=27,highlightbackground="green",highlightthickness=2).place(x=20,y=20)
b0=Button(top,bg="red",width=20,height=2,text="SEARCH",fg="white",activeforeground="red",command=search).place(x=450,y=20)

b4=Button(top,width=6,height=2,bg="green",text="CAM",fg="white",activeforeground="green").place(x=625,y=20)

f1=Frame(top,bg="red",width=410,height=250).place(x=20,y=80)

#image1
p1=Image.open(arr2[arr[0]])
p1=p1.resize((70,70),Image.ANTIALIAS)
photoimg1=ImageTk.PhotoImage(p1)
lbl_img1=Label(image=photoimg1,background="white")
lbl_img1.place(x=30,y=90,width=110,height=70)
box1=Entry(f1,textvariable=n1,font=('Arial 20'),width=13)
box1.insert(INSERT,arr[0])
box1.config(state="disabled")
box1.place(x=150,y=110)
b1=Button(f1,height=2,width=5,text="+",command=add1).place(x=370,y=110)

#image2
p2=Image.open(arr2[arr[1]])
p2=p2.resize((70,70),Image.ANTIALIAS)
photoimg2=ImageTk.PhotoImage(p2)
lbl_img2=Label(image=photoimg2,background="white")
lbl_img2.place(x=30,y=170,width=110,height=70)
box2=Entry(f1,textvariable=n2,font=('Arial 20'),width=13)
box2.insert(INSERT,arr[1])
box2.config(state="disabled")
box2.place(x=150,y=190)
b2=Button(f1,height=2,width=5,text="+",command=add2).place(x=370,y=190)

#image3
p3=Image.open(arr2[arr[2]])
p3=p3.resize((70,70),Image.ANTIALIAS)
photoimg3=ImageTk.PhotoImage(p3)
lbl_img3=Label(image=photoimg3,background="white")
lbl_img3.place(x=30,y=250,width=110,height=70)
box3=Entry(f1,textvariable=n3,font=('Arial 20'),width=13)
box3.insert(INSERT,arr[2])
box3.config(state="disabled")
box3.place(x=150,y=270)
b3=Button(f1,height=2,width=5,text="+",command=add3).place(x=370,y=270)

top.mainloop()
