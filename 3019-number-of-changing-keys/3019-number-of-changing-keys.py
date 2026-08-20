class Solution:
    def countKeyChanges(self, s: str) -> int:
        prev_key = s[0].lower()
        count = 0
        curr_key = None
        for l in s[1:]:
            curr_key = l.lower()
            if curr_key == prev_key:
                continue
            else:
                count += 1
                prev_key = curr_key
        return count
            
