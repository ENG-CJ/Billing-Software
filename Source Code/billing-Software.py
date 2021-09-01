
#  imports
from tkinter import *
from  tkinter import  messagebox
import time
from  tkinter import  ttk
from  tkinter.tix import*
import os
from  datetime import  datetime
from PIL import ImageTk,Image
import math,random
# import mainPanel

# functions


def ex():
    ans = messagebox.askquestion('Confirm', 'Are You Sure To Exit? ')
    if ans == 1:
        main.destroy()

def help():
    messagebox.showerror('Connection','Make Sure Your Internet Connection')
def active(event):
    pasword_box.config(state=NORMAL)
    pasword_box.delete(0,END)

def active2(event):
    email_box.config(state=NORMAL)
    email_box.delete(0,END)

btnState=False
def switchCase():
    global btnState
    if btnState:
        btn.config(image=showPassword)
        pasword_box.config(show='*')
        tooltip.bind_widget(btn, balloonmsg='Show Password')
        btnState=False
    else:
        btn.config(image=hidePassword)
        pasword_box.config(show='')
        tooltip.bind_widget(btn, balloonmsg='Hide Password')
        btnState=True

def login():

    if email_box.get()=='' or pasword_box.get()=='':
        messagebox.showerror('Error Occured','All Fields Are Required')
    elif '@gmail.com' not in email_box.get():
        messagebox.showerror('Error Occured','Plz Enter Valid Email')
    elif email_box.get()!='alqudus3@mail.com' and pasword_box.get()!='1234':
        messagebox.showerror('Error','Incorrect Username Or Password')
    else:
        messagebox.showinfo('ADMIN | Al-Qudus','Login Successfully')
        login_panel.destroy()
        main_panel()

def hover(event):
    billing.config(bg='black',fg='white')
def Leave(event):
    billing.config(bg='white', fg='black')

def gethover(event):
    searchBtn.config(bg='#029',fg='white',cursor='hand2')
def getLeave(event):
    searchBtn.config(bg='#010', fg='white')
def on_hover(event):
    helper.config(bg='#017',fg='white')
def out_hover(event):
    helper.config(bg='white', fg='black')

def ex_hover(event):
    exiting.config(bg='#404',fg='white')
def In_hover(event):
    exiting.config(bg='white', fg='black')


