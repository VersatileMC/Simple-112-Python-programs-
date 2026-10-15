# Smart Coders - Problem 22
age=int(input("Age: "))
# Example age groups
if age<0: print("Invalid age")
elif age<13: print("Child")
elif age<20: print("Teenager")
elif age<60: print("Adult")
else: print("Senior")
