class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ps=[0]*n
        ps[0]=nums[0]
        for i in range(0,n):
            ps[i]=ps[i-1]+nums[i]
        return ps 
        
