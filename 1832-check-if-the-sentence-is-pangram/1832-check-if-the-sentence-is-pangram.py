class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        visited = set(sentence)
        if len(visited) == 26:
            return True
        return False
        