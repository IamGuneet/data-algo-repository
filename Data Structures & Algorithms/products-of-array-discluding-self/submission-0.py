class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = {}
        suffix = {}
        for  i,n in enumerate(nums):
            prefix[i] = prefix.get(i-1,1)*n
        print(prefix) 
        for j in range(len(nums)-1,-1,-1):
            suffix[j] = suffix.get(j+1,1)*nums[j]
        print(suffix) 
        res = []
        for i in range(len(nums)):
            left_product = prefix.get(i-1,1)
            right_product = suffix.get(i+1,1)
            res.append(left_product*right_product)
        return res