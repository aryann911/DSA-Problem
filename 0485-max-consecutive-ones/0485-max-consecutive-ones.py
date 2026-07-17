class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count=0
        temp=0
        for i in range(0,len(nums)):
            if nums[i]==1:
                count+=1
            else:
                temp=max(temp,count)
                count=0
        return max(temp,count)
        