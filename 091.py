# Smart Coders - Problem 91
n=int(input("Size: "))
for i in range(1,n+1):
 for j in range(i): print((j+1)%2,end="")
 print()