def getBill():
    main.destroy()
    def exite():
        confirm=messagebox.askquestion('Confirm','Are You Sure To exit? ')
        if (confirm):
            screen.destroy()
        else:
            return
    def find_fill():
        getIn=False
        for i in os.listdir('bills/'):
            if i.split('.')[0]==bill_num.get():
                file=open(f'bills/{i}','r')
                reading=file.read()
                txt_area.delete('1.0',END)
                txt_area.insert(END,reading)
                file.close()
                getIn=True
        if getIn==False:
            messagebox.showerror('Error','Bill Not Found')

    def save_bill():

        saving=messagebox.askyesno('Confirm','Do You Want To Save ?')
        if (saving)==1:
            data=txt_area.get('1.0',END)
            customer_file=open('bills/'+str(bill.get())+'.txt','w')
            customer_file.write(data)
            customer_file.close()
            time.sleep(0.8)
            messagebox.showinfo('AL-QUDUS','Bill Saved Successfully')
        else:
            return
    def welcome():
        global bill
        txt_area.delete('1.0',END)
        bill=StringVar()
        bill_random=random.randint(1000,9999)
        bill.set(str(bill_random))
        txt_area.insert(END,'\n\t\tWELCOME TO AL-QUDUS')
        txt_area.insert(END,f'\n Bill Number: {bill.get()}')
        txt_area.insert(END,f'\n Customer name: {csname.get()}')
        txt_area.insert(END,f'\n Mobile : {mobile_num.get()}')
        txt_area.insert(END,'\n===============================================')
        txt_area.insert(END,'\n Products\t\tQTY\t\tPrice')
        txt_area.insert(END, '\n===============================================')

    def area_bill():
        welcome()
        if csname.get()=='' or phone.get()=='':
            messagebox.showerror('ERROR','Please Enter Customer Name And Phone Number')

        elif total_foods_entry.get()=='$0.0' and total_grocery_entry.get()=='$0.0' and total_drinks_entry.get()=='$0.0':
            messagebox.showerror('ERR','No Product Purchased!')
        else:
            if hura.get()!=0:
                txt_area.insert(END,f'\n  Humburger\t\t{ hura.get()}\t\t ${hura.get()*1}')

            if sandw.get()!=0:
                txt_area.insert(END,f'\n  SandWhich\t\t{ sandw.get()}\t\t ${sandw.get()*2}')

            if chic.get()!=0:
                txt_area.insert(END,f'\n  Chicken\t\t{ chic.get()}\t\t ${chic.get()*2}')
            if pizz.get()!=0:
                txt_area.insert(END,f'\n  Pizza\t\t{ pizz.get()}\t\t ${pizz.get()*5}')

            if chip.get()!=0:
                txt_area.insert(END,f'\n  Chips\t\t{ chip.get()}\t\t ${chic.get()*0.5}')

            if stic.get()!=0:
                txt_area.insert(END,f'\n Stick\t\t{ hura.get()}\t\t ${stic.get()*2}')

        #     groery

            if rice.get()!=0:
                txt_area.insert(END,f'\n  Rice\t\t{ rice.get()}\t\t ${rice.get()*7}')
            if oil.get()!=0:
                txt_area.insert(END,f'\n  Food Oil\t\t{ oil.get()}\t\t ${oil.get()*4}')
            if dal.get()!=0:
                txt_area.insert(END,f'\n  Dal\t\t{ dal.get()}\t\t ${dal.get()*1}')

            if wheat.get()!=0:
                txt_area.insert(END,f'\n  Wheat\t\t{ wheat.get()}\t\t ${wheat.get()*3}')
            if sugar.get()!=0:
                txt_area.insert(END,f'\n  Sugar\t\t{ sugar.get()}\t\t ${sugar.get()*9}')

            if brd.get()!=0:
                txt_area.insert(END,f'\n Bread\t\t{ brd.get()}\t\t ${brd.get()*1}')

            # drinks
            if maza.get()!=0:
                txt_area.insert(END,f'\n  Maza\t\t{ maza.get()}\t\t ${maza.get()*1}')
            if milk.get()!=0:
                txt_area.insert(END,f'\n  Milk\t\t{ milk.get()}\t\t ${milk.get()*2}')
            if mango.get()!=0:
                txt_area.insert(END,f'\n  Mango\t\t{ mango.get()}\t\t ${mango.get()*3}')

            if lemon.get()!=0:
                txt_area.insert(END,f'\n  Lemon\t\t{ lemon.get()}\t\t ${lemon.get()*4}')
            if sprite.get()!=0:
                txt_area.insert(END,f'\n  Sprite\t\t{ sprite.get()}\t\t ${sprite.get()*1}')

            if coco.get()!=0:
                txt_area.insert(END,f'\n Coco\t\t{ coco.get()}\t\t ${coco.get()*5}')

            txt_area.insert(END,'\n-----------------------------------------------')
            if food_tax_entry.get()!='$0.0':
                txt_area.insert(END,f'\n Food Tax:\t\t\t{food_tax_entry.get()}')
            if grocery_tax_entry.get()!='$0.0':
                txt_area.insert(END,f'\n Grocery Tax:\t\t\t{grocery_tax_entry.get()}')
            if drink_tax_entry.get()!='$0.0':
                txt_area.insert(END,f'\n Drinks Tax:\t\t\t{drink_tax_entry.get()}')
            txt_area.insert(END, '\n===============================================')
            all_total=(
                total_food_price+total_grocery_price+total_drink_price+food_tax
                +drnk_tax+grocery_tax
            )
            if all_total!=0:
                txt_area.insert(END, f'\n Total: ${all_total}')
            txt_area.insert(END, '\n-----------------------------------------------')
            day=time.strftime('%d')
            month=time.strftime('%b')
            year=time.strftime('%Y')

            hour=time.strftime('%I')
            minute=time.strftime('%M')
            seconds=time.strftime('%S')
            am_pm=time.strftime('%p')
            txt_area.insert(END, f'\n\t\tDate: {day}/ {month}/ {year}')
            txt_area.insert(END, f'\n\t\tTime: {hour}: {minute}: {seconds} {am_pm}')
            txt_area.insert(END, f'\n\t\tReceptionist: Abdulrahman')
            # save_bill()

    def total():
        # if hura.get()==0 and chic.get()==0 and pizz.get()==0 and chip.get()==0 and stic.get()==0:
        #     ttl_.set(0)
        # else:
        global total_food_price
        total_food_price = (
                (hura.get()*1)+
                (sandw.get()*2)+
                (chic.get()* 2.5)+
                (pizz.get() * 5)+
                (chip.get() * 0.5)+
                (stic.get() * 2)

        )
        global food_tax
        ttl_.set(str(f'${total_food_price}'))
        food_tax=(total_food_price*0.1)
        tx_fd.set(f'${food_tax}')


        if  rice.get() == 0 and oil.get() == 0  and dal.get() == 0 and wheat.get() == 0 and sugar.get() == 0 and brd== 0:
            grcry.set(0)
        else:

            global total_grocery_price
            total_grocery_price=(
                (rice.get() *7)+
                (oil.get() *4)+
                (dal.get() *1)+
                (wheat.get() *3)+
                (sugar.get() *9)+
                (brd.get() * 1.5)
            )
            global grocery_tax
            grcry.set(str(f'${total_grocery_price}'))
            grocery_tax = round((total_grocery_price * 0.05), 2)
            tx_grcry.set(f'${grocery_tax}')

        if maza.get() == 0 and milk.get() == 0 and mango.get() == 0 and sprite.get() == 0 and coco.get() \
            and lemon==0:
            drnks.set(0)
        else:
            global total_drink_price
            total_drink_price=(
                (maza.get() *1)+
                (milk.get() *2.99)+
                (mango.get() *3)+
                (sprite.get() *1)+
                (coco.get() *5)+
                (lemon.get() *4)
            )
            global drnk_tax
            drnks.set(str(f'${total_drink_price}'))
            drnk_tax= round((total_drink_price * 0.05), 2)
            tx_drnk.set(str(f'${drnk_tax}'))

    screen = Tk()
    screen.state('zoomed')
    screen.resizable(False,False)
    screen.config(bg='gray')
    screen.title('SOFTWARE')
    Label(screen, text='AL-QUDUS BILLING SOFTWARE', bg='#029', fg='white',
    font=('Verdana', 19, 'bold'), bd=9, relief='ridge', height=2).pack(fill=X)
    customer_frame = Label(screen, bd=6, relief='ridge', bg='#029', height=100, width=1200)
    customer_frame.place(x=0, y=95, relwidth=3, height=80)

    Label(screen, text='Customer Details', bg='#029', fg='yellow',
    font=('Verdana', 14, 'bold'), bd=5, relief='ridge').place(x=0, y=70)
    Label(customer_frame, text='Customer Name', bg='#029', fg='white',
    font=('Verdana', 14)).grid(row=0, column=0, pady=20)
    customer_var=StringVar()
    csname = Entry(customer_frame,textvariable=customer_var, width=20, bd=4, relief='sunken',
           font=('Verdana', 14))
    csname.grid(row=0, column=1)

    Label(customer_frame, text='Phone Number', bg='#029', fg='white',
    font=('Verdana', 14)).grid(row=0, column=2)
    phone=StringVar()
    mobile_num = Entry(customer_frame,textvariable=phone, width=20, bd=4, relief='sunken',
               font=('Verdana', 14))
    mobile_num.grid(row=0, column=3)

    Label(customer_frame, text='Bill Number', bg='#029', fg='white',
    font=('Verdana', 14)).grid(row=0, column=4)
    search=StringVar()
    bill_num = Entry(customer_frame,textvariable=search, width=20, bd=4, relief='sunken',
             font=('Verdana', 14))
    bill_num.grid(row=0, column=5)
    searchTip = Balloon(screen)
    searchTip.label.config(bg='white')
    searchTip.config(bg='white')
    global searchBtn
    searchBtn = Button(customer_frame,command=find_fill, text='Search', bg='#010', fg='white',
            font=('Verdana', 15, 'bold'), bd=5, width=7, relief='groove')
    searchBtn.bind('<Enter>',gethover)
    searchTip.bind_widget(bill_num,balloonmsg='Search Customer Bill Number')
    searchBtn.bind('<Leave>',getLeave)
    # search.bind('<Enter>',gethover)
    # search.bind('<Leave>',getLeave)
    searchBtn.grid(row=0, column=6, padx=20)

    # foods
    foods = Frame(screen, bg='#029', width=430, height=380, bd=7, relief='groove')
    foods.place(x=0, y=176)

    Label(foods, text='Foods', bg='#029', fg='yellow',
    font=('Verdana', 15)).place(x=1, y=1)
    Label(foods, text='Hamburger', bg='#029', fg='white',
    font=('Verdana', 17, 'bold')).place(x=1, y=50
                                      )
    # stris=IntVar()
    # global  humburger
    hura = IntVar()
    chic = IntVar()
    pizz=IntVar()
    stic=IntVar()
    sandw=IntVar()
    chip=IntVar()
    humburger = Entry(foods, textvariable=hura, width=15, bd=5, relief='sunken', font=('Verdana', 14, 'bold'))
    humburger.place(x=150, y=50)
    # line2
    Label(foods, text='Chicken', bg='#029', fg='white',
    font=('Verdana', 17, 'bold')).place(x=1, y=100
                                      )
    # global chick

    chick = Entry(foods,textvariable=chic, width=15, bd=5, relief='sunken', font=('Verdana', 14, 'bold'))
    chick.place(x=150, y=100)

    # lin3
    Label(foods, text='Sandwich', bg='#029', fg='white',
    font=('Verdana', 17, 'bold')).place(x=1, y=150
                                      )
    # global sand
    sand = Entry(foods,textvariable=sandw, width=15, bd=5, relief='sunken', font=('Verdana', 14, 'bold'))
    sand.place(x=150, y=150)

    # line 4
    Label(foods, text='Pizza', bg='#029', fg='white',
    font=('Verdana', 17, 'bold')).place(x=1, y=200
                                      )
    pizza1 = Entry(foods, textvariable=pizz, width=15, bd=5, relief='sunken', font=('Verdana', 14, 'bold'))
    pizza1.place(x=150, y=200)

    # line5
    Label(foods, text='Chips', bg='#029', fg='white',
    font=('Verdana', 17, 'bold')).place(x=1, y=250
                                      )
    # chip=IntVar()
    global chips
    chips = Entry(foods,textvariable=chip, width=15, bd=5, relief='sunken', font=('Verdana', 14, 'bold'))
    chips.place(x=150, y=250)

    # line 6
    Label(foods, text='Stick', bg='#029', fg='white',
    font=('Verdana', 17, 'bold')).place(x=1, y=300
                                      )
    global stick
    stick = Entry(foods,textvariable=stic, width=15, bd=5, relief='sunken', font=('Verdana', 14, 'bold'))
    stick.place(x=150, y=300)
    # _________________________________________________line 2____________
    food2 = Frame(screen, bg='#029', width=430, height=380, bd=7, relief='groove')
    food2.place(x=420, y=176)

    Label(food2, text='Grocery', bg='#029', fg='yellow',
    font=('Verdana', 15)).place(x=1, y=1)
    Label(food2, text='Rice', bg='#029', fg='white',
    font=('Verdana', 17, 'bold')).place(x=1, y=50
                                      )
    rice=IntVar()
    hotdog = Entry(food2,textvariable=rice, width=15, bd=5, relief='sunken', font=('Verdana', 14, 'bold'))
    hotdog.place(x=150, y=50)
    # line2
    Label(food2, text='Food Oil', bg='#029', fg='white',
    font=('Verdana', 17, 'bold')).place(x=1, y=100
                                      )
    oil=IntVar()
    kebab = Entry(food2, textvariable=oil,width=15, bd=5, relief='sunken', font=('Verdana', 14, 'bold'))
    kebab.place(x=150, y=100)

    # lin3
    Label(food2, text='Dal', bg='#029', fg='white',
    font=('Verdana', 17, 'bold')).place(x=1, y=150
                                      )
    dal=IntVar()
    chee = Entry(food2,textvariable=dal, width=15, bd=5, relief='sunken', font=('Verdana', 14, 'bold'))
    chee.place(x=150, y=150)

    # line 4
    Label(food2, text='Wheat', bg='#029', fg='white',
    font=('Verdana', 17, 'bold')).place(x=1, y=200
                                      )
    wheat=IntVar()
    whe = Entry(food2,textvariable=wheat, width=15, bd=5, relief='sunken', font=('Verdana', 14, 'bold'))
    whe.place(x=150, y=200)

    # line5
    Label(food2, text='Sugar', bg='#029', fg='white',
    font=('Verdana', 17, 'bold')).place(x=1, y=250
                                      )
    sugar=IntVar()

    suga = Entry(food2, width=15, bd=5,textvariable=sugar, relief='sunken', font=('Verdana', 14, 'bold'))
    suga.place(x=150, y=250)

    # line 6
    Label(food2, text='Bread', bg='#029', fg='white',
    font=('Verdana', 17, 'bold')).place(x=1, y=300
                                      )
    brd=IntVar()
    bread = Entry(food2,textvariable=brd, width=15, bd=5, relief='sunken', font=('Verdana', 14, 'bold'))
    bread.place(x=150, y=300)
    #     _______________________drinks______________________________

    drinks = Frame(screen, bg='#029', width=300, height=380, bd=7, relief='groove')
    drinks.place(x=810, y=176)

    Label(drinks, text='Drinks', bg='#029', fg='yellow',
    font=('Verdana', 15)).place(x=1, y=1)
    Label(drinks, text='Maza', bg='#029', fg='white',
    font=('Verdana', 17, 'bold')).place(x=1, y=50
                                      )
    maza=IntVar()
    maz = Entry(drinks,textvariable=maza,width=5, bd=5, relief='sunken', font=('Verdana', 14, 'bold'))
    maz.place(x=150, y=50)
    # line2
    Label(drinks, text='Milk', bg='#029', fg='white',
    font=('Verdana', 17, 'bold')).place(x=1, y=100
                                      )
    milk=IntVar()
    mil = Entry(drinks,textvariable=milk, width=5, bd=5, relief='sunken', font=('Verdana', 14, 'bold'))
    mil.place(x=150, y=100)

    # lin3
    Label(drinks, text='Mango', bg='#029', fg='white',
    font=('Verdana', 17, 'bold')).place(x=1, y=150
                                      )
    mango=IntVar()
    man = Entry(drinks, width=5,textvariable=mango, bd=5, relief='sunken', font=('Verdana', 14, 'bold'))
    man.place(x=150, y=150)

    # line 4
    Label(drinks, text='Lemon', bg='#029', fg='white',
    font=('Verdana', 17, 'bold')).place(x=1, y=200
                                      )
    lemon = IntVar()
    leen = Entry(drinks, textvariable=lemon, width=5, bd=5, relief='sunken', font=('Verdana', 14, 'bold'))
    leen.place(x=150, y=200)

    # line5
    Label(drinks, text='Sprite', bg='#029', fg='white',
    font=('Verdana', 17, 'bold')).place(x=1, y=250
                                      )
    sprite=IntVar()
    spr = Entry(drinks, width=5,textvariable=sprite, bd=5, relief='sunken', font=('Verdana', 14, 'bold'))
    spr.place(x=150, y=250)

    # line 6
    Label(drinks, text='Coco', bg='#029', fg='white',
    font=('Verdana', 17, 'bold')).place(x=1, y=300
                                      )
    coco=IntVar()
    cc = Entry(drinks, width=5, bd=5,textvariable=coco, relief='sunken', font=('Verdana', 14, 'bold'))
    cc.place(x=150, y=300)

    # ______________________genretor________
    gnrate = Frame(screen, bd=10, relief='groove')
    gnrate.place(x=1110, y=180, width=420, height=380)
    bill_title = Label(gnrate, text='Billing Area',
               bg='white', font=('verdana', 15, 'bold'),
               bd=7, relief='groove').pack(fill=X)
    scrollbar = Scrollbar(gnrate, orient=VERTICAL)
    txt_area = Text(gnrate, yscrollcommand=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)
    scrollbar.config(command=txt_area.yview)
    txt_area.pack(fill=BOTH)

    # line totals
    frame = Frame(screen, bg='#029', bd=10, relief='groove', width=1800,
          height=230)
    frame.place(x=1, y=560)
    #
    ttl_fds = Label(frame, text='Total Food', bg='#029', fg='yellow',
            font=('Verdana', 18, 'bold'))
    ttl_fds.place(x=3, y=20)
    # global total_foods_entry
    ttl_ = IntVar()
    total_foods_entry = Entry(frame, textvariable=ttl_,
                      font=('Verdana', 14, 'bold'), bd=7, relief='sunken')
    total_foods_entry.place(x=200, y=20)

    # drinks
    grcry=IntVar()
    ttl_grcry = Label(frame, text='Total Grocery', bg='#029', fg='yellow',
              font=('Verdana', 18, 'bold'))
    ttl_grcry.place(x=3, y=70)
    total_grocery_entry = Entry(frame,textvariable=grcry,
                        font=('Verdana', 14, 'bold'), bd=7, relief='sunken')
    total_grocery_entry.place(x=200, y=70)

    # drinks
    ttl_drnks = Label(frame, text='Total Drinks', bg='#029', fg='yellow',
              font=('Verdana', 18, 'bold'))
    ttl_drnks.place(x=3, y=120)
    drnks=IntVar()
    total_drinks_entry = Entry(frame,textvariable=drnks,
                       font=('Verdana', 14, 'bold'), bd=7, relief='sunken')
    total_drinks_entry.place(x=200, y=120)

    # taxs
    food_tx = Label(frame, text='Food Tax', bg='#029', fg='yellow',
            font=('Verdana', 18, 'bold'))
    food_tx.place(x=540, y=20)
    tx_fd=IntVar()
    food_tax_entry = Entry(frame,textvariable=tx_fd,
                   font=('Verdana', 14, 'bold'), bd=7, relief='sunken')
    food_tax_entry.place(x=710, y=20)

    drink_tx = Label(frame, text='Drink Tax', bg='#029', fg='yellow',
             font=('Verdana', 18, 'bold'))
    drink_tx.place(x=540, y=70)
    tx_drnk=IntVar()
    drink_tax_entry = Entry(frame,textvariable=tx_drnk,
                    font=('Verdana', 14, 'bold'), bd=7, relief='sunken')
    drink_tax_entry.place(x=710, y=70)

    # grocery
    groce_tx = Label(frame, text='Grocery Tax', bg='#029', fg='yellow',
             font=('Verdana', 18, 'bold'))
    groce_tx.place(x=540, y=120)
    tx_grcry=IntVar()
    grocery_tax_entry = Entry(frame,textvariable=tx_grcry,
                      font=('Verdana', 14, 'bold'), bd=7, relief='sunken')
    grocery_tax_entry.place(x=710, y=120)

    # gnrate btns
    frame2 = Frame(screen, bg='white', bd=10, relief='groove', width=510, height=220)
    frame2.place(x=1030, y=570)

    totall = Button(frame2, command=total, text='Total', bg='white', bd=10, relief='groove',
            font=('Verdana', 18, 'bold'), width=10)
    totall.place(x=10, y=20)

    generate = Button(frame2,command=area_bill, text='Generate', bg='white', bd=10, relief='groove',
              font=('Verdana', 18, 'bold'), width=10)
    generate.place(x=210, y=20)

    save = Button(frame2,command=save_bill, text='Save', bg='white', bd=10, relief='groove',
           font=('Verdana', 18, 'bold'), width=10)
    save.place(x=10, y=90)

    Exit = Button(frame2,command=exite, text='Exit', bg='#910', fg='white', bd=10, relief='groove',
          font=('Verdana', 18, 'bold'), width=10)
    Exit.place(x=210, y=90)
    welcome()
    mainloop()

