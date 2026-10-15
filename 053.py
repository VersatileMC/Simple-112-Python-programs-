# Smart Coders - Problem 53
def product(n):
 n=abs(n)
 if n<10: return n
 return (n%10)*product(n//10)
n=int(input("Number: "))
print("Product of digits:",product(n))
