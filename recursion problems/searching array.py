def search(arr, length, i, target):

    if i >= length:
        return -1
    
    elif arr[i] == target:
        return True
    
    # print(arr[i])                          # we need to print array value before the boolean value
    return search(arr, length, i+1, target)

def main():
    arr = [33,543,254,456]
    length = len(arr)
    result = search(arr, length, 0, 456)
    print(result)
main()