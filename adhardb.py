import mysql.connector  # import liberries of mysql

mydb = mysql.connector.connect(
  host="192.168.56.1",  #localhost
  user="root",
  password="root",
  database="vaccine"
)

mycursor = mydb.cursor()

#################### creation of table
#mycursor.execute("create table slot(id int(20),name varchar(200),whichdose int(12))")
mycursor.execute("show tables")
for val in mycursor:
    print(val)
########################



slotid=input("Enter slot id=")
slotname=input("Enter user name=")
slotwhichdose=input("Which dose=")


query="insert into slot values(%s,%s,%s)"
val=(slotid,slotname,slotwhichdose)

mycursor.execute(query,val)
mydb.commit()