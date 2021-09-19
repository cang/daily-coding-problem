def get_positive_subset(array):
    i = 0
    j = len(array) - 1

    while i < j:
        if array[i] > 0 and array[j] <= 0:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
        elif array[i] > 0:
            j -= 1
        else:
            i += 1

    # print("i: {}, j: {}".format(i, j))
    # print("partitioned_array:", array)
    pivot = i if array[i] > 0 else i + 1
    return array[pivot:]


def get_missing_number(array):
    if not array:
        return 1

    array = get_positive_subset(array)
    array_len = len(array)
    # print("array: {}".format(array))

    if not array:
        return 1

    if max(array) == len(array):
        return max(array) + 1

    for num in array:
        current_num = abs(num)
        if (current_num - 1) < array_len:
            array[current_num - 1] *= -1
    # print("mutated_array: {}".format(array))

    for i, num in enumerate(array):
        if num > 0:
            return i + 1

#test duplicate value 
assert get_missing_number([3, 4, -1, 1,1]) == 2
# how to remove duplicate value from get_positive_subset ? this must be the best way

assert get_missing_number([3, 4, -1, 1]) == 2
assert get_missing_number([1, 2, 0]) == 3
assert get_missing_number([1, 2, 5]) == 3
assert get_missing_number([1]) == 2
assert get_missing_number([-1, -2]) == 1
assert get_missing_number([]) == 1


#temporary, I use quicksort and binary search 1 (please remove my code when you fix duplicate issue)
def findMissingPositiveInt(list):
    n=len(list)
    quickSort(list,0,n-1)
    idx = binarySeach(list,1,0,n-1)
    if idx<0:
        return 1#-idx-1
    else:
        for i in range(idx+1,n):
            if list[i]!=i-idx+1:
                return i-idx+1
        return n-idx+1

def quickSort(list,l,r):
    if l>r: return 
    mid=list[(l+r)//2];
    i,j=l,r
    while i<j:
        while list[i]<mid: i+=1
        while list[j]>mid: j-=1
        
        if i<=j:
            list[i],list[j]=list[j],list[i]
            i+=1
            j-=1
    
    if l<j:
        quickSort(list,l,j)
    if i<r:
        quickSort(list,i,r)

def binarySeach(list,x,l,r):
    '''
    if index negative, the inserted index will be -(result)-1
    '''
    if l>r: return -(l+1)
    mid=(l+r)//2;
    if x==list[mid]:
        return mid
    elif x<list[mid]:
        return binarySeach(list,x,l,mid-1)
    else:
        return binarySeach(list,x,mid+1,r)        

assert findMissingPositiveInt([3, 4, -1, 1,1]) == 2
