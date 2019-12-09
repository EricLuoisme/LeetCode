
# By reducing the N-sum to 3-sum (slower then reducing it to 2-sum)

def fourSum(nums, target: int):
    nums = sorted(nums)
    temp_head = []
    results = []
    N = 4
    temp_head, results = reduceToThreeSum(nums, target, N, temp_head, results)
    return results


def reduceToThreeSum(nums, semi_target, N, temp_head, results):

    if N == 3:
        for pointer_cur in range(len(nums) - 2): # need to take care to len(nums) - 2
            if pointer_cur > 0 and nums[pointer_cur] == nums[pointer_cur - 1]:
                continue    # skip the repeated one

            min = int(nums[pointer_cur]) + int(nums[pointer_cur + 1]) + int(nums[pointer_cur + 2])
            max = int(nums[pointer_cur]) + int(nums[-2]) + int(nums[-1])

            if min > semi_target or max < semi_target:
                continue

            pointer_left = pointer_cur + 1
            pointer_right = len(nums) - 1

            while pointer_left < pointer_right:
                the_sum = int(nums[pointer_cur]) + int(nums[pointer_left]) + int(nums[pointer_right])
                if the_sum == semi_target:
                    this_result = temp_head + [nums[pointer_cur], nums[pointer_left], nums[pointer_right]]
                    if this_result not in results:
                        results.append(this_result)
                    pointer_left += 1
                    pointer_right -= 1

                elif the_sum < semi_target:
                    pointer_left += 1
                    while pointer_left < pointer_right and nums[pointer_left] == nums[pointer_left - 1]:
                        pointer_left += 1

                else: # the_sum > semi_target
                    pointer_right -= 1
                    while pointer_left < pointer_right and nums[pointer_right] == nums[pointer_right + 1]:
                        pointer_right -= 1

        return temp_head[:-1], results

    else:   # N > 3
        for i in range(len(nums) - N + 1):
            if semi_target < nums[i] * N or semi_target > nums[-1] * N:
                continue
            if i == 0 or (i > 0 and nums[i - 1] != nums[i]):
                temp_head += [nums[i]]
                temp_head, results = reduceToThreeSum(nums[i + 1:], semi_target - int(nums[i]), N-1, temp_head, results)

    return temp_head, results


nums = [-1,-5,-5,-3,2,5,0,4]
target = -7
print(fourSum(nums, target))
