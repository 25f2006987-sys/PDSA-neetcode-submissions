class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import math
        print(points)
        dist=[]
        for pair in points:
            x=pair[0]
            y=pair[1]
            dist.append((pair,math.sqrt(x*x+y*y)))
        dist.sort(key=lambda x : x[1])
        print (dist)
        out=[]
        for i in range(k):
            out.append(dist[i][0])
        return out
            
