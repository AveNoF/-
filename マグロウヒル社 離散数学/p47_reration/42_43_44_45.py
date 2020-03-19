R = [1,2,3,4]
r=[[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]],[[1,1],[1,2],[1,3],[2,2],[2,3],[4,4]],[[1,2],[2,1],[2,2],[3,4],[3,3],[4,3]],[[1,4],[2,3],[4,3],[2,4],[3,1],[3,2]]]

for k in range (len(r)):


	r[k].sort()

	print(r[k])

	rdmain=[]

	i=1
	rdmain.append(r[k][0][0])
	for i in range (len(r[k])-1):
		
		if r[k][i][0] != r[k][i+1][0]:
			rdmain.append(r[k][i+1][0])
		

		
	print("R_dmain= ",rdmain,"\n")

	rrange=[]

	i=1
	rrange.append(r[k][0][1])
	for i in range (len(r[k])-1):
		
		if r[k][i][1] != r[k][i+1][1] and r[k][i+1][1] not in rrange:
			rrange.append(r[k][i+1][1])
		

		
	print("R_range= ",rrange,"\n")

	synthfunc=[]
	
	for i in range (len(r[k])):
		for j in range (len(r[k])):
			if r[k][i][1] == r[k][j][0]:
				newS=[r[k][i][0],r[k][j][1]]
				if newS not in synthfunc:
					synthfunc.append(newS)

	print("\n R^2:",synthfunc,"\n")
	hantei=[0,0,0,0]
	ref = 1
	symm = 1
	antisym = 1
	tra = 1
	
	for i in range (len(R)):
		for j in range (len(r[k])):
			if R[i] != r[k][j][1] and R[i] != r[k][j][0] and hantei[0] == 0:
				hantei[0] = 1
				ref = 0 
			elif R[i] == r[k][j][0]:
				for m in range (len(r[k])):
					
					if r[k][j][0] != r[k][m][1]\
					and r[k][j][1] != r[k][m][0]\
					and hantei[1] == 0:
							hantei[1] = 1
							sym = 0
					
					if r[k][j][0] == r[k][m][1]\
					and r[k][j][1] == r[k][m][0]:
						if r[k][j][0] != r[k][j][1] and hantei[2]== 0:
							print("asdasdasdasdasdad")
							hantei[2] = 1
							antisym = 0
					if (r[k][j][1] == r[k][m][0]) and hantei[3] == 0:
						tmp = [r[k][j][0],r[k][m][1]]
						if tmp in r[k]:
							hantei[3] == 1
							tra = 0
	if ref == 1:
		print("Reflective")
	else:
		print("Not Reflective")
		
	
	if sym == 1:
		print("Symmetry")
	else:
		print("Not Symmetry")
	if antisym ==1:
		print("Unsymmetry")
	else:
		print("Not Unsymmetry")
	if tra == 1:
		print("Transitive")
	else:
		print("Not Transitive")
		
	


print("\n\n\n")
matrix = []

chilno=[]

print("Matrix of R :")
for i in range (len(R)):
	for j in range (len(R)):
		chilno = [R[i],R[j]]
		matrix.append(chilno)


for i in range (len(matrix)):
	print(str(matrix[i]), end='')
	if (i+1)%4 == 0:
		print("\n",end="")
