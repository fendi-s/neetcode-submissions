class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for i in range(len(nums)):
            num = nums[i]
            if target - num in temp:
                return [temp[target - num], i]
            temp[num] = i
        