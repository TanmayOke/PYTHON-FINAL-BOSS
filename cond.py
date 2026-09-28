num=int(input("Enter a number: "))

if (num%2==0):
    print("The number is even")
else:
    print("The number is odd")  

for i in range(1,11):
    print(str(num) + " x " + str(i) + " = " + str(num*i))