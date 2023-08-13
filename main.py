import pyodbc

# Open database initially
conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                    "Server=.\SQLEXPRESS;"
                    "Database=POSDEMO;"
                    "Trusted_Connection=yes;", autocommit=True)
def e1():
    # Lists customer
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM custmast')
    for row in cursor:
        print('row = %r' % (row,))
    print('=============================================')

def e2():
    # New customer
    custnum = input('Customer Number: ')
    custname = input('Customer Name: ')
    address = input('Address: ')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO custmast(custnum, custname, address) VALUES (?, ?, ?)', custnum, custname, address)
    print('New record inserted')

def e3():
    # Delete customer
    custnum = input('Enter Customer Number: ')
    if (custnum != ''):
        cursor = conn.cursor()
        cursor.execute('DELETE FROM custmast WHERE custnum = ?', custnum)
        print('Deleted successfully.')

def e4():
    # Update customer
    id = input('Enter Row ID: ')
    if (id != ''):
        cursor = conn.cursor()
        cursor.execute('SELECT count(*) FROM custmast WHERE ID = ?', id)
        recordcount = cursor.fetchone()
        if (recordcount[0] > 0):
            custnum = input('Customer Number: ')
            custname = input('Customer Name: ')
            address = input('Address: ')
            cursor.execute('UPDATE custmast SET custnum = ?, custname = ?, address = ? WHERE ID = ?', custnum, custname, address, id)
            print('Customer %s was updated successfully' % id)
        else:
            print('Customer not exist.')

def e5():
    # Clear customer database
    ans = input('Are you sure to clear all customer? Enter (YES/NO):')
    if (ans == 'YES'):
        cursor = conn.cursor()
        cursor.execute('TRUNCATE TABLE custmast')
        print('Succesfully cleared')
    else:
        print('Action was cancelled')


def mainMenu():
    # print("\033c", end='')
    # Show menu selection
    print('=============================================')
    print("SELECT A OPERATION")
    print("")
    print("e1 - Lists Customer")
    print("e2 - New Customer")
    print("e3 - Delete Customer ")
    print("e4 - Update Customer")
    print("e5 - Clear Customer")
    print("x - Exit")
    print("")
    # Loop
    done = False
    while not done:
        selection = input("Enter a choice: ")
        if selection == "e1":
            e1()
        elif selection == "e2":
            e2()
        elif selection == "e3":
            e3()
        elif selection == "e4":
            e4()
        elif selection == "e5":
            e5()
        elif selection == "x":
            print("Goodbye!!!!")
            done = True
            exit()
        else:
            print("Invalid choice. Try again.")
        mainMenu()
mainMenu()



