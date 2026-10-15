# Smart Coders - Problem 31
m=int(input("Month (1-12): "))
y=int(input("Year (for February): "))
if m in (1,3,5,7,8,10,12): print(31)
elif m in (4,6,9,11): print(30)
elif m==2: print(29 if y%400==0 or (y%4==0 and y%100!=0) else 28)
else: print("Invalid month")
