n=4

for i in range(n+1,0,-1):
    for j in range(n+1-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()