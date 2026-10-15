# Smart Coders - Problem 4
choice=input("Convert C to F or F to C? (C/F): ").upper()
t=float(input("Temperature: "))
if choice=="C": print("Fahrenheit:",t*9/5+32)
elif choice=="F": print("Celsius:",(t-32)*5/9)
else: print("Invalid choice")
