import random 
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def qsort(L,l,r):
            if (r<=l):
                return L
            rand_idx = random.randint(l, r)
            L[l], L[rand_idx] = L[rand_idx], L[l]
            small, big = l,l
            pivot = L[l]
            for j in range (l+1, r+1):
                if L[j] < L[l]:
                    small+=1
                    L[j],L[small]=L[small],L[j]
                    
                    big+=1
            L[small], L[l] = L[l], L[small]
            p=small
            n=len(L)
            qsort(L,l,small-1)
            qsort(L,small+1,r)
            return L
        l1=len(nums)
        return (qsort(nums, 0,l1-1 ))
     
        



        