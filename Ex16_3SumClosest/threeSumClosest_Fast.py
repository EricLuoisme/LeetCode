
def threeSumClosest(nums, target: int) -> int:

    nums = sorted(nums)
    dif = float('inf')

    for pointer in range(len(nums) - 2):

        if pointer > 0 and nums[pointer - 1] == nums[pointer]:
            continue
            # skip the one we might calculated before

        min = int(nums[pointer]) + int(nums[pointer + 1]) + int(nums[pointer + 2])
        max = int(nums[pointer]) + int(nums[-2]) + int(nums[-1])
        # by calculating the maximum and minimum sum, we can 'pruning' some
        # situations

        if min >= target:
            # if this turn's minimum sum is already greater than target
            if abs(target - min) >= abs(dif):
                # also, it's difference with target is greater then previous one
                # we can stop searching, cause we move pointer left to right,
                # the sum would only increasing.
                return target - dif
            # but, it the difference is smaller than previous one, we might still
            # need to check in (min, max), to find the closest value.

        if max < target:
            # if this turn's maximum sum is already smaller than target
            if abs(target - max) < abs(dif):
                # here we still need to recorde that if it's difference
                # is already closer than the previous one, we need to store it
                dif = target - max
            continue
            # we need to consider increase the pointer and start another turn

        # after pruning, we need to check possible situations in (min, max)
        left, right = pointer + 1, len(nums) - 1
        while left < right:
            this_sum = int(nums[pointer]) + int(nums[left]) + int(nums[right])
            if abs(target - this_sum) < abs(dif):
                dif = target - this_sum

            if this_sum == target:
                return target

            elif this_sum < target:
                left += 1
                while left < len(nums) - 1 and nums[left] == nums[left - 1]:
                    left += 1
                # here is about skipping the repeated situations
                # e.g. [pointer, 1, 1, 1, 1, 1], cause we had already
                # calculated [pointer, 1_first, 1_last] before
                # but we have to check [left - 1] # what we calculated
                # and [left] current one.

            else: # this_sum > target
                right -= 1
                while right > 0 and nums[right] == nums[right + 1]:
                    right -= 1
                # here is about skipping the repeated situations
                # e.g. [pointer, 1, 1, 1, 1, 1], cause we had already
                # calculated [pointer, 1_first, 1_last] before

    return target - dif


nums = [-1,0,1,1,55]
target = 3

print(threeSumClosest(nums, target))
