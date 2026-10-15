# Smart Coders - Problem 75
def palindrome(s):
 if len(s)<=1: return True
 return s[0]==s[-1] and palindrome(s[1:-1])
s=input("String: ")
print("Palindrome" if palindrome(s) else "Not palindrome")
