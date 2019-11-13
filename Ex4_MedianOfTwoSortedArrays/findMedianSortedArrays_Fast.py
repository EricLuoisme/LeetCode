
# Example 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
# Example 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5


def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    # really simple solution, just join two sorted lists into in sorted list, then
    # find the median number on the basis of odd or even number in that sorted list

    nums3 = [] # is the list we store to return
    if len(nums1) == 0:
        nums3 = nums2
    elif len(nums2) == 0:
        nums3 = nums1
    else:
        i_n = 0
        i_m = 0
        char_1 = nums1[i_n]
        char_2 = nums2[i_m]
        while i_n < len(nums1) or i_m < len(nums2):
            if char_1 < char_2:
                nums3.append(char_1)
                i_n += 1
                if i_n < len(nums1):
                    char_1 = nums1[i_n]
                else:
                    # only nums2 have elements
                    for k in range(i_m, len(nums2)):
                        nums3.append(nums2[k])
                    break
            else:
                nums3.append(char_2)
                i_m += 1
                if i_m < len(nums2):
                    char_2 = nums2[i_m]
                else:
                    # only nums1 have elements
                    for k in range(i_n, len(nums1)):
                        nums3.append(nums1[k])
                    break

    if len(nums3) % 2 == 1: # odd number, would have exactly one median number
        return nums3[int(len(nums3)/2)]
    else:
        nu = int(len(nums3)/2)
        return (nums3[nu] + nums3[nu - 1])/2
