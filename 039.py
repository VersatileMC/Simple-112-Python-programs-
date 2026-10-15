# Smart Coders - Problem 39
hours=float(input("Hours worked: "));rate=float(input("Hourly rate: "))
if hours<0 or rate<0: print("Invalid input")
elif hours<=40: print("Salary:",hours*rate)
else: print("Salary:",40*rate+(hours-40)*rate*1.5)
