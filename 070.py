# Smart Coders - Problem 70
n=int(input("Positive number: "));total=0
for i in range(1,n):
 if n%i==0: total+=i
print("Perfect number" if n>1 and total==n else "Not perfect")
