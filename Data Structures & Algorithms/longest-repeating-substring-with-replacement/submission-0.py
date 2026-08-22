class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


# YXYYXZZY
# l
#     r

# count[s[r]] += 1          count = {"X" : 3, Y : 2}
# max_freq = max(count.values())
# while (r - l + 1) - max_freq > k 

        left = 0
        max_freq = 0
        count = {}
        output = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1

            max_freq = max(count.values())

            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            output = max(output, right - left + 1)

        return output

