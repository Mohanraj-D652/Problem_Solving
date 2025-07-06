def sum(arr, length, index):
    if index >= length:
        return 0
    else:
        return arr[index] + sum(arr, length, index + 1)
def main():
    arr = [1,2,3,4,5]
    length = len(arr)
    result = sum(arr, length, 0)
    print(result)
main()