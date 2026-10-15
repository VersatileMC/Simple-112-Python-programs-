# Smart Coders - Problem 21
age=int(input("Age: "))
# Example prices (not specified in assignment)
if age<0: print("Invalid age")
elif age<12: print("Ticket: Rs 50")
elif age>=60: print("Ticket: Rs 80")
else: print("Ticket: Rs 120")
