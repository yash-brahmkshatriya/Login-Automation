import pickle

users={
    "yash":{
        "codeforces":'noob2831 codeforces@yahoo',
        "codechef":'noob2831 Code@yahoo31',
        "spoj":'yash_31 spoj@yash31'
    },
    "keyur":{
        "codeforces":'kcfid kcfpwd',
        "codechef":'kccid kccpwd',
        "spoj":'kspojid kspojpwd'
    },
    "chhaya":{
        "codeforces":'ccfid ccfpwd',
        "codechef":'cccid cccpwd',
        "spoj":'cspojid cspojpwd'
    },
    "dilip":{
        "codeforces":'dcfid dcfpwd',
        "codechef":'dccid dccpwd',
        "spoj":'dspojid dspojpwd'
    }
}

def add_user(name_,details_):
    users[name_]=details_
    with open("C:/Users/Dilip/Yash Codes/Python/Login_Automation/users/users.pickle","wb") as fw:
        pickle.dump(users,fw)
with open("C:/Users/Dilip/Yash Codes/Python/Login_Automation/users/users.pickle","wb") as fw:
    pickle.dump(users,fw)