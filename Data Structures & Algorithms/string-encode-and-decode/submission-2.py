class Solution:

    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""
        res = []
        for s in strs:
            # Structure: length + delimiter + string (e.g., "4#lint")
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings."""
        res = []
        i = 0
        
        while i < len(s):
            # Find the position of the '#' delimiter
            j = i
            while s[j] != '#':
                j += 1
            
            # Extract the string length between index i and j
            length = int(s[i:j])
            
            # Slice out the actual string body
            start_str = j + 1
            end_str = start_str + length
            res.append(s[start_str:end_str])
            
            # Advance the pointer past the extracted string
            i = end_str
            
        return res