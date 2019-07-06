#euler2
m = 0
x , y = 1 , 2
while y < 4000001:
	if y % 2 ==0:
		m += y
	x, y = y, x + y	
#	print(str(x) + "  " + str(y))
	
print("Sum = " + str(m))