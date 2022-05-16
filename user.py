from tkinter.font import names
from unicodedata import name


class user:
    def __init__(self,name,email_address):
        self.name=name
        self.email=email_address
        self.account_balance=0
    
    def make_depost(self,amount):
        print(self.name,"account before deposit",self.account_balance)
        self.account_balance+=amount
        print(self.name,"account after deposit",self.account_balance)
        return self
    def make_withdrawal(self,amount):
        print(self.name,"account before withdrawal",self.account_balance)
        self.account_balance-=amount
        print(self.name,"account after withdrawal",self.account_balance)
        return self
    def display_user_balance(self):
        print("User:",self.name,"Balance:",self.account_balance)
        return self
    def transfer_money(self,other_user,amount):
        print(self.name,"account before transfer",self.account_balance)
        self.account_balance-=amount
        print(self.name,"account after transfer",self.account_balance)
        print(other_user.name,"account before transfer",other_user.account_balance)
        other_user.account_balance+=amount
        print(other_user.name,"account after transfer",other_user.account_balance)
        return self

michael=user("Machael","michael@michael.com")
rim=user("Rim","rim@rim.com")
anis=user("Anis","anis@anis.com")
michael.make_depost(120).make_depost(520).make_depost(20).make_withdrawal(200).display_user_balance()
rim.make_depost(450).make_depost(630).make_withdrawal(120).make_withdrawal(205).display_user_balance()


anis.make_depost(580).make_withdrawal(400).make_withdrawal(400).make_withdrawal(125).make_withdrawal(614).display_user_balance()

michael.transfer_money(anis,458).display_user_balance()
anis.display_user_balance()


    
