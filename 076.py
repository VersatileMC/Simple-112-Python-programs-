# Smart Coders - Problem 76
def vowels(s):
 if s=="": return 0
 return (1 if s[0].lower() in "aeiou" else 0)+vowels(s[1:])
s=input("String: ")
print("Vowels:",vowels(s))
