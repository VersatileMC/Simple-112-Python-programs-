# Smart Coders - Problem 23
h=int(input("Hour (0-23): "))
if not 0<=h<=23: print("Invalid hour")
elif 5<=h<12: print("Morning")
elif 12<=h<17: print("Afternoon")
elif 17<=h<21: print("Evening")
else: print("Night")
