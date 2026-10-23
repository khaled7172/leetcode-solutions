class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        indexes = []
        values = []

        for i, v in enumerate(s):
            if v in vowels:
                indexes.append(i)
                values.append(v)

        reversed_values = values[::-1]

        s_list = list(s)
        for idx, val in zip(indexes, reversed_values):
            s_list[idx] = val

        return "".join(s_list)


        