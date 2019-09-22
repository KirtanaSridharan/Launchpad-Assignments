num = [1,2,3,4,5,2,6,7,2,8]
ele = input("Enter the element to be searched:")
ele_int = int(ele)
for i in range(len(num)):
    if num[i]==ele_int:
        print(i)