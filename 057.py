# Smart Coders - Problem 57
n=int(input("N: "))
for num in range(2,n+1):
 prime=True
 for i in range(2,int(num**0.5)+1):
  if num%i==0: prime=False;break
 if prime: print(num,end=" ")
print()
