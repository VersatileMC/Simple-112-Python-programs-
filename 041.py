# Smart Coders - Problem 41
h=int(input("Hour (1-12): "));m=int(input("Minute (0-59): "))
if not 1<=h<=12 or not 0<=m<60: print("Invalid time")
else:
 angle=abs((h%12)*30+m*0.5-m*6)
 print("Smaller angle:",min(angle,360-angle))
