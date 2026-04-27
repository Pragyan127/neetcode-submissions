class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)
        for n in num_set:
            if n-1 not in num_set:
                long = 0
                while (n+long) in num_set:
                    long += 1
                longest = max(long, longest)
        return longest

                


        