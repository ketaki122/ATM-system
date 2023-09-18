#!/usr/bin/env python
# coding: utf-8

# In[3]:


accname='ketaki'
pin=23
data={"name":accname,"Pin":pin}
print(data["name"])
    


# In[ ]:


class Atm:
    def __init__(self):
        self.accname='Ketaki'
        self.balance=10000
        self.pin=2000
        self.bank={"accountname":self.accname,"pin":self.pin,"balance":self.balance}
    def Pin(self):
        print()
        print("If you fail to put input your account will be blocked.")
        print()
        x=int(input("Enter your pin:")) 
        if self.pin==x:
            self.flag=1
            print("Account name:",self.bank["accountname"])
        else:
            print("Invalid input")
            self.flag=2
    def CheckBalance(self):
        print("Balance: ",self.bank["balance"])
    def Withdrawal(self):
        amt=int(input("Enter amount to be withdrawn:"))
        print("You have successfully withdrawn Rs.",amt)
        self.bank["balance"]=self.balance-amt
        print("Now current balance is:",self.bank["balance"])
    def deposit(self):
        amount=int(input("Enter amount to be deposited:"))
        self.bank["balance"]=self.balance+amount
        print("You have successfully deposited Rs.",amount)
        print("Now current balance is:",self.bank["balance"])
    def pingeneration(self):
        p=int(input("Enter your new pin:"))
        self.pin=p
        self.flag=1
        
        print("Pin changed successfully.")
print("***Welcome to Dhanlaxmi bank***")
def exit():
    print("Thankyou for using Dhanlaxmi ATM")
A=Atm()
def final():
    A.Pin()
    if A.flag==1:
        print("Choose operation:")
        print()
        print("1.Checkbalance,2.Withdrawal,3.Deposit,4.Pin generation")
        print()
        print("Enter the serial number of the operation:")
        o=int(input())
        if o==1:
            A.CheckBalance()
            print("Press 1 to continue and 2 to exit")
            s=int(input("Enter here:"))
        elif o==2:
            A.Withdrawal()
            print("Press 1 to continue and 2 to exit")
            s=int(input("Enter here:"))
        elif o==3:
            A.deposit()
            print("Press 1 to continue and 2 to exit")
            s=int(input("Enter here:"))
        elif o==4:
            A.pingeneration()
            final()
        else:
            print("Invalid operation")
            final()
        if s==1:
            final()
        else:
            exit()
    else:

        print("*Account blocked*")
        exit()        
final()       
            


# In[ ]:





# In[ ]:




