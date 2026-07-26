class Solution(object):
    def lowerbound(self,nums,target):
        n=len(nums)
        hi=n-1
        lo=0
        lb=-1
        while lo<=hi:
            mid=(lo+hi)//2
            if nums[mid]>=target:
                lb=mid
                hi=mid-1
            else:
                lo=mid+1
        return lb

    def upperbound(self,nums,target):
        n=len(nums)
        hi=n-1
        lo=0
        up=-1
        while lo<=hi:
            mid=(lo+hi)//2
            if nums[mid]<=target:
                up=mid
                lo=mid+1
            else:
                hi=mid-1
        return up
    def searchRange(self, nums, target):
        first=self.lowerbound(nums,target)
        if first==-1 or nums[first]!=target:
            return [-1,-1]
        last=self.upperbound(nums,target)
        return [first,last]
        

        