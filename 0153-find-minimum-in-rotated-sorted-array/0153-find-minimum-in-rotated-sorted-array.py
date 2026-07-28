class Solution(object):
    def findMin(self, nums):
        n=len(nums)
        low=0
        high=n-1
        minm=float('inf')
        while low<=high:
            mid=(low+high)//2
            if nums[mid]<=nums[high]:
                minm=min(minm,nums[mid])
                high=mid-1
            else:
                minm=min(minm,nums[low])
                low=low+1
        return minm
        