# _______________________________________________
    # import mainPanel
#     bill_window()
#     # import mainPanel
# def gethover(event):
#     search.config(bg='#023',fg='white',cursor='hand2')
# def getLeave(event):
#     search.config(bg='#010')

# fonts
fonts=[
    'Abel',
    'Pacifico',
    'Indie Flower',
    'Shadows Into Light',
    'Maven Pro'
]

# screen
login_panel=Tk()
login_panel.state('zoomed')
login_panel.title('Al-Qudus Electronics And Cosmetics Shop ')

# background image
background=ImageTk.PhotoImage(file='bg.jpg')
Label(login_panel,image=background).pack()

# login Frame
login_frame=Frame(login_panel,bd=4,relief='sunken',bg='#fff',width=500,height=670)
login_frame.place(x=20,y=70)

Label(login_frame,text='WELCOME TO- AL-QUDUS RESTAURANT',bg='#fff',fg='black',
      font=('Pacifico',17,'bold')).place(x=10,y=24)
Label(login_frame,text='--And Coffee Shop--',bg='#fff',fg='red',
      font=(fonts[0],17,'bold')).place(x=95,y=50)

Label(login_frame,text='ADMIN LOGIN',bg='#fff',fg='blue',
      font=(fonts[0],20,'bold')).place(x=125,y=130)
