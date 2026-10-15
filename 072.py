# Smart Coders - Problem 72
binary=input("Binary number: ");decimal=0
if not binary or any(d not in "01" for d in binary): print("Invalid binary")
else:
 for d in binary: decimal=decimal*2+int(d)
 print("Decimal:",decimal)
