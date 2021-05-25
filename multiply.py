a=2
b=3
c=int(a*b)
str="{}*{}={}"
print(str.format(a,b,c))
str1="{}is even then add 25={}"
str2="{} is odd then sub 25={}"
if c%2==0:
    print(str1.format(c,c+25))
else:
    print(str2.format(c,c-25))
    
	