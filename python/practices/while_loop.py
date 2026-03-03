# choice = input("Etnter the choice (press q to quite)")

# while choice !="q":
#     num = int(input("Enter the no for tables: "))

#     for i in range(1,11):
#         print(f"{num} X {i} = {num*i}") # formate the string
#     choice = input("Etnter the choice (press q to quite)")


while True:
    choice = input("Enter the number for Tables or (press for q quite): ")
    if(choice.lower() =='q'):
        print("Code has break")
        break
    if not choice.isdigit():
        print('Enter tables for number or quite  for q ')
        continue
    for i in range(1,11):
        print(f"{int(choice)} X {i} = {int(choice)*i}") # formate the string
    
