# Smart Coders - Problem 30
a=float(input("First: "));op=input("Operator (+,-,*,/): ");b=float(input("Second: "))
# Python if/elif is the beginner-friendly equivalent of switch-case
if op=="+": print(a+b)
elif op=="-": print(a-b)
elif op=="*": print(a*b)
elif op=="/": print(a/b if b!=0 else "Cannot divide by zero")
else: print("Invalid operator")
