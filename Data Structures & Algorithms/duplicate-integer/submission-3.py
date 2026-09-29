class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_l = []
        for i in nums:
            if i in new_l:
                return True
            else:
                new_l.append(i)
        return False
            
