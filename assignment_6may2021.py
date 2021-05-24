#take one string with duplicate value
str=["a","y","p","s","p","o"]
print("String with duplicate value",str)
#convert into list
mylist=list(str)
print("convert list",mylist)
#add 2 values
mylist.append("h")
mylist.append("i")
print("add 2 values",mylist)
#sort list
mylist.sort()
print("sort list",mylist)
#convert list into set
myset=set(mylist)
print("convert list to set",myset)
#create new set
myset2={"l","p","i","t","o"}
print("new set values",myset2)
#difference between 2 set
myset3=myset.difference(myset2)
print("Difference between two set",myset3)
#make copy of output and create set
myset4=myset3.copy()
print("copy and create new set",myset4)
#convert into tuple
mytuple=tuple(myset4)
print("convert into tuple",mytuple)
#length of tuple
print(len(mytuple))
#remove 2 values from tuple
myset5=set(mytuple)
print(myset5)
myset5.remove("s")
myset5.remove("a")
print(myset5)
#add 2 values from tuple
myset5.add("m")
myset5.add("f")
print(myset5)
#what is difference between set,tupleand list
#ans= List is a container to contain different types of objects and is used to iterate objects.List consumes less memory.
# Tuple is also similar to list but contains immutable objects. Tuple processing is faster than List.List consumes more memory.
#Sets are another standard Python data type that also store values. some modify functions are different than list