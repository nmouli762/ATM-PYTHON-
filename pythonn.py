

'''print("hello")
'''

'''a=3
b=2
c=a+b
print(c)'''

'''import re
name=input('enter:')      
m=re.fullmatch('python',name)
if m==None:
    print('not matching')
else:
    print('matching')'''




'''import pymysql
connection= pymysql.connect(host ="localhost",user ="root",password ="123456",db="pymydb")
c=connection.cursor()
c.execute("create table empdata(eno int,ename varchar(30),salary int,location varchar(30));")
connection.commit()
'''

'''data = 
Mr. Kumar has learned Python Language from NTH Institute and placed in TCS Company with 20000 salary,
Mr. Suresh has learned Java Language from ABC Institute and placed in HCL Company with 30000 salary,
Ms. Kavya has learned C Language from NTH Institute and placed in Wipro Company with 25000 salary,
Mrs. Navya has learned C++ Language from XYZ Institute and placed in TCS Company with 10000 salary,
Ms. Bavya has learned MySQL Database from NTH Institute and placed in CTS Company with 30000 salary,
Mrs. Sravya has learned Oracle Database from ABC Institute and placed in Wipro Company with 9000 salary
'''
''


'''
class myclass:
     ename='mouli'
     study='bsc'
     def college(self):
         print('ysrhu')
     def university(self):
        print('YSRHU')


e1=myclass()

print(e1.ename)'''


'''
def increment(sal):
     sal=sal+sal *15/100
     return sal
sal=increment(5000)
print('incremented sal =%.2f' %sal)'''
'''
f=open('myfile','w')

a,b=[int(x) for x in input("enter two nums:").split()]

c=a/b

f.write("writing {c} into myfile" )


print("file closed")
'''

''' ================================python project=============================='''

'''import pymysql
import string
connection = pymysql.connect(host='localhost', port=3306,db='mouli', user='root', password='Mouli@33', charset='utf8')
c = connection.cursor()
c.execute('select * from customer')
data=c.fetchall()
existing_users = []

for i in data:
    existing_users.append(i[1])
while True:
    reg_user=input('Enter Username: ')
#pythonsai

    if reg_user in existing_users:
     print('Already this name is taken by another, please enter new username')
     continue
    else:
        name=input('Enter Your Name: ')
        while True:
            pwd1=input('Enter Password: ')
            pwd2=input('Enter Confirm Password: ')
        #compare pwdl, pwd2
            if pwd1!= pwd2:
                print('Passwords are mismatched')
                continue
            elif len(pwd1)<8:
                print('Password must have min 8 charecters')
                continue
            
            elif len([i for i in pwd1 if i in string.ascii_lowercase]) == 0: 
                print('Password must have atleast one lower case character' )
                continue
            elif len([i for i in pwd1 if i in string.ascii_uppercase]) == 0:
                print('Password must have atleast one upper case character' )
                continue
            elif len([i for i in pwd1 if i in string.digits]) == 0:
                print('Password must have atleast one digit')
                continue
            elif len([i for i in pwd1 if i in string.punctuation]) == 0:
                print('Password must have atleast one special character' )
                continue
            else:
                email=input('Enter Email Id: ')
                
                mobile=eval(input('Enter Mobile Number: '))

                c.execute("insert into customer values (%s, %s, %s, %s, %s, %s)", (name, reg_user, pwd1, pwd2, email,mobile))
                connection.commit()
                print("your account created sucessfully")
            break   
        break
'''



''' for login
import pymysql
connection = pymysql.connect(host='localhost', port=3306,db='mouli', user='root', password='Mouli@33', charset='utf8')
c = connection.cursor()
c.execute('select * from customer')
data=c.fetchall()
login_user = input('Enter Username: ') 
login_pwd = input('Enter Password: ')
for i in data:
    if login_user == i [1] and login_pwd == i [2]:
        print('Login Sucess')
        found = True
        break
    else:
        print('Login Failed')
        break
'''



'''
import pymysql
import string

connection = pymysql.connect(
    host='localhost',
    port=3306,
    db='mouli',
    user='root',
    password='Mouli@33',
    charset='utf8'
)
c = connection.cursor()
c.execute('select * from customer')
data = c.fetchall()

existing_users = []
existing_emails = []
existing_mobiles = []
for i in data:
    existing_users.append(i)    # Username, assuming index 1
    existing_emails.append(i)   # Email, assuming index 4
    existing_mobiles.append(str(i[5]).strip())                            # existing_mobiles.append(str(i)) # Mobile, assuming index 5, store as string for comparison

while True:
    reg_user = input('Enter Username: ')
    if reg_user in existing_users:
        print('Already this name is taken by another, please enter new username')
        continue
    else:
        name = input('Enter Your Name: ')
        
        while True:
            email = input('Enter Email Id: ')
            if email in existing_emails:
                print('Email already registered, please use a different Email Id')
                continue
            break
        
        while True:
            mobile = input('Enter Mobile Number: ')
            if mobile in existing_mobiles:
                print('Mobile number already registered, please use a different Mobile Number')
                continue
            # Optionally, add extra check: isdigit() and length validation
            if not mobile.isdigit() or len(mobile) != 10:
                print('Please enter a valid 10-digit mobile number')
                continue
            break
        
        while True:
            pwd1 = input('Enter Password: ')
            pwd2 = input('Enter Confirm Password: ')
            
            if pwd1 != pwd2:
                print('Passwords are mismatched')
                continue
            elif len(pwd1) < 8:
                print('Password must have min 8 characters')
                continue
            elif len([i for i in pwd1 if i in string.ascii_lowercase]) == 0:
                print('Password must have at least one lower case character')
                continue
            elif len([i for i in pwd1 if i in string.ascii_uppercase]) == 0:
                print('Password must have at least one upper case character')
                continue
            elif len([i for i in pwd1 if i in string.digits]) == 0:
                print('Password must have at least one digit')
                continue
            elif len([i for i in pwd1 if i in string.punctuation]) == 0:
                print('Password must have at least one special character')
                continue
            else:
                # On success, insert the values
                c.execute(
                    "INSERT INTO customer VALUES (%s, %s, %s, %s, %s, %s)",
                    (name, reg_user, pwd1, pwd2, email, mobile)
                )
                connection.commit()
                print("Your account created successfully")
                # Optionally, update the lists so another registration in the same run checks latest data
                existing_users.append(reg_user)
                existing_emails.append(email)
                existing_mobiles.append(mobile)
                break
        break
'''


















