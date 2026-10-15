# Smart Coders - Problem 107
n=4
size=4
matrix=[[0]*size for i in range(size)]
top=0;bottom=size-1;left=0;right=size-1;num=1
while top<=bottom and left<=right:
 for j in range(left,right+1): matrix[top][j]=num;num+=1
 top+=1
 for i in range(top,bottom+1): matrix[i][right]=num;num+=1
 right-=1
 if top<=bottom:
  for j in range(right,left-1,-1): matrix[bottom][j]=num;num+=1
  bottom-=1
 if left<=right:
  for i in range(bottom,top-1,-1): matrix[i][left]=num;num+=1
  left+=1
for row in matrix: print(*row)
