myarr=["n","s","k","p","h","a"]
#reverse
myarr.reverse()
print(myarr)
#print all value
for val in myarr:
    print(val)
myarr1=[-34,6,-25,45,-2,4]
#reverse
myarr1.reverse()
print(myarr1)
#add when value is positive and substract when value is negative then print total
temp=0
for int in myarr1:
    temp=temp+int
print(temp)
if temp>0:
    print(temp+int)
elif temp<0:
    print(temp-int)
else:
    print(invalid)
#take one string "python is programming language"
str=" python is programming language \""
print(str)
#remove while space
print(str.strip())
#take only "python" from string
print(str[1:7])
#change python to java
str=str.replace("python","Java")
print(str)