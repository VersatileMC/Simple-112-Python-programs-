# Smart Coders - Problem 58
a=abs(int(input("First: ")));b=abs(int(input("Second: ")))
while b!=0: a,b=b,a%b
print("GCD:",a)
