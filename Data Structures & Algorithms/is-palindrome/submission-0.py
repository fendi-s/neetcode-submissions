import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        clean_text = "".join(s.split())
        translator = str.maketrans("", "", string.punctuation)

        translate = clean_text.translate(translator)
        
        if translate == translate[::-1]:
            return True
        
        return False