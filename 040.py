# Smart Coders - Problem 40
balance=float(input("Balance: "));amount=float(input("Withdrawal: "))
minimum=float(input("Required minimum balance: "))
if amount<=0 or balance<0 or minimum<0: print("Invalid input")
elif amount>balance: print("Rejected: insufficient funds")
elif balance-amount<minimum: print("Rejected: minimum balance rule")
else: print("Approved. Remaining balance:",balance-amount)
