class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")

        reversed_vowels = [ch for ch in s if ch in vowels][::-1]

        s_list = list(s)
        v_idx = 0
        for i in range(len(s_list)):
            if s_list[i] in vowels:
                s_list[i] = reversed_vowels[v_idx]
                v_idx += 1
        return "".join(s_list)


        