class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        for n in nums:
            if n-1 not in nums:
                long = 0
                while (n+long) in nums:
                    long += 1
                longest = max(long, longest)
        return longest

                


        