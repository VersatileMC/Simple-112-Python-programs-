# Smart Coders - Problem 104
n=int(input("Size: "))
size=2*n-1
for i in range(size):
 for j in range(size):
  d=min(i,j,size-1-i,size-1-j)
  print(" " if d==0 and 0<i<size-1 and 0<j<size-1 else ("*" if i==0 or i==size-1 or j==0 or j==size-1 or j==i or j==size-1-i else " "),end="")
 print()
