# Smart Coders - Problem 105
n=int(input("Size: "))
for i in list(range(1,n+1))+list(range(n-1,0,-1)):
 print(" "*(n-i)+"".join(str(j) for j in range(1,i+1))+"".join(str(j) for j in range(i-1,0,-1)))
