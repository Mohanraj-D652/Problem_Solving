def main(arr,l, i):
    
    if i >= l:
        return
    else:
        print(arr[i])
        return main(arr,l, i+1)
    
def sc():
    arr=[12,33,45,6664]
    l = len(arr)
    
    main(arr,l, 0)
sc()