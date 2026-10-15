# Smart Coders - Problem 48
n=abs(int(input("Number: ")));count=0
if n==0: count=1
while n>0:
 count+=1;n//=10
print("Digits:",count)
