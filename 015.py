# Smart Coders - Problem 15
n=int(input("Non-negative number: "))
if n<0: print("Enter a non-negative number")
else:
 count=0
 while n:
  count+=n&1
  n>>=1
 print("Set bits:",count)
