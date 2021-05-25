#covaxine = view


import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="vaccine"
)

mycursor = mydb.cursor()


#mycursor.execute("select * from covaxin where vlocation='kop'")
#for val in mycursor:
    #print(val)
#query="select * from covaxin where name='xyz'"
#query="select * from covaxin order by name desc"
query="update covaxin set name='mrf' where id=4"
mycursor.execute(query)
mydb.commit()
joinquery="select v1.name,adhar_no, \
            vlocation,whichdose from slot s1 \
            inner join covaxinnew v1 on s1.name=v1.name"
mycursor.execute(joinquery)
for val in mycursor:
    print(val)


