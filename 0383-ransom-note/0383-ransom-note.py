class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_dict = {}
        ransom_dict = {}
        for l in magazine:
            if l not in mag_dict:
                mag_dict[l] = 1
            else:
                mag_dict[l] += 1
        for k in ransomNote:
            if k not in ransom_dict:
                ransom_dict[k] = 1
            else:
                ransom_dict[k] += 1
        for key, value in ransom_dict.items():
            for k, v in mag_dict.items():
                if key not in mag_dict:
                    return False
                elif key == k:
                    if value > v:
                        return False
        print(ransom_dict)
        print(mag_dict)
        return True