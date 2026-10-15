# Smart Coders - Problem 20
ch=input("Letter: ").lower()
if len(ch)!=1 or not ch.isalpha(): print("Not an alphabet")
elif ch in "aeiou": print("Vowel")
else: print("Consonant")
