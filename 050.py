# Smart Coders - Problem 50
n=int(input("Number: "));x=abs(n);rev=0
while x>0:
 rev=rev*10+x%10;x//=10
print("Reversed:",-rev if n<0 else rev)
