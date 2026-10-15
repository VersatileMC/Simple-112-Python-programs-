# Smart Coders - Problem 99
n=int(input("Size: "))
for i in range(1,n+1): print("".join(chr(65+j) for j in range(i)))
