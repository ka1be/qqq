# Euler 3
def SimpleDividers(n):
	answer = []
	d = 2
	while d * d <= n:
		print(d)
		if n % d ==0:
			answer.append(d)
			n //= d
		else:
			d +=1
	if n > 1:
			answer.append(n)
	return answer		

 print(SimpleDividers(600851475143))	
# print(max(SimpleDividers(600851475143)))
# print(SimpleDividers(47))