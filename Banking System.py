import pymysql
connection = pymysql.connect (host='localhost', user='root', password='Mouli@33', db='CUSTOMERDB', port=3306)
c = connection.cursor()


def create_account():
    account_no = eval (input('Enter Account Number: '))
    name = input('Enter Account Holder Name: ')
    c.execute("insert into customers values (%s, %s, %s)", (account_no, name, 0.00))
    connection.commit()
    print (f'Account is created for {name} with account number: {account_no}')


def deposit_amount():
    account_no=eval(input('Enter Account Number: '))
    amount = float(input('Enter Amount to Deposit: '))
    if amount <= 0:
        print('Please deposit amount should be greater then 0')
        return
    c.execute("update customers set balance = balance + %s where account_no = %s", (amount, account_no))
    if c.rowcount == 0:
        print("Account not found")
    else:
        connection.commit()
        print(f'{amount} deposited successfully!!!')

def withdraw_amount():
    account_no = eval(input('Enter Account Number: '))
    name = input('Enter Account Holder Name: ')

    amount = float(input('Enter Amount to withdraw: '))
    
    c.execute("select balance from customers where account_no = %s", account_no)
    result = c.fetchone()
    
    if not result:
        print('Account is found')
        return
    balance = result [0]
    
    if amount > balance:
        print('Insufficient Balance!!!')
        return
    
    c.execute("update customers set balance = balance - %s where account_no = %s", (amount, account_no))
    connection.commit()
    print("%s withdrawn successfully",amount)


def check_balance():
    account_no = eval(input('Enter Account Number: '))
    c.execute("select name, balance from customers where account_no=%s", account_no)
    result = c.fetchone()

    if not result:
        print('Account is found')
    else:
        print (f"Name: {result[0]}, Balance:{result[1]}")    

     

    
def main():
    while True:
        options ="""
1. Create Account
2. Deposit Amount
3. Withdraw Amount
4. Check Balance
5. Exit
 """
        print('*Bank Of Baroda*')
        print (options)
        option = int(input('Enter Your Choice (1-5):'))
        if option == 1:
            create_account()
        elif option == 2:
            deposit_amount()
        elif option == 3:
            withdraw_amount()
        elif option == 4:
            check_balance ()
        elif option == 5:
            print('Thank You for banking with us')
            break
        else:
            print('Invalid Choice, Please Try Again between 1 to 5')



main()
