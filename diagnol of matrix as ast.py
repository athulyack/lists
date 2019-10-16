r=int(input())
c=int(input())
mat=[]
for i in range(r):
	a=[]
	for j in range(c):
		b=int(input())
		a.append(b)
	mat.append(a)
for i in range(len(mat)):
	mat[i][i]="*"
print(mat)
for i in range(r):
	for j in range(c):
		print(mat[i][j],end=" ")
	print()