Label(login_frame,text='LOGIN HERE !',bg='#fff',fg='red',
      font=(fonts[0],13,'bold')).place(x=155,y=165)
# hr rule
# Label(login_frame,text='______________________',bg='white',
#       fg='black',font=('Verdana',18,'bold')).place(x=80,y=260)
email_box=Entry(login_frame,bd=4,relief='sunken',width=25,font=('Verdana',16))
email_box.place(x=80,y=260)

# user image
img=Image.open('hello.png')
res=img.resize((50,50),Image.ANTIALIAS)
user=ImageTk.PhotoImage(res
                        )
Label(login_frame,image=user,bg='white').place(x=80,y=200)

# password
# Label(login_frame,text='______________________',bg='white',
#       fg='black',font=('Verdana',18,'bold')).place(x=80,y=360)
pasword_box=Entry(login_frame,show='*',bd=4,relief='sunken',width=25,font=('Verdana',16))
pasword_box.place(x=80,y=360)

# pas
img2=Image.open('password-icon-png-22.jpg')
res1=img2.resize((50,50),Image.ANTIALIAS)
pas=ImageTk.PhotoImage(res1
                        )
Label(login_frame,image=pas,bg='white').place(x=80,y=300)

# login btb
forget=Button(login_frame,text='Forgot Password?',cursor='hand2',bg='white',fg='blue',
             font=('Verdana',8,'underline'),bd=0)
