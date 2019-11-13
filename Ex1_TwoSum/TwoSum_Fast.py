
def twoSum(self, nums: List[int], target: int) -> List[int]:

    need_nums = {} # use a dictionary to store needed number
                    # cause the target we need would be a sum of two number
                    # we could store what we need first, then once we meet that num
                    # we could just return them at once

    for i in range(len(nums)):
        if nums[i] in need_nums:
            # if current number is already in needed numbers
            return [need_nums.get(nums[i]), i]
        else:
            # else we just add a expected needed value to need_nums
            need_nums[target - nums[i]] = i
