class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        pointer1=0
        pointer2=n-1
        while pointer1<=pointer2:
            if numbers[pointer1]+numbers[pointer2]==target:
                return [pointer1+1, pointer2+1]
            elif numbers[pointer1]+numbers[pointer2]>target:
                pointer2-=1
            else:
                pointer1+=1
            