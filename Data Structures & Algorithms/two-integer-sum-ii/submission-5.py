class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mapped = {}

        for i,num in enumerate(numbers):
            rev_sum = target - num
            if rev_sum in mapped:
                print([mapped[rev_sum],i])
                return [mapped[rev_sum]+1,i+1]

            mapped[num] = i
        return list()