'''
Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.
'''

def binary_search(arr,l,r,x):
    if l>r: 
        return -l-1

    mid=(l+r)//2
    if x==arr[mid]:
        return mid
    if x<arr[mid]:
        return binary_search(arr,l,mid-1,x)
    return binary_search(arr,mid+1,r,x)
   
def binary_insert(arr,x):
    idx = binary_search(arr,0,len(arr)-1,x)
    if idx<0:
        idx= -idx-1
    arr.insert(idx,x)


def max_sub_k_arr_ONK(arr,k):
    n=len(arr)
    if k>=n: return None

    ret=[]
    karr=[]
    for i in range(k-1):
        binary_insert(karr,arr[i])
    
    for i in range(k-1,n):
        binary_insert(karr,arr[i])
        ret.append(karr[-1])
        print(karr)
        idx= binary_search(karr,0,k-1,arr[i-k+1])
        del karr[idx]

    return ret    


'''
    if the ith value is the largest value , remove all the remain on the k list 
'''
def max_sub_k_arr_ON(arr,k):
    n=len(arr)
    ret =[]

    Qi=[] #max quere index 
    for i in range(k):

        # For every element, the previous
        # smaller elements are useless
        # so remove them from Qi
        while Qi and arr[i]>arr[Qi[-1]]:
            del Qi[-1]
        Qi.append(i)

    for i in range(k,n):

        # The element at the front of the
        # queue is the largest element of
        # previous window, so print it        
        ret.append(arr[Qi[0]])
        
        #remove out of slide window
        while Qi and Qi[0]<=i-k:
            del Qi[0]
        
        while Qi and arr[i]>arr[Qi[-1]]:
            del Qi[-1]

        Qi.append(i)

    ret.append(arr[Qi[0]])

    return ret

from collections import deque
def max_sub_k_arr_ON_using_queue(arr,k):
    n=len(arr)
    ret =[]

    Qi = deque() #max quere index 
    for i in range(k):
        #insert int to Qi
        while Qi and arr[i]>arr[Qi[-1]]:
            Qi.pop()
        Qi.append(i)

    for i in range(k,n):
        ret.append(arr[Qi[0]])
        #remove out of slide window
        while Qi and Qi[0]<=i-k:
            Qi.popleft()
        
        while Qi and arr[i]>arr[Qi[-1]]:
            Qi.pop()

        Qi.append(i)

    ret.append(arr[Qi[0]])

    return ret    

arr =[10, 5, 2, 7, 8, 7]
arr = [12, 1, 78, 90, 57, 89, 56]
print(max_sub_k_arr_ON(arr,3))

