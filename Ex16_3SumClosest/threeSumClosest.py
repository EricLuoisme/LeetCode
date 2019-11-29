
def threeSumClosest(nums, target: int) -> int:

    # start from left to right

    nums = sorted(nums)
    dif = float('inf')

    for pointer in range(len(nums) - 1):

        if pointer > 0 and nums[pointer] == nums[pointer - 1]:
            continue
            # skip some situations that pointer[val] == left[val]

        left_p = pointer + 1
        right_p = len(nums) - 1

        while left_p < right_p:
            sum_all = int(nums[pointer]) + int(nums[left_p]) + int(nums[right_p])
            # write all together can make it faster

            if sum_all > target:
                right_p -= 1
            elif sum_all < target:
                left_p += 1
            else:
                # here is about left_num + right_num + 0 == target - pointer
                return target

            this_dif = target - sum_all
            if abs(this_dif) < abs(dif):
                dif = this_dif

    return target - dif


nums = [-1,0,1,1,55]
target = 3

print(threeSumClosest(nums, target))
