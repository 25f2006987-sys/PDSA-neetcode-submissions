class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n=len(people)
        people.sort()
        pointer1=0
        pointer2=n-1
        count=0
        while pointer1<=pointer2:
            if people[pointer1]+people[pointer2] <= limit:
                pointer1+=1
                pointer2-=1
                count+=1
            elif people[pointer1]+people[pointer2] > limit:
                count+=1
                pointer2-=1
        return count
        