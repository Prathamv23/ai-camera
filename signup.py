from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from  tkinter import PhotoImage
import pymysql

#function section

def clear():
   emailEntry.delete(0,END)
   usernameEntry.delete(0,END)
   passwordEntry.delete(0,END)
   confirmEntry.delete(0,END)
   check.set(0)

def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirmEntry.get()=='':
      messagebox.showerror('Error','All Fields Are Required!')
    elif passwordEntry.get() != confirmEntry.get():
       messagebox.showerror('Error','Password Mismatch')
    elif check.get()==0:
       messagebox.showerror('Error','Please Accept Terms & Condition!')
    else:
        try:
           con=pymysql.connect(host='localhost',user='root',password='Admin@123',port=3307)
           mycursor=con.cursor()
        except:
           messagebox.showerror('Error','Database Connectivity Issue, Please Try Agian!')
           return
        try:
           query='create database userdata'
           mycursor.execute(query)
           query='use userdata'
           mycursor.execute(query)
           query='create table data(id int auto_increment primary key not null,email varchar(50),username varchar(100),password varchar(20))'
           mycursor.execute(query)
        except:
           mycursor.execute('use userdata')

        query='insert into data(email,username,password) values(%s,%s,%s)'
        mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
        con.commit()
        con.close()
        messagebox.showinfo('Success','Registration is successful')
        clear()
        root.destroy()
        import mainlogin

def login_page():
    root.destroy()
    import mainlogin

#GUI section

root=Tk()
root.title('Signup Page')
root.resizable(False,False)
root.iconphoto(False,PhotoImage(file="images\\logo.png"))
background=ImageTk.PhotoImage(file='images\\bg.jpg')

bgLable=Label(root,image=background)
bgLable.grid()

frame=Frame(root,bg='white')
frame.place(x=554,y=100)

#heading part

heading=Label(frame,text='CREATE AN ACCOUNT',font=('Microsoft Yahei UI Light',18,'bold')
              ,bg='white',fg='firebrick1')
heading.grid(row=0,column=0,padx=10,pady=10)

#email part

emailLabel=Label(frame,text='Email',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick')
emailLabel.grid(row=1,column=0,sticky='W',padx=25,pady=(10,0))

emailEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
emailEntry.grid(row=2,column=0,sticky='W',padx=25)

#username part

usernameLabel=Label(frame,text='Username',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick')
usernameLabel.grid(row=3,column=0,sticky='W',padx=25,pady=(10,0))

usernameEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
usernameEntry.grid(row=4,column=0,sticky='W',padx=25)

#password part

passwordLabel=Label(frame,text='Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick')
passwordLabel.grid(row=5,column=0,sticky='W',padx=25,pady=(10,0))

passwordEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
passwordEntry.grid(row=6,column=0,sticky='W',padx=25)

#confirm password part

confirmLabel=Label(frame,text='Confirm Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick')
confirmLabel.grid(row=7,column=0,sticky='W',padx=25,pady=(10,0))

confirmEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
confirmEntry.grid(row=8,column=0,sticky='W',padx=25)

check=IntVar()
termsandcondition=Checkbutton(frame,text='I agree to the Terms & Conditions',font=('Microsoft Yahei UI Light',9,'bold'),fg='firebrick1',bg='white',activebackground='white',activeforeground='firebrick1',cursor='hand2',variable=check)
termsandcondition.grid(row=9,column=0,pady=10,padx=15)

signupButton=Button(frame,text='Signup',font=('Open Sans',16,'bold'),bd=0,bg='firebrick1',fg='white',activebackground='firebrick1',activeforeground='white',width=17,command=connect_database)
signupButton.grid(row=10,column=0,pady=10)

alreadyaccounr=Label(frame,text="Don't have an account?",font=('Open Sans',9,'bold'),bg='white',fg='firebrick1')
alreadyaccounr.grid(row=11,column=0,sticky='W',padx=25,pady=10)

loginButton=Button(frame,text='Log in',font=('Open Sans',9,'bold underline'),bg='white',fg='blue',bd=0,cursor='hand2',activebackground='white',activeforeground='blue',command=login_page)
loginButton.place(x=170,y=404)

root.mainloop()
