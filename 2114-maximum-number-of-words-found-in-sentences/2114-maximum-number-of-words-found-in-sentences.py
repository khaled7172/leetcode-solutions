class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_len = 0
        for sentence in sentences:
            tmp = sentence.split(' ')
            tmp_len = len(tmp)
            if tmp_len > max_len:
                max_len = tmp_len
        return max_len
        