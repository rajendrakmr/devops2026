import requests

# API ( Application Programming Interface )

url = "https://dummyjson.com/todos/1"

response = requests.get(url=url)

for key,value in (response.json()).items():
    if(key=="userId"):
        if value in [152,25,4,2,1]:
            print("user Present: ",value)
        else:
            print("user id not prs: ",value)
    # print(key,value)