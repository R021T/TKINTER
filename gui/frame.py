arr=["apple","tomato","potato"]
arr2 ={'apple':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/apple.jpg",
       'banana':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/banana.jpg",
       'beetroot':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/beetroot.jpg",
       'bell pepper':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/bell pepper.jpg",
       'cabbage':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/cabbage.jpg",
       'capsicum':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/capsicum.jpg",
       'carrot':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/carrot.jpg",
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
       'lettuce':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/lettuce.jpg",
       'mango':"C:/Users/rcviu/OneDrive/Desktop/mini-main/images1/mango.jpg",
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
top.geometry("700x350")
top.title("Automatic Weighing Machine")

textBox = Text(top,height=2,width=50,highlightbackground="red",highlightthickness=2).place(x=20,y=20)
b0=Button(top,bg="red",width=20,height=2,text="SEARCH",fg="white",activeforeground="red").place(x=450,y=20)

f1=Frame(top,bg="red",width=410,height=250).place(x=20,y=80)

#image1
p1=Image.open(arr2[arr[0]])
p1=p1.resize((130,130),Image.ANTIALIAS)
photoimg=ImageTk.PhotoImage(p1)
lbl_img=Label(image=photoimg)
lbl_img.place(x=30,y=90,width=110,height=70)
box1=Text(f1,height=2,width=25)
box1.insert(INSERT,arr[0])
box1.config(state="disabled")
box1.place(x=150,y=110)
b1=Button(f1,height=2,width=5,text="+").place(x=370,y=110)

#image2
p2=Image.open(arr2[arr[1]])
p2=p2.resize((130,130),Image.ANTIALIAS)
photoimg2=ImageTk.PhotoImage(p2)
lbl_img2=Label(image=photoimg2)
lbl_img2.place(x=30,y=170,width=110,height=70)
box2=Text(f1,height=2,width=25)
box2.insert(INSERT,arr[1])
box2.config(state="disabled")
box2.place(x=150,y=190)
b2=Button(f1,height=2,width=5,text="+").place(x=370,y=190)

#image3
p3=Image.open(arr2[arr[2]])
p3=p3.resize((130,130),Image.ANTIALIAS)
photoimg3=ImageTk.PhotoImage(p3)
lbl_img3=Label(image=photoimg3)
lbl_img3.place(x=30,y=250,width=110,height=70)
box3=Text(f1,height=2,width=25)
box3.insert(INSERT,arr[2])
box3.config(state="disabled")
box3.place(x=150,y=270)
b3=Button(f1,height=2,width=5,text="+").place(x=370,y=270)


top.mainloop()
