import math
L1=10
R1=20

prime=[True] * (R1+1)

prime[0]=prime[1]=False

for i in range(2, int(math.sqrt(R1))+1):

    if(prime[i]):

        for j in range(i*i, R1+1, i):
            prime[j]=False
primes=[i for i in range(L1,R1+1) if prime[i]]

print(primes)



