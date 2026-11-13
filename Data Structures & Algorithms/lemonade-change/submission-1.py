class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        chg=[0,0,0]
        for i in bills:
            if i==5:
                chg[0]+=1
            elif i==10:
                if chg[0]==0:
                    return False
                else:
                    chg[0]-=1
                    chg[1]+=1
            elif i==20:
                if (chg[0]<3 and chg[1]==0 ) or (chg[0]==0):
                    return False

                elif chg[0]>0 and chg[1]>0:
                    chg[0]-=1
                    chg[1]-=1
                else:
                    chg[0]-=3
        return True
