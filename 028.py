# Smart Coders - Problem 28
a=float(input("Side 1: "));b=float(input("Side 2: "));c=float(input("Side 3: "))
if min(a,b,c)<=0 or a+b<=c or a+c<=b or b+c<=a: print("Invalid triangle")
elif a==b==c: print("Equilateral")
elif a==b or b==c or a==c: print("Isosceles")
else: print("Scalene")
