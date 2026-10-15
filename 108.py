# Smart Coders - Problem 108
n=int(input("Size: "))
for i in list(range(1,n+1))+list(range(n-1,0,-1)):
 print("*"+" "*(n-1)+"*"*i)
