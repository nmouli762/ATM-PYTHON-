import pymysql
connection = pymysql.connect(host='localhost', port=3306,db='sims', user='root', password='Mouli@33', charset='utf8')
c = connection.cursor()
#to save data in table studets

def creating_student():
    sid = int(input('Enter Student ID: '))
    sname = input('Enter Student Name: ')
    age = int(input('Enter Student Age: '))
    course = input('Enter Student Course: ')
    mobile = int(input('Enter Mobile Number: '))
    emailid = input('Enter Email ID: ')
    
    c.execute("insert into students values (%s, %s, %s,%s, %s, %s)", (sid, sname, age, course, mobile, emailid))
    connection.commit()
    print('Student Data Added Successfully!!!')

def reading_students():
    c.execute('select * from students')
    data=c.fetchall()  #fetchone() #fetchmany(3) #fetchall()
    #print(data)-ans in tuple of tuples forn -((),(),()) or

    for i in data:
        print(i)

def updating_student():
    sno = int(input('Enter Student Number: '))
    c.execute("select*from students")
    data=c.fetchall()
    snos = []
    for i in data:
        snos.append(i[0])
    if sno in snos:
        sname = input('Enter Student Name: ')
        age = int(input('Enter Student Age: '))
        course = input('Enter Student Course:')
        mobile = int(input('Enter Mobile Number: '))
        emailid = input('Enter Email ID: ')
        c.execute("UPDATE students SET name=%s,age=%s,course=%s,mobile=%s,email=%s where id= %s",
                  (sname, age, course, mobile, emailid, sno))
        connection.commit()
        print('Data Modified Successfully!!!!')
    
    else:
       print('Invalid Student ID')

def deleting_student():
    sno = int(input('Enter Student Number: '))
    c.execute("select * from students")
    data = c.fetchall()
    snos = []
    for i in data:
        snos.append(i[0])
    if sno in snos:
        c.execute("delete from students where id = %s", (sno))
        connection.commit()
        print("Student Data Deleted Successfully")
       
    else:
        print('Invalid Student ID')

        


def menu():
    while True: #to reexcute again and again
        print('*** Students Information Management Systems ***')
        print('1. Adding Student Data')
        print('2. Reading Students Data')
        print('3. Updating Student Data')
        print('4. Deleting Student Data')
        print('5. Exit')
        
        choice=int(input('Please choose your choice (1-5):'))

        if choice == 1:
            creating_student()
        elif choice == 2:
            reading_students()
        elif choice == 3:
            updating_student()
        elif choice == 4:
            deleting_student()
        elif choice == 5:
            print('You are exiting...Bye Bye...')
            break
        else:
            print('Invalid Choice!!!Please Enter 1 to 5')
            

menu()
