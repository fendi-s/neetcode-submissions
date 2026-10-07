class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        length = 0
        for start in nums:
            if (start - 1) not in nums_set:
                end = start + 1
                while end in nums_set:
                    end += 1
                length = max(length, end - start)
        return length