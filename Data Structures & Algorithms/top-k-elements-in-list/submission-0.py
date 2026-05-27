class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # number and their frequency sorted in descending.
        dictt = dict()
        for x in nums:
            if x in dictt:
                dictt[x] += 1
            else: dictt[x] = 1
        res = [key for key, val in sorted(dictt.items(), key = lambda x: x[1], reverse = True) ]
        return res[:k]
    

        