# Smart Coders - Problem 103
n=int(input("Size: "))
for i in list(range(1,n+1))+list(range(n,0,-1)):
 print("*"*i+" "*(2*(n-i))+"*"*i)
