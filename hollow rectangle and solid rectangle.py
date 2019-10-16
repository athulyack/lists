r=5
col=4
for i in range(r):
	a=col
	if i==0 or i==r-1:
		print("* "*col)
		continue
	print("*",end="" )
	print("  "*(col-2),"* ")
	print()
for i in range(r):
	print("* "*col)
	