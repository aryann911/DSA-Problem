class Solution(object):
    def maxSubArray(self, nums):
        max_sum=nums[0]
        total=nums[0]
        for i in range(1,len(nums)):
            total=max(nums[i],total+nums[i])
            max_sum=max(total,max_sum)

        return max_sum
        


        