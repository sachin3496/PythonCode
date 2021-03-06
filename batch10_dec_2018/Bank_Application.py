#!/usr/bin/env python
# coding: utf-8

# <h1 style='color:red'>Bank Applications</h1>

# In[14]:

import json
f = open('bank1.db','r')
data = json.load(f)
f.close()
from getpass import getpass
from time import ctime

def update_file():
    f = open('bank1.db','w')
    json.dump(data,f)
    f.close()

def update_log(logdata,type_msg):
    f = open('bank_log.txt','a')
    time = ctime()
    msg=logdata
    type_msg = type_msg
    log = f"""{time}\t{msg}\t{type_msg}
    """
    f.write(log)

# In[15]:


def signup():
    print("\n\nWelcome to Signup Services ")
    uname = input("Username : ")
    password = getpass("password : ")
    bal = int(input("Enter current balance : "))
    email = input("Enter your Email Address : ")
    addr = input("Enter your Address  : ")
    ph_no = input("Enter your phone number : ")
    acc_nums = sorted(list(data.keys()))
    acc_no = int(acc_nums[-1]) + 1
    data[acc_no] = { 'username':uname,'password':password,'bal':bal,
                    'email':email,'ph_no':ph_no,'addr':addr }
    update_file()
    print("\n\nYour account Sucessfully Created")
    print(f"\n\n{acc_no} This is your Account Write it down somewhere very safe and do not share with any it will be used in login process with password \n\n")
    input("\n\nPress any key to coninue")
    login()


# In[16]:


def chk_bal(acc_no):
    print(f"\n\nWelcome user {data[acc_no]['username']} to Check Balance Service \n\n")
    print("Your Account number is : ",acc_no)
    for key,value in data[acc_no].items():
        print(f"{key} = {value}")
    choice(acc_no)


# In[30]:


def debit(acc_no):
    print(f"\n\nWelcome user {data[acc_no]['username']} to debit services\n\n")
    amount = int(input("Enter amount to be debited : "))
    
    if amount > data[acc_no]['bal'] : 
        print("Insufficient Account Balance")
        print(f"you only have {data[acc_no]['bal']} left in your account")
        choice(acc_no)
        update(f"{amount} debited from acc no {acc_no}","debit")
    else : 
        data[acc_no]['bal'] -= amount
        update_file()
        print(f"\n\nYour Account Sucessfully Debited with {amount}, Your Current Balance is {data[acc_no]['bal']}")
        choice(acc_no)


# In[26]:


def credit(acc_no):
    print(f"\n\nWelcome user {data[acc_no]['username']} to credit services\n\n")
    amount = int(input("Enter amount to be Credit : "))
    data[acc_no]['bal'] += amount
    update_file()
    print(f"\n\nYour Account Sucessfully Credited with {amount}, Your Current Balance is {data[acc_no]['bal']}")
    choice(acc_no)


# In[19]:


def choice(acc_no):
            print("\n\nChoose one of the service : ")
            print("\n1.Credit\n2.Debit\n3.Chk_Balance\n4.Logout")
            ch = int(input("Enter your Choice : "))
            if ch == 1 : 
                credit(acc_no)
            elif ch == 2 : 
                debit(acc_no)
            elif ch == 3 : 
                chk_bal(acc_no)
            elif ch == 4 :
                print(" Logging you out ")
                main()
            else : 
                print("Invalid Choice")
                choice(acc_no)
            


# In[20]:


def login():
    update_log('Login Process Initiated','General')
    print("\n\nWelcome to login services \n\n")
    acc_no = input("Enter your Account number : ").strip().lower()
    if acc_no in data.keys() :
        update_log(f'user with acc num {acc_no} trying to login','login_try') 
        from getpass import getpass
        password = getpass("Enter your Password : ")
        if password == data[acc_no]['password'] : 
            choice(acc_no)    
            update_log(f'user with acc num {acc_no} has logged into system','login')
        else : 
            print("\n\nInvalid Password Try Again\n\n")
            input("\nPress any key to login again ")
            login()
    else : 
        update_log('unauthorized access detected','warning')
        print("\nNo such Account Exists")
        print("\nPlease Signup\n")
        input("\n\nPress any key to go into main menu")
        main()
        


# In[24]:

import socket
def main():
    name = socket.gethostname()
    update_log(f"Application Started at machine {name}","General") 
    print("\n\nWelcome to Python Bank")
    print("\n\nChoose your Service : ")
    print("1.login\n2.signup\n3.Exit")
    ch = int(input("Enter your Choice : "))
    if ch == 1 : 
        login()
    elif ch == 2 : 
        signup()
    else : 
        print("\n\nThanks for using our Services")
        print("Exiting")
    


# In[32]:


main()


# In[ ]:




