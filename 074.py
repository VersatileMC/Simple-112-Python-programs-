# Smart Coders - Problem 74
x=float(input("x (radians): "));n=int(input("Number of terms: "));total=0;factorial=1;power=x
for i in range(n):
 if i>0:
  power*=x*x
  factorial*=(2*i)*(2*i+1)
 term=power/factorial
 if i%2==0: total+=term
 else: total-=term
print("Sin series sum:",total)
