def table(num):
    for i in range(1, 11):
        print(f"{num} X {i} = {num * i}")
    print()

# h
while True:
    user_input = input("Table ke liye number daalo (exit ke liye q): ")

    if user_input.lower() == "q":
        print("Program exit ho gaya 👍")
        break

    if not user_input.isdigit():
        print("Sirf number ya 'q' daalo ❌")
        continue

    table(int(user_input))
