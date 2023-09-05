from tkinter import *
win=Tk()
win.title("queue")
front=-1
rear=-1
size=0
win.geometry("1200x1000")
w1=PanedWindow(win,height=10).pack(side=TOP,fill=BOTH,expand=1)
w2=PanedWindow(win,height=10).pack(side=TOP,fill=BOTH,expand=1)
Label(w2,text = "QUEUES",height=3,bg="white",font=("Bookman Old Style", 20, "bold")).pack(fill=BOTH)
w3=PanedWindow(win,height=5).pack(side=TOP,fill=BOTH,expand=1)
w4=PanedWindow(win,height=10)
Label(w4,text="           Enter here ->    ", font=("Bookman Old Style", 16)).pack(side=LEFT,anchor = "nw")
entry = Entry(w4,font=("Bookman Old Style", 14),width= 25)
entry.pack(side=LEFT,anchor = "nw")
Label(w4,text="           ").pack(side=LEFT,anchor = "nw")

# Define a function to return the Input data
def get_data():
    global size
    global entry
    n= int(entry.get())
    entry.delete(0, END)
    size = n
    global button
    button=['','','','','','','','','','','','','','','']
    for i in range(n):
       button[i]=Button(w7,text="",fg="black", font=("Bookman Old Style", 20),height=4,width=4)
       button[i].pack(side=LEFT,padx=15,pady=15,fill=BOTH,expand=1)
       l=Label(w8,font=("Bookman Old Style", 10),text=i).pack(side=LEFT,padx=15,pady=15,fill=BOTH,expand=1)
    w7.pack(side=TOP,fill=BOTH,expand=1)
    w8.pack(side=TOP,fill=BOTH,expand=1)

#enueue function
def enqueue():
    n= int(entry.get())
    global entrymsg
    global front
    global rear
    global button
    global size
    global b1
    global b2
    entry.delete(0, END)
    if rear==size-1:
        entrymsg.configure(state='normal')
        entrymsg.delete(0, END)
        entrymsg.insert(0, " Queue is full..!")
        entrymsg.configure(state='readonly')
    else:
        if front==-1:
            front=0
        rear+=1
        button[rear].config(text=n)
        val = button[rear].config()["text"][4]
        val = str(val)+" is added"
        entrymsg.configure(state='normal')
        entrymsg.delete(0, END)
        entrymsg.insert(0, val)
        entrymsg.configure(state='readonly')
        b1.config(text=str(front))
        b2.config(text=str(rear))

#dequeue function
def dequeue():
    global entrymsg
    global front
    global rear
    global button
    global size
    if front == -1:
        entrymsg.configure(state='normal')
        entrymsg.delete(0, END)
        entrymsg.insert(0, " Queue is empty..!")
        entrymsg.configure(state='readonly')
    else:
        if front == rear:
            front = -1
        val = button[0].config()["text"][4]
        for i in range(rear):
            button[i].config(text=button[i+1].config()["text"][4])
        button[rear].config(text="")
        val = str(val)+" is removed"
        entrymsg.configure(state='normal')
        entrymsg.delete(0, END)
        entrymsg.insert(0, val)
        entrymsg.configure(state='readonly')
        rear=rear-1
        b1.config(text=str(front))
        b2.config(text=str(rear))

#clear queue function
def clearqueue():
    global rear
    global button
    global entrymsg
    for i in range(rear+1):
        button[i].config(text="")
    entrymsg.configure(state='normal')
    entrymsg.delete(0, END)
    entrymsg.insert(0, "queue cleared")
    entrymsg.configure(state='readonly')
    

Button(w4, text= "Click to Create",command=get_data).pack(side=LEFT,anchor = "nw")
Label(w4,text="                 Front    ", font=("Bookman Old Style", 16)).pack(side=LEFT,anchor = "nw")
b1 = Button(w4,text=str(front),width=5,height=1,font=("Bookman Old Style", 16))
b1.pack(side=LEFT,anchor = "nw")
Label(w4,text="         Rear     ", font=("Bookman Old Style", 16)).pack(side=LEFT,anchor = "nw")
b2 = Button(w4,text=str(rear),width=5,height=1,font=("Bookman Old Style", 16))
b2.pack(side=LEFT,anchor = "nw")
w4.pack(side=TOP,fill=BOTH,expand=1)

w5 = PanedWindow(win,height=10)
lab_msg = Label(w5, text="                   Message    ", font=("Bookman Old Style", 16)).pack(side=LEFT,anchor = "nw")
entrymsg = Entry(w5,font=("Bookman Old Style", 14),width= 60)
entrymsg.pack(side=LEFT)
w5.pack(side=TOP,fill=BOTH,expand=1)

w6 = PanedWindow(win,height=10)
button1 = Button(w6, text ="enqueue", font=("Bookman Old Style", 16),activebackground="green",activeforeground="white",fg ="green",command=enqueue) 
button1.pack(side=LEFT,padx=40,pady=15,fill=BOTH,expand=1)

button2 = Button(w6, text ="dequeue",font=("Bookman Old Style", 16), activebackground="red",activeforeground="white",fg ="red",command=dequeue) 
button2.pack(side=LEFT,padx=40,pady=15,fill=BOTH,expand=1)

button3 = Button(w6, text ="clear queue",font=("Bookman Old Style", 16),activebackground="blue",activeforeground="white", fg ="blue",command=clearqueue) 
button3.pack(side=LEFT,padx=40,pady=15,fill=BOTH,expand=1)
w6.pack(side=TOP,fill=BOTH,expand=1)

w7=PanedWindow(win,height=10)
w8=PanedWindow(win,height=10)
w9=PanedWindow(win,height=10)
Label(w9,text="",height=10,bg="black")
w9.pack(side=TOP,fill=BOTH,expand=1)
win.mainloop()
