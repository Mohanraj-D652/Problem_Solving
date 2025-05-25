n=int(5)

for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print("")
    
for k in range(1,n):
    for l in range(n-k):
         print("*",end=" ")
    print("")