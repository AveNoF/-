f=[[1,4],[4,3],[2,3],[6,5],[3,4],[5,6]]




Im=[]
f2=[]
onebyone=1
already1=[]



for i in range (len(f)):
	already1.append(f[i][1])
	if f[i][1] not in Im:
		Im.append(f[i][1])
	if f[i][1] in already1:
		onebyone=0
	

for i in range (len(f)):
	if f[i][0] in Im:
		f2.append(f[i])


print("Im: ",Im)#a

print("F^2: ",f2)#b

if onebyone == 1:#c
	print("f is one by one")
else:
	print("f is not one by one")
	

