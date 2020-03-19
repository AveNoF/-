f=[[1,3],[2,4],[6,3],[4,4],[2,2],[5,3]]
d=[1,2,3,4,5,6]
i=0

print("f: ",f)
print("d: ",d)

already=[]

for i in range(len(f)):
	if f[i][0] not in d:
		print("This is not function")
		exit()
	elif f[i][0] in already:
		print("This is not function")
		exit()
	
	already.append(f[i][0])

if (set(d) <= set(already)) == False:
	print("This is not function")
	exit()



print("True")


