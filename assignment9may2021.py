#Take two input from users
a=int(input("Enter no 1:a="))
b=int(input("Enter no  :b="))
#Display nearest value from users
val=100
for x in (a,b):
    print("close","=",(val-x))
    if a>b:
        print("a")
    else:
        print("b")
#create dictionary with 5 value
myDict={"Pranali":{"id":1,"Adress":"Mulund","age":27},"Akku":{"id":2,"Adress":"Diva","age":30},"Prajyo":{"id":3,"Adress":"Thane","age":28},"Sayli":{"id":4,"Adress":"Airoli","age":26},"Darshu":{"id":1,"Adress":"Mulund","age":27}}
#iterate all the keys and value
for y in myDict:
    print(y,"=",myDict[y])
#store constant values in variable
mytp=(1,5,8,6,8)
mylist=list(mytp)
print(mylist)
mylist.append(7)
print(mylist)
#max and min value
myarr=[5,2,45,8,5,6]
myarr.sort()
print("Min no","=",myarr[0])
print("Max no","=",myarr[len(myarr)-1])
#store unique values no duplicate
myset={5,6,6,4,2,3,7}
print(myset)