class Solution:
    def isPalindrome(self, s: str) -> bool:
        list1=[]
        for k in s:
            if k.lower() in 'abcdefghijklmnopqrstuvwxyz0123456789':
                list1.append(k)
        print (list1)
        
        n=len(list1)

        for i in range (n//2):
            if list1[i].lower()!=list1[-i-1].lower():
                return False
        return True
        