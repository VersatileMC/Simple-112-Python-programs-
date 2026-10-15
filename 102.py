# Smart Coders - Problem 102
n=int(input("Size: "))
for i in range(1,n+1):
 left="".join(chr(65+j) for j in range(i))
 print(" "*(n-i)+left+left[-2::-1])