forget.place(x=300,y=395)
Login=Button(login_frame,command=login,text='Login',width=9,cursor='hand2',bg='#012',fg='white',
             font=('Verdana',16,'bold'),bd=5,relief='ridge')
Login.place(x=160,y=430)
# show hide
tooltip=Balloon(login_frame)
tooltip.label.config(bg='white')
tooltip.config(bg='white')
show_img=Image.open('show.jpg')
resize=show_img.resize((50,50),Image.ANTIALIAS)
showPassword=ImageTk.PhotoImage(resize)
# hide
hide_img=Image.open('hide.png')
resize2=hide_img.resize((50,50),Image.ANTIALIAS)
hidePassword=ImageTk.PhotoImage(resize2)


btn=Button(login_frame,command=switchCase,image=showPassword,bg='white',bd=0,activebackground='white')
tooltip.bind_widget(btn,balloonmsg='Show Password')
btn.place(x=410,y=350)


Label(login_frame,text='ADEEG TAYAYSAN UGU IMOOW AL-QUDUS',bg='white',
      fg='black',font=("Verdana",8,'bold')).place(x=100,y=530)
Label(login_frame,text='Billing Software',bg='white',
      fg='black',font=("Verdana",8,'bold')).place(x=170,y=555)
Label(login_frame,text='POWERED BY: ENG-CJ',bg='white',
      fg='red',font=("Verdana",12)).place(x=130,y=620)


