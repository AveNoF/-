



problem=[[0,6,18,1,12],[1,5,7,11],[1,5,7,11,13,17,19,23],[0,2,4,8,16],[0,1,17,23,5],[1,3,9,7,15]]
print("problem= ",problem,"\n")

hantei = 0

for i in range (len(problem)):
	for j in range(len(problem[i])):
		for k in range(len(problem[i])):
			if  problem[i][j] * problem[i][k] % 24 == 0 and hantei == 0:
				print("\n problem[",i,"] is closed\n")
				hantei = 1
	if hantei != 1:
		print("\n problem[",i,"] is not closed\n")
	hantei = 0
