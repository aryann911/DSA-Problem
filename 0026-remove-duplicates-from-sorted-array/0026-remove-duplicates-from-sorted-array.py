class Solution(object):
    def removeDuplicates(self, nums):
        i=0
        j=i+1
        if len(nums)==1:
            return 1
        while j<len(nums):
            if nums[j]!=nums[i]:
                i+=1
                nums[i],nums[j]=nums[j],nums[i]
            j+=1
        return i+1

        