arr =  [1, 2, 3, 4, 5]

n = len(arr) -1
x=arr[n]
print(arr[n])

for i in range(n,0,-1):
    # unwanted statement because if the condition is not satisfied the swaping is not happening  thats the reason : " if arr[i-1] < arr[i]:"
    arr[i] = arr[i-1]
# arr[0] = x
print(arr)

    # print(arr[i-1])
# print(arr[n])