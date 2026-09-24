""" age = 20
if age >= 18:
    print("You are an adult.")
    if age >= 65:
        print("You are a senior citizen.") """

"""age =  int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
    if age >= 65:
        print("You are a senior citizen.")
    else :
        print("You are not adult nor senior citizen.")
else:
    print("You are a child.")"""

age =  int(input("Enter your age: "))
print ("You are an adult." if age >= 18 else "You are a child.")
if age >= 90:
    print("You are eligible for senior citizen benefits and voting rights.")
elif age >= 18: 
    print("You are an adult")
    if  age <= 65:
        print("You are in working age") 
    else :  
        print("You are a senior citizen.")
elif age >=13:
    print("You are a teenager.")
else:
    print("You are a child.")                