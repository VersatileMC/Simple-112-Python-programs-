# Smart Coders - Problem 92
n=int(input("Size: "))
for i in range(n):
 print(" "*(n-i-1),end="")
 value=1
 for j in range(i+1):
  print(value,end=" ")
  value=value*(i-j)//(j+1) if j<i else value
 print()
