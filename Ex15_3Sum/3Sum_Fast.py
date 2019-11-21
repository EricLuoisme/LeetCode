
def threeSum(nums):

    # this implementation is about sorting the whole list first, then
    # from the left to right, use a pointer i to represent the smallest
    # val (left ele in 3Sum). Then from it's next element (middle ele in 3Sum)
    # and the end of sorted list (right ele in 3Sum), narrow them. And finally
    # find all possible combination to reach 0.

    nums = sorted(nums)
    results = []

    for i in range(len(nums)-2):

        if i > 0 and nums[i] == nums[i-1]: # we can skip them
            continue

        middle = i + 1
        right = len(nums) - 1
        while middle < right:
            sum = nums[i] + nums[middle] + nums[right]
            if sum > 0: # means r is too large, need to find a smaller one
                right -= 1
            elif sum < 0: # means m is too small, need to find a larger one
                middle += 1
            else:
                results.append([nums[i], nums[middle], nums[right]])
                while middle < right and nums[middle] == nums[middle + 1]:
                    # because we do not need to add duplicated ele
                    # also, if middle already 'greater' then right
                    # we can stop
                    middle += 1
                while middle < right and nums[right] == nums[right - 1]:
                    right -= 1

                # from the above two while actions, we will still results
                # in same value of middle and right. We need to move them
                # manually
                middle += 1
                right -= 1

    return results


s = [-1, 0, 1, 2, -1, 4]
print(threeSum(s))
