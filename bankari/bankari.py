# Bank Program

import sqlite3
import os.path

# Gets the directory path where the db is located and links the program to the db
dirPath = os.path.dirname(os.path.abspath(__file__))
db = os.path.join(dirPath, "bankari.db")
conn = sqlite3.connect(db)
source = conn.execute(''' SELECT user, checking, savings FROM accounts ''')

# Startup Function
def start(checking, savings):
    print('\nHello ' + user + '! What would you like to do today?\n')
    print('Balance in Checking: $' + str(checking))
    print('Balance in Savings: $' + str(savings) + '\n')
    
    # Runs Banking Interface
    actions(checking, savings)

# Deposit Function
def deposit(checking, savings):
    account = input('Would you like to deposit in your Checking or Savings account: ')
    amount = input('How much are you looking to deposit into your ' + account + ' today: ')
    
    # Checks for account deposit location
    if account == 'Checking' or account == 'checking':
        checking = float(checking) + float(amount)
        checking = "{:.2f}".format(checking)
        
        # Updates db
        conn.execute("UPDATE accounts SET checking = ?", [checking])
        conn.commit()
    else:
        savings = float(savings) + float(amount)
        savings = "{:.2f}".format(savings)
        
        # Updates db
        conn.execute("UPDATE accounts SET savings = ?", [savings])
        conn.commit()
    start(checking, savings)

# Withdraw Function
def withdraw(checking, savings):
    account = input('Would you like to withdraw from your Checking or Savings account: ')
    amount = input('How much would you like to withdraw from your ' + account + ' today: ')

    if account == 'Checking' or account == 'checking':
        checking = float(checking) - float(amount)
        print('You withdrew $' + str(amount) + '. Your new balance in your Checking account is $' + "{:.2f}".format(checking) + '.')
        checking = "{:.2f}".format(checking)
        
        # Updates db
        conn.execute("UPDATE accounts SET checking = ?", [checking])
        conn.commit()
    else:
        savings = float(savings) - float(amount)
        print('You withdrew $' + str(amount) + '. Your new balance in your Savings account is $' + "{:.2f}".format(savings) + '.')
        savings = "{:.2f}".format(savings)
        
        # Updates db
        conn.execute("UPDATE accounts SET savings = ?", [savings])
        conn.commit()
    start(checking, savings)

# Transfer Function
def transfer(checking, savings):
    route = input('From which account would you like to transfer your funds:\n\n(1) Checking to Savings\n(2) Savings to Checking\n\n')
    
    if route == '1':
        print('You selected to transfer from Checking to Savings.')
        amount = input('How much would you like to transfer today: ')
        checking = float(checking) - float(amount)
        savings = float(savings) + float(amount)
        checking = "{:.2f}".format(checking)
        savings = "{:.2f}".format(savings)
        
        # Updates db
        conn.execute("UPDATE accounts SET checking = ?, savings = ?", [checking, savings])
        conn.commit()
    else:
        print('You selected to transfer from Savings to Checking.')
        amount = input('How much would you like to transfer today: ')
        savings = float(savings) - float(amount)
        checking = float(checking) + float(amount)
        checking = "{:.2f}".format(checking)
        savings = "{:.2f}".format(savings)
        
        # Updates db
        conn.execute("UPDATE accounts SET checking = ?, savings = ?", [checking, savings])
        conn.commit()
    start(checking, savings)

# Exit Function
def exit():
    print('Thank you for banking with us today.')
    conn.close()

# Interface Actions Function
def actions(checking, savings):
    action = input('(1) Deposit into Checking/Savings\n(2) Withdraw from Checking/Savings \n(3) Transfer Funds\n(4) Sign Out\n\n')

    # Deposit Checking/Savings
    if action == '1':        
        deposit(checking, savings)

    # Withdraw Checking/Savings
    elif action == '2':
        withdraw(checking, savings)

    # Transfer Funds
    elif action == '3':
        transfer(checking, savings)

    # Exit
    else:
        exit()

# Program Spin Up
# Pulls in data from db, formats and assigns to variables
for row in source:
    checking = "{:.2f}".format(row[1])
    savings = "{:.2f}".format(row[2])

user = input('Please enter your username: ')

start(checking, savings)