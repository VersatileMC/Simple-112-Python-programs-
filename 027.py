# Smart Coders - Problem 27
units=float(input("Units used: "))
# Example slab rates: first 100 at Rs 2, next 100 at Rs 3, remaining at Rs 5
if units<0: print("Invalid units")
elif units<=100: print("Bill:",units*2)
elif units<=200: print("Bill:",200+(units-100)*3)
else: print("Bill:",500+(units-200)*5)
