class Solution(object):
    def searchInsert(self, nums, target):
        n=len(nums)
        hi=n-1
        lo=0
        posi=n
        while hi>=lo:
            mid=(lo+hi)//2
            if nums[mid]>=target:
                posi= mid
                hi=mid-1
            else:
                lo=mid+1
        return posi

        