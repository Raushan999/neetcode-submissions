class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums)<=1: return False
        
        set1 = set()
        set1.add(nums[0])
        for x in nums[1:]:
            if x in set1: return True
            set1.add(x)
        return False
