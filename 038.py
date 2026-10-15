# Smart Coders - Problem 38
n=int(input("Three-digit number: "))
if 100<=n<=999:
 total=sum(int(d)**3 for d in str(n))
 print("Armstrong" if total==n else "Not Armstrong")
else: print("Enter a three-digit number")
