item1=500
item2=2500

print("The total amount of items is ",item1+item2)

if(item1>5000):
    discount=item1*20/100
    print(item1-discount)
elif(item1>3000 and item1<5000):
    discount=item1*10/100
    print(item1-discount)
else:
    print("No discount")