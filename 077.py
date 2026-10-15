# Smart Coders - Problem 77
def show(i,n):
 if i>n: return
 print(i,end=" ")
 show(i+1,n)
 print(i,end=" ")
n=int(input("N: "))
show(1,n)
print()
