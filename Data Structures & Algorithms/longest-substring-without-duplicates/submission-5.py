class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxl = 0
        c = set()
        
        for right in range(len(s)):
            while s[right] in c:
                c.remove(s[left])
                left += 1
            c.add(s[right])
            maxl = max(maxl, right - left + 1)
                
        return maxl