class Solution:
    def calPoints(self, operations: List[str]) -> int:
        out=[]
        sum=0
        for i in operations:
            if i =='+':
                score=out[-1]+out[-2]
                out.append(score)
            elif i=='D':
                score=out[-1]*2
                out.append(score)
            elif i=='C':
                out.pop(-1)
            else:
                out.append(int(i))
            
        for i in out:
            sum+=i
        return sum
        