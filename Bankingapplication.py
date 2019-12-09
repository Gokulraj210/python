import os
accountName = ''
accountId = ''
balance = 0
previousTransaction = 0

def cls():
    os.system("clear")
    
def main(cname, cid,):
    accountName = "cname"
    accountId = "cid"
    showMenu()

def deposit(amount):
    global balance, previousTransaction
    balance += amount
    previousTransaction = amount

def withdraw(amount):
    global balance, previousTransaction
    balance = balance - amount
    previousTransaction = -amount

def getPreviousTransaction():
    if previousTransaction > 0:
        print('You deposit: '), previousTransaction
    elif previousTransaction < 0:
        print('You withdraw: '), previousTransaction
    else:
        print('There is no transaction.')

def showMenu():
    print('--------------------------------------')
    print('FUNDLESS BANK OF INDIA')
    print('--------------------------------------')
    print('A. accountName')
    print('B. accountId')
    print('C. Check Balance')
    print('D. Deposit')
    print('E. Withdraw')
    print('F. Previous Transaction')
    print('G. Exit')
    print('--------------------------------------')
    option = ''
    amount = 0

    while option != 'c':
        option = input('Select an option:')
        if option == 'a':
            print('Your balance is: '), balance
        elif option == 'b':
            try:
                amount = int(input('Enter amount of deposit:'))
                deposit(amount)
            except ValueError:
                print('Not a valid number!')
        elif option == 'c':
            try:
                amount = int(input('Enter amount of withdraw:'))
                withdraw(amount)
            except ValueError:
                print('Not a valid number!')
        elif option == 'd':
            getPreviousTransaction()
        elif option == 'e':
            print('******************')
        else:
            print('Option invalid! Please try again!')

    print('Thank you for using our service!')

main("Raj","xyz-001");
