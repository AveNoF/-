x=input("input X:")
print("X=",x)
a=[]
i=0
for i in range(5):
	add=input("input A:")
	print(add,"is",i,"st num")
	a.append(add)
print("A=",a)


if x in a:
	print("Ans: 1")
else:
	print("Ans: 0")
