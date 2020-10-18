# euler project #5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def checkval(num1):
    for i in range(1, 21):
        if (num1 % i) == 0:
            g = 1
        else:
            g = 0
            break
    if (g == 1):
        return True
    else:
        return False


m = 222017240 # 2520
k = checkval(m)
while k != True:
    m = m + 20
    k = checkval(m)
  #  print(str(k) + ',' + str(m))
print(m)


