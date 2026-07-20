class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        maxlen = 0
        if len(s) == 1:
            return 1
        for idx, char in enumerate(s):
            if char in last_seen and left<=last_seen[char]:
                    left = last_seen[char] + 1
            
            last_seen[char] = idx
            maxlen = max(maxlen, (idx-left+1))
        return maxlen 