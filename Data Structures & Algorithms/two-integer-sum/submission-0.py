class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output_list = []
        to_find = None
        for i in range(len(nums)):
            nums_2 = nums.copy()
            if to_find == None:
                to_find = target - nums[i]
                nums_2.remove(nums[i])
                if to_find in nums_2:
                    output_list.append(i)
                else:
                    to_find = None
            else:
                if nums[i] == to_find:
                    output_list.append(i)
                    break
            
        return output_list
            