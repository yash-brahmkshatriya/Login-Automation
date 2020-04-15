from tkinter import *
import pickle
from tkinter.ttk import Style
from Sites import open_sites
import os
main_window=Tk()

AUTH = False
NEW_USR = False
USER = 'Yash'

path_to_users = ''

usernames={}
users_det={}

def setAuth(login_window):
    global AUTH
    AUTH=True
    login_window.destroy()
def setUSER(val):
    global USER
    USER=val
def add_user(name_,details_,wind,id_cf,pwd_cf,id_cc,pwd_cc,id_spoj,pwd_spoj):
    global NEW_USR
    global USER
    global path_to_users
    
    wind.destroy()
    NEW_USR = True
    USER = name_
    
    details_["codeforces"]=str(id_cf.get()+' '+pwd_cf.get())
    details_["codechef"]=str(id_cc.get()+' '+pwd_cc.get())
    details_["spoj"]=str(id_spoj.get()+' '+pwd_spoj.get())
    
    users_det[name_]=details_
    with open(str(path_to_users+"/users.pickle"),"wb") as fw:
        pickle.dump(users_det,fw)
    print('User added')
def login_fun():
    global AUTH
    global USER
    global main_window
    main_window.destroy()
    login_window=Tk()
    login_window.title('Login')
    login_window.geometry('300x100')
    Label(login_window, text="Select User:").grid(row=1,column=1,padx=(10,10),pady=(10,10))
    # Label(login_window, text="Select User:").pack(side="left",padx=(10,10),pady=(10,10))
    tkvar = StringVar(login_window)
    tkvar.set('Yash')
    popupMenu = OptionMenu(login_window, tkvar, *usernames,command=setUSER).grid(row=1,column=2,padx=(10,20),pady=(10,10))
    # popupMenu = OptionMenu(login_window, tkvar, *usernames).pack(side="left",padx=(10,20),pady=(10,10))
    auth_button = Button(login_window,text="Authenticate!",command=lambda:setAuth(login_window)).grid(row=2,column=1,padx=(100,30),pady=(10,10))
    # auth_button = Button(login_window,text="Authenticate!",command=setAuth).pack(padx=(100,30),pady=(10,10),expand=True)
    if AUTH:
        return
def signup_fun():
    global main_window
    main_window.destroy()
    signup_window=Tk()
    signup_window.title('Sign Up')
    signup_window.geometry('300x100')
    Label(signup_window, text="Name:").grid(row=2,column=1,padx=(60,0),pady=(10,0))
    n11=StringVar()
    nam=Entry(signup_window,textvariable=n11).grid(row=2,column=2,pady=(10,0))
    enter=Button(signup_window,text="Enter",command=lambda:get_signup_details(signup_window,n11),width=10).grid(row=3,column=2,padx=(15,20),pady=(10,10))
def get_signup_details(signup_window,usr):
    if usr.get().lower() in usernames:
        print('User exists')
        return
    signup_window.destroy()
    det_window=Tk()
    det_window.title('Data Entry')
    det_window.geometry('500x500')
    
    id_cf=StringVar()
    pwd_cf=StringVar()
    id_cc=StringVar()
    pwd_cc=StringVar()
    id_spoj=StringVar()
    pwd_spoj=StringVar()
    details_={}
    #Taking CodeForces
    Label(det_window, text="CF Id:").grid(row=1,column=1,padx=(60,10),pady=(10,10))
    entrycfi=Entry(det_window,textvariable=id_cf).grid(row=1,column=2,padx=(60,10),pady=(10,10))
    Label(det_window, text="CF Pwd:").grid(row=2,column=1,padx=(60,10),pady=(10,10))
    entrycfp=Entry(det_window,textvariable=pwd_cf).grid(row=2,column=2,padx=(60,10),pady=(10,10))
    # details_["codeforces"]=id_cf.get()+' '+pwd_cf.get()
    #Taking CodeChef
    Label(det_window, text="CC Id:").grid(row=3,column=1,padx=(60,10),pady=(10,10))
    entrycci=Entry(det_window,textvariable=id_cc).grid(row=3,column=2,padx=(60,10),pady=(10,10))
    Label(det_window, text="CC Pwd:").grid(row=4,column=1,padx=(60,10),pady=(10,10))
    entryccp=Entry(det_window,textvariable=pwd_cc).grid(row=4,column=2,padx=(60,10),pady=(10,10))
    # details_["codechef"]=id_cc.get()+' '+pwd_cc.get()
    #Taking SPOJ
    Label(det_window, text="SPOJ Id:").grid(row=5,column=1,padx=(60,10),pady=(10,10))
    entryspoji=Entry(det_window,textvariable=id_spoj).grid(row=5,column=2,padx=(60,10),pady=(10,10))
    Label(det_window, text="SPOJ Pwd:").grid(row=6,column=1,padx=(60,10),pady=(10,10))
    entryspojp=Entry(det_window,textvariable=pwd_spoj).grid(row=6,column=2,padx=(60,10),pady=(10,10))
    # details_["spoj"]=id_spoj.get()+' '+pwd_spoj.get()

    sbt=Button(det_window,text="Submit",command=lambda:add_user(name_=usr.get(),details_=details_,wind=det_window,id_cf=id_cf,pwd_cf=pwd_cf,id_cc=id_cc,pwd_cc=pwd_cc,id_spoj=id_spoj,pwd_spoj=pwd_spoj),width=15).grid(row=9,column=2,padx=(40,0),pady=(20,0))

