# Smart Coders - Problem 5
n=int(input("Number: "))
if n%3==0 and n%5==0: print("Divisible by both")
elif n%3==0: print("Divisible by 3")
elif n%5==0: print("Divisible by 5")
else: print("Neither")
