class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # number and their frequency sorted in descending.
        
        dictt = dict()
        for x in nums:
            if x in dictt:
                dictt[x] += 1
            else: dictt[x] = 1
        
        res = sorted(dictt.items(), key = lambda x: x[1])
        print(res)
        res = [x[0] for x in res]
        print(res)
        print(res[len(res)-k:])
        return res[len(res)-k: ]

        # how to sort a dictionary:
        # sorted(dictt.items(), key  = lambda x: x[1]):
        # This returns the (key, val) in sorted order of values. 
        # Now just do whatever way you wnat to report the output. 
    

        