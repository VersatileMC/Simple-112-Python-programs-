# Smart Coders - Problem 69
n=int(input("Positive number: "))
if n<=0: print("Enter a positive number")
else:
 for i in range(1,n+1):
  if n%i==0: print(i,end=" ")
 print()
