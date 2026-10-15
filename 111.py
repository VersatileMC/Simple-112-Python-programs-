# Smart Coders - Problem 111
n=int(input("Size: "))
for i in range(n//2,n+1,2):
 print(" "*(n-i)+"*"*i+" "*(n-i)+"*"*i)
for i in range(2*n,0,-2): print(" "*((2*n-i)//2)+"*"*i)
