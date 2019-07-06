# euler4.py


# Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. 
# Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.
# Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
k2 = 0
flagglobal = False
def CheckPalyndrome(n):
	a1 = list(str(n))
	k = len(str(n))	
	flag = False
	if k % 2 ==0:			
		for j in range(1, int(k / 2)+1, 1):
			if a1[j-1] == a1[len(str(n)) - j]:
				flag = True
			else: 
				flag = False		
				break				
	else:	
		for j in range(1, int(k / 2)+2, 1):
			if a1[j-1] == a1[len(str(n)) - j]:
				flag = True
			else:
				flag = False		
				break	
	return flag
for i1 in range(100,999,1):		
	for i2 in range(100,999,1):		
		k1 = i1 * i2
		if (k1 > k2) and (CheckPalyndrome(k1) == True):
			k2 = k1
			i11 = i1
			i21 = i2			
print(str(i11) + ' - '  + str(i21) + ' - ' + str(k2))			