# panel
def main_panel():
    global  main
    main = Tk()
    main.resizable(0,0)
    main.state('zoomed')
    main.title('AL-QUDUS RESTAURANT | BILL CUSTOMER SYSTEM')
    Label(main, text='', bg='#010', height=6).pack(fill=X)
    slide=''
    count=0


    slider=Label(main, text='AL-QUDUS RESTAURANT', font=('Verdana', 35, 'bold'),
          fg='white', bg='#010')
    slider.place(x=0, y=5)
    # Label(main, text='RESTAURANT', font=('Verdana', 35, 'bold'),
    #       fg='yellow', bg='#010').place(x=290, y=5)
    Label(main, text='HEALTHY FOOD,HEALTH LIFE', font=('Verdana', 13, 'bold'),
          fg='cyan', bg='#010').place(x=290, y=65)
    #     logo
    logo = Image.open('stock.png')
    resz = logo.resize((90, 90), Image.ANTIALIAS)
    log = (ImageTk.PhotoImage(resz))
    img_=Label(main, image=log, bg='#010', bd=0)
    img_.place(x=700, y=1)

    # clock
    clock=Image.open('clock.png')
    clock_res=clock.resize((70,70),Image.ANTIALIAS)
    new_clock=ImageTk.PhotoImage(clock_res)
    Label(main, text='', bg='white', bd=0, height=6, width=130).place(x=800, y=0)
    Label(main, image=new_clock, bg='white', bd=0).place(x=810, y=10)
    time_label=Label(main,text='',bg='white',fg='black',font=('Helvetica',29,'bold'))
    time_label.place(x=900,y=21)

    utc = Label(main, text='TIME UTC NOW', bg='white', fg='red', font=('Helvetica', 13))
    utc.place(x=975
              , y=61)
    def clock():

        hour = time.strftime('%I')
        minutes = time.strftime('%M')
        seconds = time.strftime('%S')
        am_pm = time.strftime('%p')
        time_label.config(text=hour+' : '+ minutes+ ' : '+ seconds+ ' '+ am_pm)
        time_label.after(1000,clock)
    clock()
    # calender
    day=time.strftime('%d')
    month=time.strftime('%b')
    year=time.strftime('%y')
    cl_image=Image.open('cl.png')
    cl_rez=cl_image.resize((85,85),Image.ANTIALIAS)
    ne_cl=ImageTk.PhotoImage(cl_rez)
    calender_label=Label(main,image=ne_cl,bg='white').place(x=1200,y=0)
    cl=Label(main,text=day+' / '+month+ ' / '+year ,bg='white',
             font=('Helvetica',19,'bold')).place(x=1280,y=30)

    # image
    bg=Image.open('order.jpg')
    bg_rez=bg.resize((1300,680),Image.ANTIALIAS)
    new=ImageTk.PhotoImage(bg_rez)
    Label(main,image=new).place(x=270,y=100)

    # notebook
    # notebook=ttk.Notebook(main)
    frame_btns=Frame(main,width=290,height=700,bg='#fff',bd=10,relief='groove')
    frame_btns.place(x=1,y=100)
    bill=Image.open('pay.png')
    res_bill=bill.resize((250,120),Image.ANTIALIAS)
    new_bil=ImageTk.PhotoImage(res_bill)
    global billing
    billing=Button(frame_btns,text='Bill',
    activebackground='white',
    command=getBill,cursor='hand2',compound=TOP,bd=0,font=('Verdana',19,'bold'),bg='white',image=new_bil,
                    )
    billing.bind('<Enter>',hover)
    billing.bind('<Leave>',Leave)
    billing.place(x=1,y=30)

    # help
    help_=Image.open('tree.png')
    help_res=help_.resize((100,100),Image.ANTIALIAS)
    new_help=ImageTk.PhotoImage(help_res)
    global helper
    helper=Button(frame_btns,command=help,text='Help+',
    activebackground='white',cursor='hand2',compound=TOP,bd=0,font=('Verdana',19,'bold'),bg='white',image=new_help,
                    )
    helper.bind('<Enter>',on_hover)
    helper.bind('<Leave>',out_hover)
    helper.place(x=60,y=220)

    # exit
    exit_=Image.open('exit (2).png')
    exit_res=exit_.resize((100,100),Image.ANTIALIAS)
    new_ex=ImageTk.PhotoImage(exit_res)
    global exiting

    exiting= Button(frame_btns,command=ex,text='EXIT',
    activebackground='white',cursor='hand2',compound=TOP,bd=0,font=('Verdana',19,'bold'),bg='white',image=new_ex,
                    )
    exiting.bind('<Enter>',ex_hover)
    exiting.bind('<Leave>',In_hover)
    exiting.place(x=65
                            ,y=400)

    Label(main,text='AL-QUDUS RESTURANT ',bg='white',
          fg='black',font=('Verdana',14,'bold')).place(x=10,y=660)
    Label(main,text='AND COFFEE SHOP',bg='white',
          fg='black',font=('Verdana',14,'bold')).place(x=10,y=690)

    Button(main,text='Setting',bg='white',
          fg='blue',font=('Verdana',14,'underline'),bd=0,cursor='hand2').place(x=10,y=730)


    Button(main,text='Port',bg='white',
          fg='blue',font=('Verdana',14,'underline'),bd=0,cursor='hand2').place(x=100,y=730)
    Button(main,text='Link',bg='white',
          fg='blue',font=('Verdana',14,'underline'),bd=0,cursor='hand2').place(x=160,y=730)

    # times
    mainloop()

# foods

