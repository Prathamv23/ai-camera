from tkinter import*
from tkinter import messagebox
from PIL import ImageTk
import pymysql


def forget_pass():
    def change_password():
        if user_Entry.get()=='' or password_Entry.get()=='' or confirmpass_Entry.get()=='':
            messagebox.showerror('Error','All Fields Are Required!',parent=window)
        elif password_Entry.get()!=confirmpass_Entry.get():
            messagebox.showerror('Error','Password and Confirm Password are not maching!',parent=window)
        else:
            con=pymysql.connect(host='localhost',user='root',password='Admin@123',port=3307,database='userdata')
            mycursor=con.cursor()
            query='select * from data where username=%s'
            mycursor.execute(query,(user_Entry.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error','Incorrect Username',parent=window)
            else:
                query='update data set password=%s where username=%s'
                mycursor.execute(query,(password_Entry.get(),user_Entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success','Password is reset, Please login with new password',parent=window)
                window.destroy()


    window=Toplevel()
    window.title('Change Password')

    bgPic=ImageTk.PhotoImage(file='images\\background.jpg')
    bgLabel=Label(window,image=bgPic)
    bgLabel.grid()

    heading_label=Label(window,text='RESET PASSWORD',font=('arial','18','bold'),bg='white',fg='magenta2')
    heading_label.place(x=480,y=60)

    userLabel=Label(window,text='Username',font=('arial',12,'bold'),bg='white',fg='orchid1')
    userLabel.place(x=470,y=130)

    user_Entry=Entry(window,width=25,font=('arial',11,'bold'),bd=0,fg='magenta2')
    user_Entry.place(x=470,y=160)

    Frame(window,width=250,height=2,bg='orchid1').place(x=470,y=180)

    passwordLabel=Label(window,text='New Password',font=('arial',12,'bold'),bg='white',fg='orchid1')
    passwordLabel.place(x=470,y=210)

    password_Entry=Entry(window,width=25,font=('arial',11,'bold'),bd=0,fg='magenta2')
    password_Entry.place(x=470,y=240)

    Frame(window,width=250,height=2,bg='orchid1').place(x=470,y=260)

    confirmpassLabel=Label(window,text='Confirm Password',font=('arial',12,'bold'),bg='white',fg='orchid1')
    confirmpassLabel.place(x=470,y=290)

    confirmpass_Entry=Entry(window,width=25,font=('arial',11,'bold'),bd=0,fg='magenta2')
    confirmpass_Entry.place(x=470,y=320)

    Frame(window,width=250,height=2,bg='orchid1').place(x=470,y=340)

    submitButton=Button(window,text='Submit',bd=0,bg='magenta2',fg='white',font=('Open Sans','16','bold'),width=19,cursor='hand2',activebackground='magenta2',activeforeground='white',command=change_password)
    submitButton.place(x=470,y=390)

    window.mainloop()

def login_user():
    if UsernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All Fields Are Required!')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='Admin@123',port=3307)
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Connection is not established try again')
            return
        query='use userdata'
        mycursor.execute(query)
        query='select * from data where username=%s and password=%s'
        mycursor.execute(query,(UsernameEntry.get(),passwordEntry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid usernme or password')
        else:
            #messagebox.showinfo('Welcome','Login is sucessful')
            root.destroy()
            import dashboard




def signup_page():
    root.destroy()
    import signup

def user_enter(event):
    if UsernameEntry.get()=='Username':
        UsernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)

def hide():
    openeye.config(file='D:\\defence system\\images\\closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='D:\\defence system\\images\\closeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)


#GUI section

root=Tk()
root.geometry('990x660+50+50')
root.resizable(0,0)
root.title('Login Page')
root.iconphoto(False,PhotoImage(file="images\\logo.png"))
bgImage=ImageTk.PhotoImage(file='images\\bg.jpg')

bgLabel=Label(root,image=bgImage)
bgLabel.place(x=0,y=0)

heading=Label(root,text='USER LOGIN',font=('Microsoft Yahei UI Light',23,'bold')
              ,bg='white',fg='firebrick1')
heading.place(x=605,y=120)

#user part

UsernameEntry=Entry(root,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
UsernameEntry.place(x=580,y=200)
UsernameEntry.insert(0,'Username')

UsernameEntry.bind('<FocusIn>',user_enter)

frame1=Frame(root,width=250,height=2,bg='firebrick').place(x=580,y=222)

#password part

passwordEntry=Entry(root,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
passwordEntry.place(x=580,y=260)
passwordEntry.insert(0,'Password')

passwordEntry.bind('<FocusIn>',password_enter)

frame2=Frame(root,width=250,height=2,bg='firebrick').place(x=580,y=282)

#eye button

openeye=PhotoImage(file='images\\openeye.png')
eyeButton=Button(root,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=800,y=254)

forgetButton=Button(root,text='Forget Password?',bd=0,bg='white',activebackground='white',cursor='hand2',font=('Microsoft Yahei UI Light',9,'bold'),fg='firebrick1',activeforeground='firebrick1',command=forget_pass)
forgetButton.place(x=715,y=295)

loginButton=Button(root,text='Login',font=('Open Sans',16,'bold'),fg='white',bg='firebrick1',activeforeground='white',activebackground='firebrick1',cursor='hand2',bd=0,width=19,command=login_user)
loginButton.place(x=578,y=350)

orlable=Label(root,text='--------------- OR ---------------',font=('Open Sans',16),fg='firebrick1',bg='white')
orlable.place(x=583,y=400)

facebook_logo=PhotoImage(file='images\\facebook.png')
fbLabel=Label(root,image=facebook_logo,bg='white')
fbLabel.place(x=610,y=440)

google_logo=PhotoImage(file='images\\google.png')
googleLabel=Label(root,image=google_logo,bg='white')
googleLabel.place(x=660,y=440)

twitter_logo=PhotoImage(file='images\\twitter.png')
twitterLabel=Label(root,image=twitter_logo,bg='white')
twitterLabel.place(x=710,y=440)

instagram_logo=PhotoImage(file='images\\instagram.png')
instagramLabel=Label(root,image=instagram_logo,bg='white')
instagramLabel.place(x=760,y=440)

signuplable=Label(root,text='Dont have an account?',font=('Open Sans',9,'bold'),fg='firebrick1',bg='white')
signuplable.place(x=590,y=500)

newaccButton=Button(root,text='Create new one!',font=('Open Sans',9,'bold underline'),fg='blue',bg='white',activeforeground='blue',activebackground='firebrick1',cursor='hand2',bd=0,command=signup_page)
newaccButton.place(x=727,y=500)


root.mainloop()
