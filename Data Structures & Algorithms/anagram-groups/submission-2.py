class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for k in strs:
            tmp=''.join(sorted(k))
            if tmp in d.keys():
                d[tmp].append(k)
            else:
                d[tmp]=[k]
        return list(d.values())

