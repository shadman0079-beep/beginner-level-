age = int(input("Enter your age: "))
print ("You are " + str(age) + " years old.")

if age >= 90:  
    print ("senior More like date expired ")
elif age >= 18:
    print ("adult")

elif age >= 13:
    print ("teenager")
else:
    print ("child")
if age >= 18 and age < 90:
    print ("You are eligible to vote.")