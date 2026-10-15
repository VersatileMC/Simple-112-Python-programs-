# Smart Coders - Problem 14
n=int(input("Number: "));k=int(input("Bit position (0-based): "))
print("Set" if n&(1<<k) else "Not set")
