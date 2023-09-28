from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import sqlite3



def forget_pass():
    window=Toplevel()
    window.title('Change Password')

    bgPic=ImageTk.PhotoImage(file='background.jpg')
    bglabel=Label(window,image=bgPic)
    bglabel.grid()

    heading_label= Label(window,text='Reset Password', font=('arial','18','bold'),bg='white',fg='magenta2')
    heading_label.place(x=470,y=100)

    user_entry = Entry(window, width=25, font=('arial', 11, 'bold'), fg='magenta2')
    user_entry.place(x=470, y=160)

    Frame(window,width=250,height=2, bg='orchid1').place(x=470,y=180)

    passwordLabel = Label(window, text='New Password', font=('arial', 12, 'bold'), bg='white', fg='orchid1')
    passwordLabel.place(x=470, y=210)


    newpass_entry=Entry(window,width=25)

    window.mainloop()



def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All fields are required')

    else:
        try:
            con = sqlite3.connect('logininfo.db')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Connection is not established try again')
            return
        query='''select * from data where username=? and password=?'''
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid username or password')
        else:
            messagebox.showinfo('Welcome','Login is successful')
            login_window.destroy()
            import MainProj




def signup_page():
    login_window.destroy()
    import signup


def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)


def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)


def user_enter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)


def password_enter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)


login_window = Tk()
login_window.geometry('990x660+50+50')
login_window.resizable(0, 0)
login_window.title('Login Page')

bgImage = ImageTk.PhotoImage(file='bg.jpg')
bgLabel = Label(login_window, image=bgImage)
bgLabel.place(x=0, y=0)

heading = Label(login_window, text='USER LOGIN', font=('Microsoft Yahei UI Light', 23, 'bold'), bg='white', fg='firebrick1')
heading.place(x=605, y=120)

usernameEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'), bg='white', fg='firebrick1')
usernameEntry.place(x=580, y=200)
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>', user_enter)

frame1 = Frame(login_window, width=250, height=2, bg='firebrick1')
frame1.place(x=580, y=222)

passwordEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'), bg='white', fg='firebrick1',show='*')
passwordEntry.place(x=580, y=260)
passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>', password_enter)
frame2 = Frame(login_window, width=250, height=2, bg='firebrick1')
frame2.place(x=580, y=282)

openeye = PhotoImage(file='openeye.png')
eyeButton = Button(login_window, image=openeye, bd=0, bg='white', activebackground='white', cursor='hand2', command=hide)
eyeButton.place(x=800, y=255)

forgetButton=Button(login_window, text='forgot Password?',bd=0,activebackground='white'
                    ,cursor='hand2',font=('Microsoft Yahei UI Light', 9, 'bold'), bg='white', fg='firebrick1',activeforeground='firebrick1',command=forget_pass)
forgetButton.place(x=715,y=295)

loginButton=Button(login_window,text='Login',font=('Open Sans',16,'bold'),fg='white'
                   ,bg='firebrick1',activeforeground='white',activebackground='firebrick1',cursor='hand2',bd=0,width=19,command=login_user)
loginButton.place(x=578,y=350)


orLabel=Label(login_window,text='----------OR----------',font=('Open Sans',20),fg='firebrick1',bg='white')
orLabel.place(x=583,y=400)

facebook_logo=PhotoImage(file='facebook.png')
facebookLabel=Label(login_window,image=facebook_logo,bg='white')
facebookLabel.place(x=640,y=440)

google_logo=PhotoImage(file='google.png')
googleLabel=Label(login_window,image=google_logo,bg='white')
googleLabel.place(x=690,y=440)

twitter_logo=PhotoImage(file='twitter.png')
twitterLabel=Label(login_window,image=twitter_logo,bg='white')
twitterLabel.place(x=740,y=440)


signupLabel=Label(login_window,text='Dont have an account?',font=('Open Sans',9,'bold'),fg='firebrick1')
signupLabel.place(x=590,y=500)

newaccountButton=Button(login_window,text='Create new one',font=('Open Sans',9,'bold underline'),
                        fg='blue',bg='white',activeforeground='blue',activebackground='white',cursor='hand2',bd=0,command=signup_page)
newaccountButton.place(x=727,y=500)




login_window.mainloop()