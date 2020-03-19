


a=[]
i=0
for i in range(5):
	add=input("input A:")
	print(add,"is",i,"st num")
	a.append(add)
print("A=",a)


b=[]
i=0
for i in range(10):
	add=input("input B:")
	print(add,"is",i,"st num")
	b.append(add)
print("B=",b)


if (set(a) <= set(b)) == True:
	print("Ans: 1")
else:
	print("Ans: 0")

