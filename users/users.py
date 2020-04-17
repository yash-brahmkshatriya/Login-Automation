import pickle

users={
    "yash":{
        "codeforces":'noob2831 cfpwd',
        "codechef":'noob2831 ccpwd',
        "spoj":'yash_31 spojpwd'
    },
    "keyur":{
        "codeforces":'kcfid kcfpwd',
        "codechef":'kccid kccpwd',
        "spoj":'kspojid kspojpwd'
    }
}

def add_user(name_,details_):
    users[name_]=details_
    with open("C:/Users/Dilip/Yash Codes/Python/Login_Automation/users/users.pickle","wb") as fw:
        pickle.dump(users,fw)
with open("C:/Users/Dilip/Yash Codes/Python/Login_Automation/users/users.pickle","wb") as fw:
    pickle.dump(users,fw)