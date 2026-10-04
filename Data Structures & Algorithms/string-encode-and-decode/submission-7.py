class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"
        return res

    def decode(self, s: str) -> List[str]:
        # s = "5#Hello5#World"
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            word_len = int(s[i:j])
            word_i = j + 1
            res.append(s[word_i : word_i + word_len])
            i = word_i + word_len

        return res
