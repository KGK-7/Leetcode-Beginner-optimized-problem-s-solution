class Solution(object):
    def isPerfectSquare(self, num):
        
        if num < 2 and num >= 0:
            return True

        x=num//2

        while x*x > num:
            x= (x+ num//x)//2

        return x*x ==num