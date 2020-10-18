# euler Problem #6
# The sum of the squares of the first ten natural numbers is, 
# The square of the sum of the first ten natural numbers is,
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of
# the sum is .
# Find the difference between the sum of the squares of the first one hundred natural numbers and the 
# square of the sum.

def square_sum1():
	k = 0
	for i in range(1,101):
		k = k + (i * i)
	return k
def square_sum2():
	m = 0
	for i in range(1,101):
		m = m + i
	n = m * m
	return n
m1 = square_sum1
m2 = square_sum2
print(m1)
print(m2)
# print(str(m2 - m1))	
