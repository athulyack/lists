n=int(input())
listfinal=[]
a=0
def delt(list1,min1):
	for ii in range(len(list1)):
		if list1[ii][1]==min1:
			list1.pop(ii)
			return
def find(list1,min1):
	listfinal=""
	for ii in range(len(list1)):
		if list1[ii][1]==min1:
			listfinal=list1[ii][0]
			list1.pop(ii)
			return listfinal
list1=[]
mark=[]
for i in range(n):
        name = input()
        score = float(input())
        mark.append(score)
        list1.append([name,score])
min1=list1[0][1]
for j in range(len(list1)):
    if list1[j][1]<min1:
        min1=list1[j][1]
a=mark.count(min1)
for re in range(a):
	mark.remove(min1)
print(mark)
for cou in range(a):
	delt(list1,min1)
print(list1)
min1=list1[0][1]
for j in range(len(list1)):
    if list1[j][1]<min1:
        min1=list1[j][1]
a=mark.count(min1)
for cou in range(a):
	listfinal.append(find(list1,min1))
listfinal.sort()
for i in range(len(listfinal)):
	print(listfinal[i])






