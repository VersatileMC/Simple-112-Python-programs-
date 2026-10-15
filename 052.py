# Smart Coders - Problem 52
n=int(input("Positive number: "))
if n<=0: print("Enter a positive number")
else:
 while n!=1 and n!=4:
  total=0
  while n>0:
   d=n%10;total+=d*d;n//=10
  n=total
 print("Happy number" if n==1 else "Not happy")
