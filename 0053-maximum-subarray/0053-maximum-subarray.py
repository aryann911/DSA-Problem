class Solution(object):
    def maxSubArray(self, nums):
        total=0
        max_sum=float('-inf')
        for i in range(0,len(nums)):
            total=total+nums[i]
            max_sum=max(total,max_sum)
            if total <0:
                total=0
        return max_sum
        


        