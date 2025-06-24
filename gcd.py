a = 15
b = 25

add = 1
if(a > b):
    gcd=(b , a)
else:
    gcd=(a , b)
        
for i in range(2,a+1):
    if(a % i == 0 and b % i == 0):
        add = i
print (add)