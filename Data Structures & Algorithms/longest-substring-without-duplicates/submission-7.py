class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        seen = []
        longest = 1

        for char in s:
            if char in seen:
                longest = max(len(seen), longest)
                idx = seen.index(char)
                seen = seen[idx+1:]
            
            seen.append(char)
        return max(len(seen), longest)