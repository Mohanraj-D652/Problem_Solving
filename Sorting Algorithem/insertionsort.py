a=[2,33,4,63,1,55,69,0,22,3]
for i in range(1,len(a)):
    key = a[i]
    j=i-1
    while(j >= 0 and key < a[j]):
        a[j+1] = a[j]
        j=j-1
    a[j+1] = key
print(a)