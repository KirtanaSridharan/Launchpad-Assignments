name = input("Enter name:")
age = input("Enter age:")
age_int = int(age)
year = 100-age_int
new_year = 2019 + year
for i in range(len(name)):
    if name[i]==" ":
        firstname=name[0:i+1]
s =f"Hey {firstname}! You will turn 100 in the year {new_year}"
print(s)
