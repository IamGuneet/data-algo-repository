class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs ={}

        for i in range(len(nums)):
            two_sum = target - nums[i]
            if two_sum in pairs:
                return [pairs.get(two_sum),i]
            else:
                pairs[nums[i]]=i
        