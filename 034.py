# Smart Coders - Problem 34
import math
a=float(input("a: "));b=float(input("b: "));c=float(input("c: "))
if a==0: print("Not quadratic")
else:
 d=b*b-4*a*c
 if d>0: print("Two real roots:",(-b+math.sqrt(d))/(2*a),(-b-math.sqrt(d))/(2*a))
 elif d==0: print("Equal roots:",-b/(2*a))
 else: print("Imaginary roots:",complex(-b/(2*a),math.sqrt(-d)/(2*abs(a))),complex(-b/(2*a),-math.sqrt(-d)/(2*abs(a))))
