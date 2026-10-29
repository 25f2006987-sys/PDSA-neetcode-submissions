class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen={}
        count=0
        for i in nums:
            
            if i in seen.keys():
                print(seen)
                if abs(seen[i]-count)<=k:
                    return True
            
            seen[i]=count
            count=count+1
        return False
        