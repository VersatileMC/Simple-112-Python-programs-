# Smart Coders - Problem 63
x=float(input("x: "));n=int(input("n: "));result=1
for i in range(abs(n)): result*=x
if n<0:
 if x==0: print("Undefined")
 else: print("Power:",1/result)
else: print("Power:",result)
