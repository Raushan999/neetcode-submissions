class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
##1. brute force code.
        # for i in range(0, len(nums)):
        #     search = target -  nums[i]
        #     for j in range(i+1, len(nums)):
        #         if search == nums[j]: return [i, j]
        # return [0, 0]

##2. Optimzed code: Hash Map
        # hash_map = {} # dictionary. 
        # for i, val in enumerate(nums):
        #     hash_map[val] = i # store the indices 
        # for i, val in enumerate(nums):
        #     search = target - val
        #     if search in hash_map and (hash_map[search] != i):
        #         return [i, hash_map[search]]
        # return []

##3. One Pass Hash Map
        hash_map = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff not in hash_map:
                hash_map[val] = i
            else: 
                return [hash_map[diff], i]
