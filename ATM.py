import pymysql
from datetime import datetime 

connection = pymysql.connect(host='localhost', user='root', password='Mouli@33', database='atmdb',port=3306)
cursor = connection.cursor()

def login_account():
    attempts=0
    while attempts < 3:
        acc_no = int(input('Enter Your Account Number: '))
        pin = int(input('Enter Your PIN:'))
        cursor.execute("SELECT * from accounts where account_no=%s and pin=%s", (acc_no,pin))
        account = cursor.fetchone()
        if account:
            print (f"Welcome {account [1]}!")
            return acc_no
        else:
            attempts=attempts + 1
            print (f"Invalid Credentials, Attempts Left {3-attempts}")
    print('Too Many Invalid Attemps')
    return None

def update_balance(account_no, balance):
    cursor.execute("UPDATE accounts set balance = %s where account_no=%s", (balance, account_no))
    connection.commit()
    
def transaction_record (account_no, trans_type, amount, target_account=None):
    cursor.execute ("INSERT INTO transactions (account_no, trans_type, amount, target_account, trans_time) VALUES (%s,%s, %s,%s,%s)",
        (account_no, trans_type, amount, target_account,datetime.now()))
    connection.commit()

def show_mini_statement(account_no):
    cursor.execute("select balance from accounts where account_no =%s", (account_no,))
    balance = cursor.fetchall()[0]
    print (f"Current Balance: {balance}/-")
    cursor.execute("select trans_type, amount, target_account, trans_time from transactions where account_no=%s",(account_no,))
    trans = cursor.fetchall ()
    if not trans:
        print('No Transactions Yet')
    else:
        for i in trans [-1::-1]: 
            trans_type, amount, target,time=i
            if target:
                print(f"{trans_type} {amount}/---> {target} on {time}")
            else:
                 print(f"{trans_type} {amount}/---> {target} on {time}")
        

    
    
           
def atm_menu(account_no):
    daily_withdrawn=0
    while True:
        print('\n1.Check Balance\n2.Withdraw\n3.Deposit\n4.Transfer\n5.Transaction History\n6. Change PIN\n7.Exit')
        choice = eval(input('Choose Your Choice:'))
        cursor.execute("SELECT balance from accounts where account_no=%s", (account_no,))
        balance = cursor.fetchone()[0] 
        if choice == 1:
            print (f"Your Current Balance: {balance}")
        elif choice == 2:
            try:
                amount=eval(input("ENTER AMOUNT TO WITHDRAW:"))
                if amount<=0:
                    print('invalid amount')
                    continue
                elif amount > balance:
                    print('Insufficient Balance')
                elif daily_withdrawn+amount > 20000:
                    print('Daily Limit exceeded')
                elif amount%100 != 0:
                    print('Amount must be multiple of 100')
                else:
                    balance = balance-amount
                    daily_withdrawn = daily_withdrawn + amount
                    update_balance(account_no, balance)
                    transaction_record(account_no, "withdraw", amount)
                    print(f'withdrawn{amount}.New Balance:{balance}')
            except ValueError:
                print('invalid input')


        elif choice == 3:
            try:
                amount = eval(input('Enter Amount to Deposit: '))
                if amount <= 0:
                    print('A Invalid Amount')
                else:
                    balance = balance + amount 
                    update_balance(account_no, balance)
                    transaction_record(account_no, "deposit", amount)
                    print (f"Deposited {amount}/-. New Balance {balance}/-.")
            except ValueError:
                    print("A Invalid Input")
        elif choice == 4:
            target_acc = eval (input('Enter Target Account Number: '))
            if account_no == target_acc:
                print("You can not transfer money to your own account")
                continue
            cursor.execute("select balance from accounts where account_no=%s", (target_acc,))
            target_balance = cursor.fetchone()[0]
            if not target_balance:
                print("Target Account does not exist")
                continue
            try:
                amount = eval (input('Enter amount to transfer: '))
                if amount <= 0:
                    print("Invalid Amount")
                    continue
                else:
                    balance -= amount #balance = balance amount
                    target_balance+=amount #target_balance = target_balance + amount
                    update_balance (account_no, balance)  #updating my balance
                    update_balance (target_acc, target_balance) #updating my friend balance
                    transaction_record (account_no, "Transfer", amount, target_acc)
                    transaction_record (account_no, "Received", amount, account_no)
                    print(f"Transferred {amount}/- to {target_acc}. New Balance {balance}/-")
            except ValueError:
                print("Invalid Input")
        elif choice==5:
            show_mini_statement(account_no)

        elif choice==6:
            
            try:
                new_pin=eval(input("Enter New 4-Digit PIN: "))
                if len(str(new_pin)) == 4:
                    cursor.execute("UPDATE accounts set pin = %s where account_no=%s", (new_pin, account_no))
                    connection.commit()
                    print('PIN changed successfully!!!')
                else:
                    print("PIN should contains 4 digits")
            except ValueError:
                print('Invalid Format')
        elif choice == 7:
            print("Thank You For Using NTH Bank ATM, Byeee!!!!")
            break
        else:
            print("Invalid Choice")
            

            
def create_account():
    name = input('Enter Your Full Name: ')
    if not name:
        print("Name can not be empty")
        return None
    try:
        age=int(input("Enter Your Age: "))
        if age < 10:
            print("Minimum age is 10")
            return None
    except ValueError:
        print("Invalid Age")
        return None
    try:
        initial_deposit = float(input('Enter Initial Amount: '))
        if initial_deposit < 0:
            print("Deposit Amount cannot be negative")
            return None
    except ValueError:
        print("Invalid Amount")
        return None
    try:
        pin=input('Enter 4-Digit PIN: ')
        if not(pin.isdigit()and len(pin)==4):
            print("PIN must be 4 digits")
            return None
    except ValueError:
        print('PIN must be integer value')
        return None
    try:
        confirm_pin=input('Confirm your 4-Digit PIN: ')
        if pin!= confirm_pin:
            print('PINs do not match, Please try again')
            return None
    except ValueError:
        print("PIN must be integer value")
        return None
    cursor.execute ("SELECT max(account_no) from accounts")
    max_acc = cursor.fetchone() [0]

    account_no = (max_acc + 1) if max_acc else 1001
    cursor.execute("INSERT into accounts(account_no, name, age, pin, balance) values (%s, %s, %s, %s, %s)", (account_no, name, age, pin, initial_deposit))
    connection.commit()
    print(f"Account created succssfully! You account number is: {account_no}")

    return account_no


def main():
    while True:
        print('Welcome to NTH Bank ATM')
        print('\n1. Login to Account\n2. Create New Account\n3. Exit')
     
        try:
            choice = int(input('Enter Your Choice: '))
        except ValueError:
            print("Invalid Choice: not a number")
            continue

        if choice == 1:
            acc=login_account()
            if acc:
                atm_menu(acc) 
        elif choice == 2:
            create_account()
        elif choice == 3:
            print("Thank You For using NTH BANK ATM")
            break
        else:
            print('Invalid Choice')
            

main()


























    
