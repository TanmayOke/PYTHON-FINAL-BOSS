customer={}

def add_customer(account_number,name,balance):
    if account_number in customer:
       print("Account number already exists!!")
    else:
     customer[account_number]={
        "Name":name,
        "Balance":balance
    }
     print("Customer addded succesfully!!")

def display_customer(account_number):
   if account_number in customer:
      print(f"Account Number: {account_number}")
      print(f"Name: {customer[account_number]['Name']}")
      print(f"Balance: {customer[account_number]['Balance']}")
   else:
      print("Account number does not exists!!")

add_customer(105,"Tanmay",500000)
add_customer(102, "Akbar", 7000)
add_customer(103, "Anthony", 5000)
display_customer(105)
display_customer(102)
display_customer(103)