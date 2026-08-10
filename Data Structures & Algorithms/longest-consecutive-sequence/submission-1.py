class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_seq = 0

        for num in nums:

            if num-1 not in num_set:
                curr_num = num
                curr_seq = 1

                while curr_num+ 1 in num_set:
                    curr_seq += 1
                    curr_num += 1
            
                longest_seq = max(longest_seq,curr_seq)
        return longest_seq