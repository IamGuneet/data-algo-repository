class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        op =[]
        for i in nums:
            frequency[i]=frequency.get(i,0)+1
        keys = sorted(frequency.items(),key = lambda x: x[1] ,reverse=True)[:k]
        return [item[0] for item in keys]