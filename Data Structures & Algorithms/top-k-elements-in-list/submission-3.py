class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            counts[n] = 1 + counts.get(n, 0)
        for num, count in counts.items():
            freq[count].append(num)
        
        res = []
        for i in range(len(nums), 0, -1):
            for n in freq[i]:
                if n != []:
                    res.append(n)
            if len(res) == k:
                return res