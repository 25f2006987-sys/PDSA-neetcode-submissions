class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        degree={}
        for i in range(n):
            degree[i+1]=0

        for i in trust:
            first=i[0]
            second=i[1]
            degree[first]-=1
            degree[second]+=1
        for i in degree.keys():
            if degree[i]==n-1:
                return i
        return -1