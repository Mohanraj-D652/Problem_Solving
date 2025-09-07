# def Mergesort(array):
#     if len(array) > 1:
        
#         middle = len(array) // 2
#         left = array[0:middle]
#         right = array[middle: len(array)]

#         Mergesort(left)
#         Mergesort(right)

#         lp = 0
#         rp = 0
#         fp = 0

#         while(len(left) > lp and len(right) > rp):

#             if left[lp] < right[rp]:
#                 array[fp] = left[lp]
#                 lp += 1
#             else:
#                 array[fp] = right[rp]
#                 rp += 1
#             fp += 1


#         while(len(left) > lp):
#             array[fp] = left[lp]
#             lp += 1
#             fp += 1

#         while(len(right) > rp):
#             array[fp] = right[rp]
#             rp += 1
#             fp += 1

# array = [5,4,3,2,6,7,9,8]
# print("default array: ",array)
# Mergesort(array)
# print("New sorted array: ",array)



def Merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2   # 4 // 2 = 2  , 2 // 2 = 1
        left = array[0:mid]
        right = array[mid:len(array)]

        Merge_sort(left)   # 2 // 2 = 1
        Merge_sort(right)  # 2 // 2 = 1
        

        lp = 0
        rp = 0
        kp = 0

        while(lp < len(left) and rp < len(right)):
            if left[lp] > right[rp]:
                array[kp] = right[rp]
                rp += 1
            else:
                array[kp] = left[lp]
                lp += 1
            kp += 1

        while(lp < len(left)):
            array[kp] = left[lp]
            lp += 1
            kp += 1
        while(rp < len(right)):
            array[kp] = right[rp]
            rp += 1
            kp += 1
 
array = [5,4,3,2,8,9,7,6,1,10,11,12,55,0]
Merge_sort(array)
print(array)