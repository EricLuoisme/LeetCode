
def twoSum(self, nums: List[int], target: int) -> List[int]:
        ret_list = []
        for i in range(0, len(nums)):
            i_val = nums[i]
            for j in range(i+1, len(nums)):
                if i_val + nums[j] == target:
                    ret_list.append(i)
                    ret_list.append(j)
                    return ret_list
