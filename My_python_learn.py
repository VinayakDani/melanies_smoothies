# abc.py
"'" Git Push 
1. Local repository setup 
 local path
 git init    --> create local git repo

2. add remote repo to git repo (Clone remote repo to local repo)
in cmd 
$ git remote add origin gitcloneurl

$ git status

$ git add -A   --> add all file from local to got repo

$ git commit -m "comment"   --> local save changes.

-- Git Push the code
$ git push origin master 
$ git status   --> 


  



import pip


class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("RS.", amount, "was debited")
        print("total balance = ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("RS.", amount, "was credited")
        print("total balance =", self.get_balance())

    def get_balance(self):
        return self.balance
    
acc1 = Account(10000,12345)
acc1.debit(2000)
acc1.credit(5000)


import pip
pip install ipython
