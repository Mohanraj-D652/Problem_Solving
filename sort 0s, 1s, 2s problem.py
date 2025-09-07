arr = [0,1,2,0,1,2]
zero = 0
one = 0
two = 0
        
for i in arr:
    if i == 0:
        zero += 1
    elif i == 1:
        one += 1
    else:
        two += 1
        
print(zero , one, two)
                
for j in range(0,zero):
    arr[j] = 0
for  j in range(zero,zero+one):
    arr[j] = 1
for j in range(zero+one,len(arr)):
    arr[j] = 2
    
print(arr)