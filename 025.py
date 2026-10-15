# Smart Coders - Problem 25
m=float(input("Marks (0-100): "))
if m<0 or m>100: print("Invalid marks")
elif m>=90: print("A")
elif m>=80: print("B")
elif m>=70: print("C")
elif m>=60: print("D")
else: print("F")
