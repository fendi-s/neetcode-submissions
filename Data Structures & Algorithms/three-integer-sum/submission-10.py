class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            if i < 0:
                break

            lo, hi = i + 1, n - 1
            while lo < hi:
                total = nums[i] + nums[lo] + nums[hi]

                if total < 0:
                    lo += 1
                elif total > 0:
                    hi -= 1
                else:
                    ans.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    while nums[lo] == nums[lo-1] and lo < hi:
                        lo += 1

        return ans
