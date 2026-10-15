# Smart Coders - Problem 106
n=int(input("Size: "))
for i in range(3):
 for j in range(n):
  print("*" if (i+j)%4==0 or (i==1 and j%4==2) else " ",end="")
 print()
