from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
root = Tk()
root.title('Airline Reservation')
root.geometry('1100x650')

bgimg = PhotoImage(file='plane.png')
limg = Label(root, image=bgimg)
limg.pack()

lbl1 = Label(root,text='AIRLINE RESERVATION', font=("Times New Roman", 25),bg='#549DB1')
lbl1.place(x=360,y=25)

lbl2 = Label(root,text='Name:',font=("Times New Roman", 15),bg='#60a1b3')
lbl2.place(x=300,y=100)

entry = Entry(root,relief='sunken',width=35,font=("Times New Roman", 15),bg='#ccc6c4')
entry.place(x=400,y=102)

lbl3 = Label(root,text='From:',font=("Times New Roman", 15),bg='#60a1b3')
lbl3.place(x=300,y=150)

style= ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground= "#ccc6c4", background= "#ccc6c4")

city=StringVar()
options = ('Agra','Ahmedabad','Amritsar','Bengaluru','Chandigarh','Chennai','Coimbatore','Gangtok','Hyderbad','Jaipur','Jammu','Jodhpur','Kolkata','Lucknow','Mumbai','New Delhi','Puducherry','Pune','Rajkot','Ranchi','Shillong','Surat','Thiruvanthampuram','Visakhapatnam')
box = ttk.Combobox(root,value=options,textvariable=city,font=("Times New Roman", 12))
box.place(x=300,y=190)

lbl3 = Label(root,text='To:',font=("Times New Roman", 15),bg='#60a1b3')
lbl3.place(x=600,y=150)

cities=StringVar()
option = ('Agra','Ahmedabad','Amritsar','Bengaluru','Chandigarh','Chennai','Coimbatore','Gangtok','Hyderbad','Jaipur','Jammu','Jodhpur','Kolkata','Lucknow','Mumbai','New Delhi','Puducherry','Pune','Rajkot','Ranchi','Shillong','Surat','Thiruvanthampuram','Visakhapatnam')
box = ttk.Combobox(root,value=option,textvariable=cities,font=("Times New Roman", 12))
box.place(x=600,y=190)

lbl4 = Label(root,text='Departure',font=("Times New Roman", 15),bg='#60a1b3')
lbl4.place(x=300,y=250)

cal1 = DateEntry(root, width= 20, background= "magenta3", foreground= "white",bd=1,font=("Times New Roman", 12))
cal1.place(x=300,y=290)

lbl5 = Label(root,text='Return',font=("Times New Roman", 15),bg='#60a1b3')
lbl5.place(x=600,y=250)

cal2 = DateEntry(root, width= 20, background= "magenta3", foreground= "white",bd=1,font=("Times New Roman", 12))
cal2.place(x=600,y=290)

lbl6 = Label(root,text='Adult',font=("Times New Roman", 15),bg='#60a1b3')
lbl6.place(x=300,y=350)

year1 = IntVar()
sbox1 = Spinbox(root,from_=0, to = 9, textvariable = year1,width=25,bg='#ccc6c4')
sbox1.place(x=300,y=390)

lbl7 = Label(root,text='Children',font=("Times New Roman", 15),bg='#60a1b3')
lbl7.place(x=600,y=350)

year2 = IntVar()
sbox2 = Spinbox(root,from_=0, to = 9, textvariable = year2,width=25,bg='#ccc6c4')
sbox2.place(x=600,y=390)

lbl8 = Label(root,text='Class',font=("Times New Roman", 15),bg='#60a1b3')
lbl8.place(x=300,y=450)

clas = StringVar()
opt = ('Economy','Premium','Business')
cbox = ttk.Combobox(root, value=opt,textvariable=clas,width=46,font=("Times New Roman", 15))
cbox.place(x=300,y=490)

btn = Button(root, text="Show Flights",font=("Times New Roman", 15),width=40,bg='#de9b7e')
btn.place(x=320,y=550)



root.mainloop()