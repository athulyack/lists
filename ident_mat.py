r1=int(input())
c1=int(input())
r2=int(input())
c2=int(input())
a1=[]
k=1
a2=[]
if r1!=r2 or c1!=c2:
	print("nottt")
	k=0
if k==1:
	for i in range(r1):
		l=[]
		l=[int(m) for m in input().split()]
		a1.append(l)
	for i in range(r2):
		l=[]
		l=[int(m) for m in input().split()]
		a2.append(l)
	for i in a1:
		for j in a2:
			if i!=j:
				print("nottt")
				k=0
				break
		if k==0:
			break
if k==1:
	print("yessssssssss")
