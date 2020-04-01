from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox

# Root Element
win = Tk();
win.config(background = '#114D96')

a = b = c = d = 0
global total_items

# Cart

def cart():
    total_items = a + b + c + d
    cartlabel = Label(win , text = "Total items in the cart\n"+str(total_items))
    cartlabel.config(font = ('arial' , 16) , bg = "#114D96" , fg = "ghostwhite")
    cartlabel.place(x = 1100 , y = 35)
cart()


# Button command function

def Camera():
    global a
    a += 1
    messagebox.showinfo("Confirmation" , "Item added to cart");
    cart()

def Moisturizer():
    global b
    b += 1
    messagebox.showinfo("Confirmation" , "Item added to cart");
    cart()

def Watch():
    global c
    c += 1
    messagebox.showinfo("Confirmation" , "Item added to cart");
    cart()

def Guitar():
    global d
    d += 1
    messagebox.showinfo("Confirmation" , "Item added to cart");
    cart()

# ------------------------------- BILLING FUNCTIONS -----------------------------------

def calculate():
    global win2
    win2 = Tk()
    win2.config(bg = '#DEB887')
    bill()
    win2.geometry("1366x768")
    win2.mainloop()

def bill():
    global price
    price = [34999 , 675 , 1750 , 8999]
    item_name = ['Camera','Moisturizer','Watch','Guitar']
    global l1
    l1 = Label(win2 , text = "Item Name" , font = ("arial" , 24) , fg = '#000080' , bg = '#DEB887')
    l2 = Label(win2, text="Unit", font=("arial", 24) , fg = '#000080' , bg = '#DEB887')
    l3 = Label(win2, text="Price", font=("arial", 24) , fg = '#000080' , bg = '#DEB887')
    l4 = Label(win2, text="Amount", font=("arial", 24) , fg = '#000080' , bg = '#DEB887')

    if(a>0):
        total = a * price[0]
        l5 = Label(win2 , bg = '#DEB887', text = ""+item_name[0]+"                    "+""+str(a)+"            x        "+str(price[0])+"           =        "+""+str(total), font = ('arial',18))
        l5.place(x= 375 , y = 150)

    if (b > 0):
        total1 = b * price[1]
        l6 = Label(win2, bg = '#DEB887', text="" + item_name[1] + "                " + "" + str(b) + "            x        " + str(price[1]) + "               =         " + "" + str(total1), font=('arial', 18))
        l6.place(x=375, y=180)

    if (c > 0):
        total2 = c * price[2]
        l7 = Label(win2, bg = '#DEB887', text="" + item_name[2] + "                       " + "" + str(c) + "           x        " + str(price[2]) + "              =      " + "" + str(total2), font=('arial', 18))
        l7.place(x=375, y=210)

    if (d > 0):
        total3 = d * price[3]
        l8 = Label(win2, bg = '#DEB887', text="" + item_name[3] + "                       " + "" + str(d) + "           x        " + str(price[3]) + "              =      " + "" + str(total3), font=('arial', 18))
        l8.place(x=375, y=240)

    if(a>0 or b>0 or c>0 or d>0):
        total_price = (a * 34999) + (b * 675) + (c * 1750) + (d * 8999)
        l9 = Label(win2 , bg = '#DEB887', text = "YOUR TOTAL AMOUNT IS "+str(total_price)+" Rs" , font = ('arial' , 26))
        l10 = Label(win2 , bg = '#DEB887', text = "THANKS FOR SHOPPING WITH US !" , font = ('arial' , 28))
        l9.place(x=375, y=300)
        l10.place(x=360, y=400)
    else:
        l11 = Label(win2 , bg = '#DEB887', text = "PLEASE ADD ITEMS TO YOUR CART !" , fg = 'red', font = ("arial" , 28))
        l11.place(x= 380 , y= 350)

    l1.place(x= 340 , y = 70)
    l2.place(x= 580 , y = 70)
    l3.place(x = 760 , y = 70)
    l4.place(x= 960 , y = 70)

# Heading text

hlabel = Label(win,text = "Shopping Cart", fg = 'white' ,bg = '#114D96', pady = 15)
hlabel.config(font=('Comic Sans MS',45))
hlabel.pack(side = 'top')


# Creating frames
f1 = Frame(win, width = 1050, height = 570, bg = 'white').pack()

# Addding elements to frame

# Item 1
# image
img1 = ImageTk.PhotoImage(Image.open('images/dslr.png'))
f1label1 = Label(f1,image = img1)
f1label1.config(width = 220, height = 150)
f1label1.place(x = 270, y = 140)

# Label
f1label2 = Label(win, text = "₹34,999", font=('arial',18))
f1label2.place(x = 270, y = 300)

# Button
f1button1 = Button(text = 'ADD TO CART' ,bg = '#FFC300', fg = 'black', width = 24, height = 2, command = Camera)
f1button1.place(x = 270, y = 335)

# Item 2
# image
img2 = ImageTk.PhotoImage(Image.open('images/maui.png'))
f1label3 = Label(f1,image = img2)
f1label3.config(width = 220, height = 150)
f1label3.place(x = 600, y = 140)

# Label
f1label4 = Label(win, text = "₹675", font=('arial',18))
f1label4.place(x = 600, y = 300)

# Button
f1button2 = Button(text = 'ADD TO CART' ,bg = '#FFC300', fg = 'black', width = 24, height = 2, command = Moisturizer)
f1button2.place(x = 600, y = 335)

# Item 3
# image
img3 = ImageTk.PhotoImage(Image.open('images/watch.png'))
f1label5 = Label(f1,image = img3)
f1label5.config(width = 220, height = 150)
f1label5.place(x = 930, y = 140)

# Label
f1label6 = Label(win, text = "₹1,750", font=('arial',18))
f1label6.place(x = 930, y = 300)

# Button
f1button3 = Button(text = 'ADD TO CART' ,bg = '#FFC300', fg = 'black', width = 24, height = 2, command = Watch)
f1button3.place(x = 930, y = 335)

# Item 4
# image
img4 = ImageTk.PhotoImage(Image.open('images/guitar.png'))
f1label7 = Label(f1,image = img4)
f1label7.config(width = 500, height = 150)
f1label7.place(x = 410, y = 420)

# Label
f1label8 = Label(win, text = "₹8,999", font=('arial',18))
f1label8.place(x = 410, y = 580)

# Button
f1button4 = Button(text = 'ADD TO CART' ,bg = '#FFC300', fg = 'black', width = 24, height = 2, command = Guitar)
f1button4.place(x = 410, y = 615)


# Bill button
billbutton = Button(text = "Generate Bill" , command = calculate)
billbutton.place(x = 965 , y = 500)
billbutton.config(bg = 'red' , fg = "white" , width = 16 , height = 2 , font = ('Arial' , 16))

win.mainloop();