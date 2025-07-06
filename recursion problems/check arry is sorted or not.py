def check(arr, length, index):
    if index >= length-1:
        return True
    if arr[index] > arr[index+1]:
        return False
    return check(arr,length, index +1)
def main():
    arr=[1,2,3,4,5]
    length = len(arr)
    result = check(arr, length, 0)
    print(result)
main()