def setup():
    global usernames
    global USER
    global users_det
    global path_to_users
    path_to_users = os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','users')
    with open(str(path_to_users+'/users.pickle'),"rb") as fr:
        users_det=pickle.load(fr)
    usernames=dict.fromkeys(users_det)
    
    main_window.title("Login automation")
    # login_window.style=Style()
    # login_window.style.theme_use("default")
    
    # login_button=Button(main_window,text="Login",command=login_fun,width=15,height=2).grid(row=2,column=2,sticky=S,padx=(30,15),pady=(20,20))
    
    # signup_button=Button(main_window,text="SignUp",command=signup_fun,width=15,height=2).grid(row=2,column=5,sticky=S,padx=(15,30),pady=(20,20))
    login_button=Button(main_window,text="Login",command=login_fun,width=15,height=2).pack(side="left",padx=(30,10),pady=10)
    
    signup_button=Button(main_window,text="SignUp",command=signup_fun,width=15,height=2).pack(side="right",pady=10,padx=(10,30))

    main_window.geometry("320x90")
    main_window.mainloop()

    return AUTH, NEW_USR, USER
    # if AUTH:
    #     return True,USER
    # else:
    #     return False,USER
def isAuth():
    return setup()
# setup()

def show_failed_status(what):
    failed_window = Tk()
    failed_window.title('Status')
    failed_window.geometry('200x80')
    Label(failed_window,text=str('Sorry! '+what+' Failed')).pack(padx=(10,10),pady=(10,5))
    closebtn = Button(failed_window,text='Close',command=failed_window.destroy,width=12).pack(padx=(10,10),pady=(5,10))
    failed_window.mainloop()

def show_success_status(what):
    success_window = Tk()
    success_window.title('Status')
    success_window.geometry('200x80')
    Label(success_window,text=str('Congrats! '+what+' Successful')).pack(padx=(10,10),pady=(10,5))
    closebtn = Button(success_window,text='Close',command=success_window.destroy,width=12).pack(padx=(10,10),pady=(5,10))
    success_window.mainloop()

def show_sites(usrname, det):
    # site_window = Tk()
    # site_window.title('Sites')
    # site_window.geometry('500x300')
    # namelbl = Label(site_window,text=usrname).grid(row=1,column=1,padx=(10,10),pady=(10,10))
    # Button(site_window,text='Logout',command=site_window.destroy).grid(row=1,column=2,padx=(30,10),pady=(10,10))
    # site_window.mainloop()
    path_to_logo = os.path.dirname(os.path.abspath(__file__))
    site_window = Tk()
    site_window.title('Sites')
    site_window.geometry('400x140')
    namelbl = Label(site_window, text=usrname).grid(row=0, column=0, padx=(0, 0), pady=(10, 10))
    Button(site_window, text='Logout', command=site_window.destroy).grid(row=0, column=3, padx=(0, 0), pady=(10, 10))
    # codeforces
    photo = PhotoImage(file=str(path_to_logo+'/codeforces.png'))
    photoimage = photo.subsample(3, 3)
    Button(site_window, text='CodeForces', image=photoimage, compound=LEFT,command=lambda:open_sites.openCF(det['codeforces'])).grid(row=2, column=0, padx=(0, 0),pady=(10, 10))
    # codeChef
    photo1 = PhotoImage(file=str(path_to_logo+'/logocodechef.png'))
    photoimage1 = photo1.subsample(3, 3)
    Button(site_window, text="Codechef", image=photoimage1, padx=8, compound=LEFT,command=lambda:open_sites.openCC(det['codechef'])).grid(row=2, column=1, padx=(0, 0),pady=(10, 10))
    # spoj
    photo3 = PhotoImage(file=str(path_to_logo+'/logospoj.png'))
    photoimage3 = photo3.subsample(3, 3)
    Button(site_window, text="SPOJ", image=photoimage3, padx=15, compound=LEFT,command=lambda:open_sites.openSPOJ(det['spoj'])).grid(row=2, column=3, padx=(0, 0),pady=(10, 10))
    site_window.mainloop()