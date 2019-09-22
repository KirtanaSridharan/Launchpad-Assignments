s = []
s = input("Enter a sentence:")
print(s)
ss = f"{s[-4:]} {s[-7:-5]} {s[-14:-8]}"
ss.lower()
ss = ss.capitalize()
print(ss)