# Smart Coders - Problem 29
a=float(input("Side 1: "));b=float(input("Side 2: "));c=float(input("Side 3: "))
print("Valid triangle" if min(a,b,c)>0 and a+b>c and a+c>b and b+c>a else "Invalid triangle")
