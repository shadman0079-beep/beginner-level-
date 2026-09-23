"""age = 20
if age >= 18:
    print("You are an adult.")
    if age >= 65:
        print("You are a senior citizen.") """

age =  int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
    if age >= 65:
        print("You are a senior citizen.")
    else :
        print("You are not adult nor senior citizen.")
else:
    print("You are a child.")