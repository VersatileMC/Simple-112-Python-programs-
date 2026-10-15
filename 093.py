# Smart Coders - Problem 93
n=int(input("Size: "))
for i in range(1,n+1): print(" "*(n-i)+"".join(str(j) for j in range(1,2*i)))
