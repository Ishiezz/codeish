class Solution:
    def addDigits(self, num: int) -> int:
        if num<=9:
            return num
        ans=(num%10)+self.addDigits(num//10)
        if ans<=9:
            return ans
        else:
            return self.addDigits(ans)
