class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""
        
        for i, char_tuple in enumerate(zip(*strs)):
            if len(set(char_tuple)) > 1:
                return strs[0][:i]
                
        return min(strs, key=len)