# Smart Coders - Problem 33
a=float(input("First: "));b=float(input("Second: "));c=float(input("Third: "))
if a>b: a,b=b,a
if b>c: b,c=c,b
if a>b: a,b=b,a
print(a,b,c)
