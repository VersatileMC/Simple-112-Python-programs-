# Smart Coders - Problem 67
n=int(input("Number: "))
if n<0: print("Not Armstrong")
else:
 digits=str(n);total=0
 for d in digits: total+=int(d)**len(digits)
 print("Armstrong" if total==n else "Not Armstrong")
