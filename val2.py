myarr=["a","b"," g ","d","e"]
myarr1=["ghj","fjg"]
print(len(myarr))
myarr.extend(myarr1)

for val in myarr:
	print("my value is =", val.strip())
myarr.sort()
print(myarr)

    
