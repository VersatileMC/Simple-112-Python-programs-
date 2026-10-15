# Smart Coders - Problem 68
n=abs(int(input("Number: ")));small=9;large=0
if n==0: small=large=0
while n>0:
 d=n%10
 if d<small: small=d
 if d>large: large=d
 n//=10
print("Smallest:",small,"Largest:",large)
