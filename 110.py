# Smart Coders - Problem 110
n=int(input("Size: "))
for i in range(n):
 for j in range(n): print("*" if i==n//2 or j==n//2 else " ",end="")
 print()
