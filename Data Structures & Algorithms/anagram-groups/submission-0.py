class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashh = {}
        for val in strs:
            sortt = "".join(sorted(val))
            
            if sortt not in hashh: # if sorted value not in key of dictionary.
                hashh[sortt] = [val]
            else:
                hashh[sortt].append(val)
        print(list(hashh.values()))
        return list(hashh.values())
        
        
        