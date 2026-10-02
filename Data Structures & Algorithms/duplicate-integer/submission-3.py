class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for i in range(len(nums)):
            count.setdefault(nums[i], 0)
            count[nums[i]] += 1
            if count[nums[i]] > 1:
                return True
        return False