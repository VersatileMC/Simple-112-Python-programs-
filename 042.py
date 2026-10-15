# Smart Coders - Problem 42
marks=float(input("Marks percentage: "));attendance=float(input("Attendance percentage: "));income=float(input("Annual family income: "))
# Example eligibility limits; assignment does not provide thresholds
if marks>=80 and attendance>=75 and income<=200000: print("Eligible")
else: print("Not eligible")
