import mysql.connector
mydb=mysql.connector.connect (
host="localhost",
user="root",
password="root",
database="bank"
)
mycursor=mydb.cursor()
#mycursor.execute("create database bank")
#for dbname in mycursor:
#    print(dbname)
#mycursor.execute("use bank")
#for dbname in mycursor:
#   print(dbname)
#mycursor.execute("create table userdetails (id int(30),name varchar(30),age int(30),address varchar(30))")
#for tblname in mycursor:
#    print(tblnam)
mycursor.execute("insert into userdetails values(%s,%s,%s,%s)")
for val in mycursor:
    print(val)
