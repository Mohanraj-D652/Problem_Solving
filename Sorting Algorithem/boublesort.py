def function(arr):

    
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    print(arr)
function(arr=[2,34,5,43,578,4,2,0,1,8])
