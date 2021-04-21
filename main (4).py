import random
class Atm(object):
    def __init__(self, balance, accNo):
        #self.cashWithdrawal = cashWithdrawal
        self.balance = balance
        self.accNo = accNo
        #self.ongoingLoan = ongoingLoan

    def withdrawal(self, amount):
        newAmount = int(self.balance) - amount
        print ("remaining balance: " +  str(newAmount))
    def checkBalance(self):
        balance = self.balance
        print("Rs." + " " +  " " +  "balance is available")

def main():
    accountNo = input("enter your account number: ")
    balance = input("enter your balance: ")
    newUser = Atm(balance, accountNo)
    print("Choose your activity: ")
    print("1: balance, 2: wthdrawal")
    activity = int(input("enter the activity number: "))
    if activity == 1: 
        newUser.checkBalance()
    elif activity == 2: 
        amount = int(input("enter the amount to be withdrawed: "))
        newUser.withdrawal(amount)

    else: 
        print("no such activity found")

if __name__ == "__main__": 
    main()
