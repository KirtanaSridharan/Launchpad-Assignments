numlist = [1,1,2,3,2,4,5,5,6]
newlist = []
for i in numlist:
     if i not in newlist:
          newlist.append(i)
print(newlist)
