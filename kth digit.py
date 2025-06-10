a=12
b=11
k=4
result=1
count=0
for i in range(b):
    result=result*a
print(result)

while(result>0):
    kth=result%10
    count=count+1
    
    result=result//10
    if(count==k ):
      print(kth)