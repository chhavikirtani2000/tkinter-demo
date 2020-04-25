from tkinter import *
import sqlite3

root = Tk()
root.geometry('500x500')
root.title("Registration Form")


Fullname=StringVar()
Email=StringVar()
var = IntVar()
c=StringVar()
var1= IntVar()
def exitt():
    exit()
def second_win():
    window=Tk()
    window.title("welcome to second window")
    window.geometry('250x200')
    label_02=Label(window,text='Signup successful', relief="solid",font=('arial',12,'bold')).place(x=30,y=70)
    but_01=Button(window, text='demo',width=20,bg='brown',fg='white',command=database).place(x=80,y=110)
    root.destroy()
def database():
   name1=Fullname.get()
   email=Email.get()
   gender=var.get()
   country=c.get()
   prog=var1.get()
   conn = sqlite3.connect('Form.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Email TEXT,Gender TEXT,country TEXT,Programming TEXT)')
   cursor.execute('INSERT INTO Student (FullName,Email,Gender,country,Programming) VALUES(?,?,?,?,?)',(name1,email,gender,country,prog,))
   conn.commit()
   
   
             
label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root,textvar=Fullname)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Email",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root,textvar=Email)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
label_3.place(x=70,y=230)

Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)

label_4 = Label(root, text="country",width=20,font=("bold", 10))
label_4.place(x=70,y=280)

list1 = ['Canada','India','UK','Nepal','Iceland','South Africa'];

droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
c.set('select your country') 
droplist.place(x=240,y=280)

label_4 = Label(root, text="Programming",width=20,font=("bold", 10))
label_4.place(x=85,y=330)
var2= IntVar()
Checkbutton(root, text="java", variable=var1).place(x=235,y=330)

Checkbutton(root, text="python", variable=var2).place(x=290,y=330)

Button(root, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=380)
but_login = Button(root, text='Signup',width=20,bg='brown',fg='white',command=second_win).place(x=180,y=400)
conn = sqlite3.connect('Form.db')
c=conn.cursor()
rows=c.execute("SELECT * FROM Student")
records=c.fetchall()
for row in records:
    print(row[0])
    print(row[1])
    lab1=Label(root, text=row[0],width=20,font=("bold", 10))
    lab1.place(x=150,y=400)
    lab11=Label(root, text=row[1],width=20,font=("bold", 10))
    lab11.place(x=100,y=300)
#data = []
#for row in rows:
#        data.append(list(row))
#label = data

#label_5=Label(root, text=label,width=20,font=("bold", 10))
label_4.place(x=90,y=280)
root.mainloop()
