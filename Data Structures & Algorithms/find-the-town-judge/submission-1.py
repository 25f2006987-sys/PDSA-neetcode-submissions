class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree={}
        outdegree={}
        for i in range(n):
            indegree[i+1]=0
            outdegree[i+1]=0

        for i in trust:
            first=i[0]
            second=i[1]
            indegree[second]=indegree.get(second,0)+1
            outdegree[first]=outdegree.get(first,0)+1
        
        for i in indegree.keys():
            if indegree[i]==n-1 and outdegree[i]==0:
                return i
        return -1