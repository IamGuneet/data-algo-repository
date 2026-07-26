class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pairs = {}
        op =[]
        for idx, num in enumerate(numbers):
            pair = target - num
            if pair in pairs:
                op.append(pairs[pair]+1)
                op.append(idx+1)

            pairs[num] = pairs.get(num,idx)
            
        return op