# humb=IntVar()
#
# def bill_window():
#
#     def acc():
#         tt=(
#             (hum.get()*2)+
#             (ch.get()*2)
#         )
#         ttl_.set(str(f'${tt}'))
#
#         # total_foods_entry.insert(0,f'${ttl}')
#     screen=Tk()
#     screen.state('zoomed')
#     screen.config(bg='gray')
#     screen.title('SOFTWARE')
#     Label(screen,text='AL-QUDUS BILLING SOFTWARE',bg='#029',fg='white',
#           font=('Verdana',19,'bold'),bd=9,relief='ridge',height=2).pack(fill=X)
#     customer_frame=Label(screen,bd=6,relief='ridge',bg='#029',height=100,width=1200)
#     customer_frame.place(x=0,y=95,relwidth=3,height=80)
#
#     Label(screen,text='Customer Details',bg='#029',fg='yellow',
#           font=('Verdana',14,'bold'),bd=5,relief='ridge').place(x=0,y=70)
#     Label(customer_frame,text='Customer Name',bg='#029',fg='white',
#           font=('Verdana',14)).grid(row=0,column=0,pady=20)
#     csname=Entry(customer_frame,width=20,bd=4,relief='sunken',
#                  font=('Verdana',14))
#     csname.grid(row=0,column=1)
#
#     Label(customer_frame,text='Phone Number',bg='#029',fg='white',
#           font=('Verdana',14)).grid(row=0,column=2)
#     mobile_num=Entry(customer_frame,width=20,bd=4,relief='sunken',
#                  font=('Verdana',14))
#     mobile_num.grid(row=0,column=3)
#
#
#     Label(customer_frame,text='Bill Number',bg='#029',fg='white',
#           font=('Verdana',14)).grid(row=0,column=4)
#     bill_num=Entry(customer_frame,width=20,bd=4,relief='sunken',
#                  font=('Verdana',14))
#     bill_num.grid(row=0,column=5)
#     global search
#     search=Button(customer_frame,text='Search',bg='#010',fg='white',
#                   font=('Verdana',15,'bold'),bd=5,width=7,relief='groove')
#     search.bind('<Enter>',gethover)
#     search.bind('<Leave>',getLeave)
#     search.grid(row=0,column=6,padx=20)
#
#     # foods
#     foods=Frame(screen,bg='#029',width=430,height=380,bd=7,relief='groove')
#     foods.place(x=0,y=176)
#
#     Label(foods,text='Foods',bg='#029',fg='yellow',
#           font=('Verdana',15)).place(x=1,y=1)
#     Label(foods,text='Hamburger',bg='#029',fg='white',
#           font=('Verdana',17,'bold')).place(x=1,y=50
#                                             )
#     # stris=IntVar()
#     hum=IntVar()
#     humburger=Entry(foods,textvariable=hum,width=15,bd=5,relief='sunken',font=('Verdana',14,'bold'))
#     humburger.place(x=150,y=50)
#     #line2
#     Label(foods,text='Chicken',bg='#029',fg='white',
#           font=('Verdana',17,'bold')).place(x=1,y=100
#                                          )
#     global chick
#     ch=IntVar()
#     chick=Entry(foods,textvariable=ch,width=15,bd=5,relief='sunken',font=('Verdana',14,'bold'))
#     chick.place(x=150,y=100)
#
#     #lin3
#     Label(foods,text='Sandwich',bg='#029',fg='white',
#           font=('Verdana',17,'bold')).place(x=1,y=150
#                                             )
#     global sand
#     sand=Entry(foods,width=15,bd=5,relief='sunken',font=('Verdana',14,'bold'))
#     sand.place(x=150,y=150)
#
#     #line 4
#     Label(foods,text='Pizza',bg='#029',fg='white',
#           font=('Verdana',17,'bold')).place(x=1,y=200
#                                             )
#     global pizza
#     pizza=Entry(foods,width=15,bd=5,relief='sunken',font=('Verdana',14,'bold'))
#     pizza.place(x=150,y=200)
#
#     #line5
#     Label(foods,text='Chips',bg='#029',fg='white',
#           font=('Verdana',17,'bold')).place(x=1,y=250
#                                             )
#     # chip=IntVar()
#     global  chips
#     chips=Entry(foods,width=15,bd=5,relief='sunken',font=('Verdana',14,'bold'))
#     chips.place(x=150,y=250)
#
#     #line 6
#     Label(foods,text='Stick',bg='#029',fg='white',
#           font=('Verdana',17,'bold')).place(x=1,y=300
#                                             )
#     global  stick
#     stick=Entry(foods,width=15,bd=5,relief='sunken',font=('Verdana',14,'bold'))
#     stick.place(x=150,y=300)
#     #_________________________________________________line 2____________
#     food2 = Frame(screen, bg='#029', width=430, height=380, bd=7, relief='groove')
#     food2.place(x=420, y=176)
#
#     Label(food2, text='Grocery', bg='#029', fg='yellow',
#           font=('Verdana', 15)).place(x=1, y=1)
#     Label(food2, text='Rice', bg='#029', fg='white',
#           font=('Verdana', 17, 'bold')).place(x=1, y=50
#                                               )
#     hotdog = Entry(food2, width=15, bd=5, relief='sunken', font=('Verdana', 14, 'bold'))
#     hotdog.place(x=150, y=50)
#     # line2
#     Label(food2, text='Food Oil', bg='#029', fg='white',
#           font=('Verdana', 17, 'bold')).place(x=1, y=100
#                                               )
#     kebab = Entry(food2, width=15, bd=5, relief='sunken', font=('Verdana', 14, 'bold'))
#     kebab.place(x=150, y=100)
#
#     # lin3
#     Label(food2, text='Dal', bg='#029', fg='white',
#           font=('Verdana', 17, 'bold')).place(x=1, y=150
#                                               )
#     chee = Entry(food2, width=15, bd=5, relief='sunken', font=('Verdana', 14, 'bold'))
#     chee.place(x=150, y=150)
#
#
#     # line 4
#     Label(food2, text='Wheat', bg='#029', fg='white',
#           font=('Verdana', 17, 'bold')).place(x=1, y=200
#                                               )
#     pizza = Entry(food2, width=15, bd=5, relief='sunken', font=('Verdana', 14, 'bold'))
#     pizza.place(x=150, y=200)
#
#     # line5
#     Label(food2, text='Sugar', bg='#029', fg='white',
#           font=('Verdana', 17, 'bold')).place(x=1, y=250
#                                               )
#     roast = Entry(food2, width=15, bd=5, relief='sunken', font=('Verdana', 14, 'bold'))
#     roast.place(x=150, y=250)
#
#     # line 6
#     Label(food2, text='Bread', bg='#029', fg='white',
#           font=('Verdana', 17, 'bold')).place(x=1, y=300
#                                               )
#     bread = Entry(food2, width=15, bd=5, relief='sunken', font=('Verdana', 14, 'bold'))
#     bread.place(x=150, y=300)
# #     _______________________drinks______________________________
#
#     drinks = Frame(screen, bg='#029', width=300, height=380, bd=7, relief='groove')
#     drinks.place(x=810, y=176)
#
#     Label(drinks, text='Drinks', bg='#029', fg='yellow',
#           font=('Verdana', 15)).place(x=1, y=1)
#     Label(drinks, text='Maza', bg='#029', fg='white',
#           font=('Verdana', 17, 'bold')).place(x=1, y=50
#                                               )
#     hotdog = Entry(drinks, width=5, bd=5, relief='sunken', font=('Verdana', 14, 'bold'))
#     hotdog.place(x=150, y=50)
#     # line2
#     Label(drinks, text='Milk', bg='#029', fg='white',
#           font=('Verdana', 17, 'bold')).place(x=1, y=100
#                                               )
#     kebab = Entry(drinks, width=5, bd=5, relief='sunken', font=('Verdana', 14, 'bold'))
#     kebab.place(x=150, y=100)
#
#     # lin3
#     Label(drinks, text='Mango', bg='#029', fg='white',
#           font=('Verdana', 17, 'bold')).place(x=1, y=150
#                                               )
#     chee = Entry(drinks, width=5, bd=5, relief='sunken', font=('Verdana', 14, 'bold'))
#     chee.place(x=150, y=150)
#
#
#     # line 4
#     Label(drinks, text='Lemon', bg='#029', fg='white',
#           font=('Verdana', 17, 'bold')).place(x=1, y=200
#                                               )
#     pizza = Entry(drinks, width=5, bd=5, relief='sunken', font=('Verdana', 14, 'bold'))
#     pizza.place(x=150, y=200)
#
#     # line5
#     Label(drinks, text='Sprite', bg='#029', fg='white',
#           font=('Verdana', 17, 'bold')).place(x=1, y=250
#                                               )
#     roast = Entry(drinks, width=5, bd=5, relief='sunken', font=('Verdana', 14, 'bold'))
#     roast.place(x=150, y=250)
#
#     # line 6
#     Label(drinks, text='Coco', bg='#029', fg='white',
#           font=('Verdana', 17, 'bold')).place(x=1, y=300
#                                               )
#     bread = Entry(drinks, width=5, bd=5, relief='sunken', font=('Verdana', 14, 'bold'))
#     bread.place(x=150, y=300)
#
# #______________________genretor________
#     gnrate=Frame(screen,bd=10,relief='groove')
#     gnrate.place(x=1110,y=180,width=420,height=380)
#     bill_title=Label(gnrate,text='Billing Area',
#                      bg='white',font=('verdana',15,'bold'),
#                      bd=7,relief='groove').pack(fill=X)
#     scrollbar=Scrollbar(gnrate, orient=VERTICAL)
#     txt_area=Text(gnrate,yscrollcommand=scrollbar.set)
#     scrollbar.pack(side=RIGHT,fill=Y)
#     scrollbar.config(command=txt_area.yview)
#     txt_area.pack(fill=BOTH)
#
#     # line totals
#     frame=Frame(screen,bg='#029',bd=10,relief='groove',width=1800,
#                 height=230)
#     frame.place(x=1,y=560)
#     #
#     ttl_fds=Label(frame,text='Total Food',bg='#029',fg='yellow',
#                   font=('Verdana',18,'bold'))
#     ttl_fds.place(x=3,y=20)
#     global total_foods_entry
#     ttl_=StringVar()
#     total_foods_entry=Entry(frame,textvariable=ttl_,
#                   font=('Verdana',14,'bold'),bd=7,relief='sunken')
#     total_foods_entry.place(x=200,y=20)
#
#     # drinks
#     ttl_grcry=Label(frame,text='Total Grocery',bg='#029',fg='yellow',
#                   font=('Verdana',18,'bold'))
#     ttl_grcry.place(x=3,y=70)
#     total_grocery_entry=Entry(frame,
#                   font=('Verdana',14,'bold'),bd=7,relief='sunken')
#     total_grocery_entry.place(x=200,y=70)
#
    # #drinks
    # ttl_drnks=Label(frame,text='Total Drinks',bg='#029',fg='yellow',
    #               font=('Verdana',18,'bold'))
    # ttl_drnks.place(x=3,y=120)
    # total_drinks_entry=Entry(frame,
    #               font=('Verdana',14,'bold'),bd=7,relief='sunken')
    # total_drinks_entry.place(x=200,y=120)
    #
    # # taxs
    # food_tx=Label(frame,text='Food Tax',bg='#029',fg='yellow',
    #               font=('Verdana',18,'bold'))
    # food_tx.place(x=540,y=20)
    # food_tax_entry=Entry(frame,

# loop
mainloop()