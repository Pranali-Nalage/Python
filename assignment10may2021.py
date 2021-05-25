#create numeric array
myarr=[12,55,33,44,99,2,1]
print("numeric array",":",myarr)

#find out lowest number
myarr.sort()
print("Lowest Number",":",myarr[0])

#find out height number
myarr.sort()
print("Highest Number",":",myarr[len(myarr)-1])

#create String array
myarr1=["Sunday","Monday","Tuesday","Wednsday","Thursday","Friday","saturday"]
print("String array",":",myarr1)

#find out lowest length text
temp1=len(myarr1[0])
str=""
for v in myarr1:
    if (temp1>=len(v)):
       temp1=len(v)
       str=v
print("Lowest length numbr",":",temp1,"=",str)

#find out highest length text
temp=0
str1=""
for val in myarr1:
    if (temp<len(val)):
        temp=len(val)
        str1=val
print("Highest length numbr",":",temp,"=",str1)
