# Smart Coders - Problem 97
n=int(input("Size: "))
for i in range(1,n+1): print("".join(str(j%2) for j in range(i)))
