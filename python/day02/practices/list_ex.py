a = [100,200,True,"hello"]

print(a)


clouds =list()
clouds.append("aws")
clouds.append("azure")
clouds.append("gcp")
clouds.append('utho')

print(clouds)
print("length of list is ",len(clouds))
print("World leader of cloud service provider :" ,clouds[-1])
# print(dir(clouds))

for i in clouds:
    if(i == 'aws'):
        print(f"{i} is Market Leader")
    elif(i =="utho"):
        print(f"{i} is Indian cloud provider")
    else:
        print(f"{i} ko padhan padega")
  