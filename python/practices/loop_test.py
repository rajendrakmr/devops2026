for i in range(5):
    env = input("What is your current environment? (e.g. dev, stg, prd) ") 
    if env=="prd":
        print("Dont't deploy on Friday")
    elif env=="stg":
        print("Take backup & Test well")
    else:
        print("Safe to deploy any day")



#variable 
#loop
#input
#condition