#program to sort array accoding to their no of occurence
ar=[1,1,2,2,2,2,3]
new={}
for i in ar:
	k=ar.count(i)
	new[k]=i
n=new.keys()
n=list(n)
n.sort()
n1=""
for i in n:
	n1+=str(i)
n1=n1[::-1]
n1=list(n1)
for i in range(len(n1)):
	n1[i]=int(n1[i])
final=""
for i in n1:
	f=str(new[i])*i
	final+=f
f=list(final)
for i in range(len(f)):
	f[i]=int(f[i])
print(f)
