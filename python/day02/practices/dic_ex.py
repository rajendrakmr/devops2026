info = {
    "name": "rajendra",# string
    "city": "bokaro", # string
    "qualification": "Bachlor of Computer Application", # string
    "age":27, # integer
    "salary":10.5, # float
    "married": True, # boolean
    "favorite_languages": ["python","java","javascript"], # list
}

print(f"I Live in {info['city']} and I am {info['age']} years old")
info.update({"designation":"Software Engineer"})
# print(info)


for key,value in info.items():
    print(f"{key} : {value}")