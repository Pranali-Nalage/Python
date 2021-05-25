import mysql.connector  # import liberries of mysql

mydb = mysql.connector.connect(
  host="192.168.56.1",  #localhost
  user="root",
  password="root",
  database="vaccine"
)

mycursor = mydb.cursor()



#mycursor.execute("create table covaxin(id int(30),name varchar(30),adhar_no varchar(200),vlocation varchar(200))")
#mycursor.execute("describe covaxin")
mycursor.execute("insert into covaxin values (1,'abc','123rty','Kop')")
mycursor.execute("insert into covaxin values (2,'pqr','45tyu','mum')")
mycursor.execute("insert into covaxin values (3,'kys','173rty','pun')")
mycursor.execute("insert into covaxin values (4,'xyz','83rty','kar')")
mycursor.execute("insert into covaxin values (5,'tyr','703rty','tam')")

mydb.commit()
#for tblname in mycursor:
#    print(tblname)

#for des in mycursor:
#    print(des)

print(mycursor.rowcount)