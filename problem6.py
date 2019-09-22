value = []
key = []
for i in range(3):
    value.append(input("Enter name:"))
    key.append(input("Enter USN:"))
dictt = {}
dictt = dict()
for i in range(3):
    dictt[key[i]]=value[i]
print(dictt)