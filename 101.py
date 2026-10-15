# Smart Coders - Problem 101
n=int(input("Size: "))
for i in range(1,n+1): print(" "*(n-i)+"".join(chr(65+j) for j in range(i)))
