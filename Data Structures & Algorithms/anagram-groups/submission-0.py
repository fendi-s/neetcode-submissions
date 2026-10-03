class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i, s in enumerate(strs):
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            anagrams.setdefault(tuple(count), []).append(s)
        
        return list(anagrams.values())
