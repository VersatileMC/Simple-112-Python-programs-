# Smart Coders - Problem 59
a=int(input("First: "));b=int(input("Second: "));x=abs(a);y=abs(b)
while y: x,y=y,x%y
print("LCM:",abs(a*b)//x if x else 0)
