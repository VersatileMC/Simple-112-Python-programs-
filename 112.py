# Smart Coders - Problem 112
n=int(input("Size: "))
for i in range(n):
 for j in range(n): print("*" if i==0 or j==0 or i==n-1 or j==n-1 or i==j or i+j==n-1 else " ",end="")
 print()
