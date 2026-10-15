def hello():
    print("Welcome to the world of data science")
    print("This is our first function")

hello()

def greet(naam):
    print("Hello "+ naam +"!!")

greet("Rahul")


def printMessage(message: str):
    for i in range(4):
        print(message)

printMessage("This is a new message")

def add(a,b):
    c=a+b
    print(c)

add(166,7626)

def multiply(a,b=5):
    return a*b

ans=multiply(5)
print(ans)
print(multiply(5,9))

divide=lambda a,b:a/b
print(divide(10,2))

numbers=[1,2,3,4,5,6,7,8,9]
def square(num):
    return num**2

SquaredNumbers=list(map(square,numbers))
print(SquaredNumbers)


result_lambda=map(lambda a:a**2,numbers)
print(list(result_lambda))

fruits=["apple","kela","santra","khajur","papita"]

uppercase_fruits=map(lambda w: w.upper(),fruits)
print(list(uppercase_fruits))