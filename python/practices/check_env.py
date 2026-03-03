#get the enviroment from the user
env = input("What is your current environment? (e.g. dev, stg, prd) ")




# a = int(input("Enter the num 1:"))
# b = int(input("Enter the num 2:"))


# print(f"The sum of {a} and {b} is: {a + b}")

# print(f"The multiplication of {a} and {b} is: {a * b}")

# print(f"The division of {a} and {b} is: {a / b}")
# print(f"The subtraction of {a} and {b} is: {a - b}")
print(env)
 
if env=="prd":
    print("Dont't deploy on Friday")
elif env=="stg":
    print("Take backup & Test well")
else:
    print("Safe to deploy any day")