#write a program to calculate total marks 
mysub={"MySql":70,"Java":90,"Python":98,"VBA":67}
print("total subject addition :",sum(mysub.values()))


#replace values from set
mysub.update({"MySql":90})
print(mysub)

#write inheritance program(take a example related to CORONA virus)
class CORONA():
    def __init__(self):
        print("Corona Virus")
    def vaccine(self):
        print("Take vaccine")
class Dosename(CORONA):
    def covaccine(self):
        print("first dose name covaccine")
    def covishield(self):
        print("second dose name covishield")


d=Dosename()
d.vaccine()
d.covaccine()
d.covishield()


#print all values of array in upper case {"xyz","pqr","tcw","cud","mur"}
myname={"xyz","pqr","tcw","cud","mur"}
for x in myname:
    print(x.upper())



#write a program to insert values into table
    #how many value to be insert - take input from user
import mysql.connector 
mydb=mysql.connector.connect(
host="localhost",
user="root",
password="root",
database="college"
)
mycursor=mydb.cursor()
user=int(input("Enter number of rows do you want:="))
for val in range(0,user):
    Student_Id=input("Enter student Id number=")
    Student_Name=input("Enter student Name=")
    Student_Age=input("Enter student Age=")
    Student_Address=input("Enter student Address=")
    q="insert values(%s,%s,%s,%s)"
    val=(Student_Id,Student_Name,Student_Age,Student_Address)
    mydb.commit()
    
    #if it is 4 then add 4 values (it should be dynamically)
    
#Print below design take input from user
    #eg: if user enters 6 then 6 rows should be added like below design
    # ******
    # *****
    # ****
    # ***
    # **
    # *
n=int(input("Enter value"))
print(n)
temp=""
for i in range(n,0,-1):
    for k in range(1,i+1):
        temp=temp+"*"
    print(temp)
    temp=""
    
        