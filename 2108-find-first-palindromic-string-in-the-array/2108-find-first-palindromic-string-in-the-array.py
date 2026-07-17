class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        tmp = ""
        string = ""
        for word in words:
            string += word[::-1]
            if string == word:
                return string
            else:
                string = ""
        return tmp