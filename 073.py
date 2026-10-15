# Smart Coders - Problem 73
count=0;total=0
while True:
 n=float(input("Number (-1 to stop): "))
 if n==-1: break
 count+=1;total+=n
print("Count:",count)
print("Average:",total/count if count else "No numbers entered")
