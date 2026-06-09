class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ## Time optimized code:- 
        forward_prod = list()
        backward_prod = list()
        f1 = nums[0]
        b1 = nums[-1]
        forward_prod.append(f1)
        backward_prod.append(b1)
        for x in nums[1:]:
            f1 *= x
            forward_prod.append(f1)
        rev = nums[::-1]
        for x in rev[1:]:
            b1 *= x
            backward_prod.append(b1)
        backward_prod = backward_prod[::-1]
        result = [0]*len(nums)
        result[0] = backward_prod[1]
        result[-1] = forward_prod[-2]
        for i in range(1, len(nums)-1):
            result[i] = forward_prod[i-1] * backward_prod[i+1]
        return result

            
        