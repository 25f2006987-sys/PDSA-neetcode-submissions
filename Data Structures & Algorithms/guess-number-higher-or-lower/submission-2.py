# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        while low <= high:
            curr = (low + high) // 2
            g = guess(curr)
            if g == 0:
                return curr
            elif g == -1:
                high = curr - 1
            else:
                low = curr + 1
