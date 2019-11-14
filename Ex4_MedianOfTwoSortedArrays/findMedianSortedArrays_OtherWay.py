
import random

def findMedianSortedArrays(nums1, nums2) -> float:
    # by using the sort() method in python, the fastest way
    # nums3 = nums1 + nums2
    # nums3.sort()
    #
    # if len(nums3) % 2 == 1:
    #     return nums3[int(len(nums3)/2)]
    # else:
    #     nu = int(len(nums3)/2)
    #     return (nums3[nu] + nums3[nu - 1])/2


    # by using the quick select algorithm. Finding the median in a list with length
    # in 11, would be the 6th smallest element
    nums3 = nums1 + nums2
    pivot = random.randint(0, len(nums3) - 1) # randomly pick a pivot

    if len(nums3) % 2 == 1: # odd number of length, only one element as median
        return kthQuickSelect(nums3, len(nums3)//2, nums3[pivot])
    else:
        mid = len(nums3)//2
        return (kthQuickSelect(nums3, mid - 1, nums3[pivot]) + \
            kthQuickSelect(nums3, mid, nums3[pivot]))/2


def kthQuickSelect(elements, kth, pivot):
    # implementing kth quick select algorithm

    if len(elements) == 1: # means we only have one elements in this list
                            # it should be the smallest
        # assert(kth == 0) # then k should be 0

        if kth != 0:
            print(elements)

        return elements[0]

    low = [] # store the elements that less than to the pivot
    hig = [] # store the elements that greater than pivot
    equ = [] # store the elements that is equal to the pivot

    for ele in elements:
        if ele < pivot:
            low.append(ele)
        elif ele > pivot:
            hig.append(ele)
        else:
            equ.append(ele)

    if kth < len(low): # means what we need to find is in the LOW partition
        nw_pivot = random.randint(0, len(low)-1)
        return kthQuickSelect(low, kth, low[nw_pivot])
    elif kth < len(low) + len(equ): # mean kth is greater than low but not grater than
                                    # pivot. Which means the pivot sould be the median
        return pivot
    else: # means kth is in hig
        nw_pivot = random.randint(0, len(hig) - 1)
        return kthQuickSelect(hig, kth - len(low) - len(equ), hig[nw_pivot])


print(findMedianSortedArrays([1,2], [3,4]))
