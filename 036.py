# Smart Coders - Problem 36
cp=float(input("Cost price: "));sp=float(input("Selling price: "))
if sp>cp: print("Profit:",sp-cp)
elif sp<cp: print("Loss:",cp-sp)
else: print("No profit, no loss")
