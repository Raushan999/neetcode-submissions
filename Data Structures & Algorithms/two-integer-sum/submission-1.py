class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
##1. brute force code.
        # for i in range(0, len(nums)):
        #     search = target -  nums[i]
        #     for j in range(i+1, len(nums)):
        #         if search == nums[j]: return [i, j]
        # return [0, 0]

##2. Optimzed code
        n = len(nums)
        search_dict = dict() # hash map. 
        for i in range(0, n):
            search_dict[target - nums[i]] = i
        for i in range(0, n):
            if search_dict[nums[i]] and i != search_dict[nums[i]]:
                return sorted([i, search_dict[nums[i]]])