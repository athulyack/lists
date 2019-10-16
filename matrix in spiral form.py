#print matrix in spiral form
row=3
col=2
mat=[]
a=[]
for i in range(row):
	r=[]
	for j in range(col):
		ab=int(input())
		r.append(ab)
	mat.append(r)
for i in range(len(mat)):
	b=[]
	b=mat[i]
	if i%2==0:
		a.append(b)
		continue
	else:
		b.reverse()
		a.append(b)

print(a)