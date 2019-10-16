#program to find row having max no of zero in 0/1 matrix
r=int(input())
c=int(input())
mat=[]
for i in range(r):
	a=[]
	for j in range(c):
		b=int(input())
		a.append(b)
	mat.append(a)
print(mat)
count=[]
for i in mat:
	m=i.count(0)
	count.append(m)
f=count
ind=count.index(max(count))
print(ind+1)
