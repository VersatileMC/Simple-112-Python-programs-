# Smart Coders - Problem 26
n=int(input("Day (1-7): "))
days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print(days[n-1] if 1<=n<=7 else "Invalid day")
