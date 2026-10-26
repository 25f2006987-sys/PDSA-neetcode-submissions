class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        max_len = min(len(s) for s in strs)
        list1, list2 = [], [""]
        
        for i in range(1, max_len + 1):
            list1 = [k[:i] for k in strs]
            
            if len(set(list1))==1:
                list2=list1.copy()  
        if len(strs)==1:
            return (strs[0])
        else:
            return(list2[0])

