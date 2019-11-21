
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


def threeSum(nums):

    # too slow to pass the LeetCode tests

    results = []

    T = [['None']*len(nums) for i in range(len(nums))]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            T[i][j] = - (nums[i] + nums[j])

    # find all possible combinations
    for i in range(len(nums)):
        found = [(ix, iy) for ix, row in enumerate(T) \
                                for iy, val in enumerate(row) \
                                if val == nums[i] and ix != i and iy != i]

        for f in found:
            (x, y) = f
            notHas = True
            this_sol = [nums[x], nums[y], nums[i]]
            # if len(this_sol) > 0:
            for all in results:
                if set(all) == set(this_sol):
                    notHas = False
                    break
            if notHas:
                results.append(sorted(this_sol)) # use this method to sort list

    return sorted(results)

s = [-11,-3,-6,12,-15,-13,-7,-3,13,-2,-10,3,12,-12,6,-6, \
12,9,-2,-12,14,11,-4,11,-8,8,0,-12,4,-5,10,8,7,11,-3,7,5, \
-3,-11,3,11,-13,14,8,12,5,-12,10,-8,-7,5,-9,-11,-14,9,-12, \
1,-6,-8,-10,4,9,6,-3,-3,-12,11,9,1,8,-10,-3,2,-11,-10,-1,1,\
-15,-6,8,-7,6,6,-10,7,0,-7,-7,9,-8,-9,-9,-14,12,-5,-10,-15,-9,\
-15,-7,6,-10,5,-7,-14,3,8,2,3,9,-12,4,1,9,1,-15,-13,9,-14,11,9]
print(threeSum(s))
