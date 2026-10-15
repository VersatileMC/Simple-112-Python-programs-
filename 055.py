# Smart Coders - Problem 55
n=int(input("N: "));result=1
if n<0: print("Factorial undefined")
else:
 for i in range(1,n+1): result*=i
 print("Factorial:",result)
