class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree={}
        outdegree={}
        for i in trust:
            first=i[0]
            second=i[1]
            indegree[second]=indegree.get(second,0)+1
            outdegree[first]=outdegree.get(first,0)+1
        in_list=list(indegree.items())
        in_list.sort(key=lambda x:-x[1])
        out_list=list(outdegree.items())
        out_list.sort(key=lambda x:x[1])
        print (in_list, out_list)
        if in_list[0][1]==n-1 and in_list[0][0] not in outdegree.keys():
            return in_list[0][0]
        return -1