'''import time

def squares(lst):
    newLst = []
    start = time.time()
    for i in lst:
        newLst.append(i**2)
    end = time.time()
    duration = end - start
    print('The Function has taken', duration, 'seconds')
    print(newLst)

def cubes(lst):
    newLst = []
    for i in lst:
        newLst.append(i**3)
    print(newLst)

lst = range(1, 10001)
squares(lst)
cubes(lst)
'''



'''
x = 100
while x>=100 and x <= 200:
    if x % 2 == 0:
        print(x)
    x += 1
'''
'''str='Hello'
n=len(str)
for i in range(n):
    print(str[i])
'''



'''
import calendar as c
import datetime
dt = datetime.datetime.now()
current_year = dt.year
current_month = dt.month
current_day = dt.day
current_date = dt.date
x = c.weekday(current_year, current_month,current_day)
print(x)

'''

'''import random

def generate_account_number(existing_numbers):
    """
    Generates a unique 12-digit account number.
    existing_numbers: a set of existing account numbers for uniqueness check.
    Returns: a unique 12-digit account number as a string.
    """
    while True:
        account_no = str(random.randint(10**11, (10**12) - 1))  # create a 12-digit number
        if account_no not in existing_numbers:
            existing_numbers.add(account_no)
            return account_no



used_accounts = {"123456789012", "987654321098"}  # already-used accounts
new_account = generate_account_number(used_accounts)

print("New Account Number:", new_account)'''


'''
def run_calculator_interaction():
    num1=eval(input("enter the first value:"))
    num2=eval(input("enter the second value:"))
    print("1. Addition,2. Subtraction,3. Multiplication,4. Exit")
    
    choice = int(input('Enter Your Choice: '))
    while choice<5:
       if choice==1:
           print(num1+num2)
       elif choice==2:
           print(num1-num2)
       elif choice==3:
           print(num1*num2)
       else:
           print('invalid response')      

run_calculator_interaction()'''

'''
def run_calculator_interaction():
    num1 = float(input("Enter the first value: "))
    num2 = float(input("Enter the second value: "))

    while True:
        print("\nEnter Your Choice:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Exit")

        choice = int(input("Choice: "))

        if choice == 1:
            print("Result:", num1 + num2)
            return choice
        elif choice == 2:
            print("Result:", num1 - num2)
            return choice
        elif choice == 3:
            print("Result:", num1 * num2)
            return choice
        elif choice == 4:
            print("Exiting...")
            return choice
        else:
            print("Invalid response, please choose again.")

run_calculator_interaction()
'''




'''
age = int(input("Enter your age: "))
is_student = input("Are you a student? (yes/no): ").lower()
# Determine ticket price
if age < 5:
    price = "Free"
elif age <= 12:
    price = "$10"
elif age <= 17:
    if is_student == 'yes':
        price = "$12"
    else:
        price = "$15"
elif age <= 64:
    if is_student == 'yes':
        price = "$18"
    else:
        price = "$25"
else:
    price = "$20"
print("Ticket Price:", price)
'''
'''
def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)
print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7),
)
'''




   
'''
def f(x):
    if x > 0:
        print("Only printed when x is positive; x =", x)
        print("Also only printed when x is positive; x =", x)
    print("Always printed, regardless of x's value; x =", x)

f(1)
f(0)
'''

'''
def estimate_average_slot_payout(n_runs):
    """Run the slot machine n_runs times and return the average net profit per run.
    Example calls (note that return value is nondeterministic!):
    >>> estimate_average_slot_payout(1)
    -1
    >>> estimate_average_slot_payout(1)
    0.5
    """
    payouts = [play_slot_machine() - 1 for i in range(n_runs)]
    avg_payout = sum(payouts) / n_runs
    return avg_payout

    estimate_average_slot_payout(10000000)
'''
'''
print("hello")
print("world")
print("hello", end='')
print("pluto", end='')
'''
'''
datestr = '1956-01-31'
year, month, day = datestr.split('-')
print(datestr.split('-'))
'''
'''O(n^2)
lst=[2,6,9,11,34,67,45,76,14]
sum = 20
n=len(lst)

for i in range(n):
    isFound=False
    for j in range(i+1,n):
        if (lst[i]+lst[j]==sum):
            print(lst[i],lst[j])
            isFound=True
            break;

    if(isFound):
        break;
'''
'''
lst=[2,6,9,11,34,67,45,76,14]
sum = 20
n=len(lst)
s=set()

for i in range(n):
    if((sum-lst[i]) in s):
        print(lst[i],sum-lst[i])
        
    else:
        s.add(lst[i])

i=0
set=()

i=1
s=(2,14,9
'''

for num in range(1,101):
    if num>1:
        for i in range(2, num):
            if num%i==0:
                break
            else:
                print(num)
                break

            
        
    

































