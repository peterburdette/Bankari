import sqlite3
import os.path

dirPath = os.path.dirname(os.path.abspath(__file__))
db = os.path.join(dirPath, "bank.db")
conn = sqlite3.connect(db)
source = conn.execute(''' SELECT user, checking, savings FROM accounts ''')
print("Opened database successfully")

# conn.execute('''CREATE TABLE COMPANY
#          (ID INT PRIMARY KEY     NOT NULL,
#          NAME           TEXT    NOT NULL,
#          AGE            INT     NOT NULL,
#          ADDRESS        CHAR(50),
#          SALARY         REAL);''')

test = conn.execute(''' SELECT user, checking, savings FROM accounts ''')

for row in test:
    one = "user = ", row[0]
    two = "checking = ", row[1]
    three = "savings = ", row[2]

print(one)
print(two)
print(three)
# record = test.fetchone()
# print(record)

conn.close()