class Solution(object):
    def rearrangeArray(self, nums):
        pos=0
        nav=1
        n=len(nums)
        result=[0]*n
        for num in nums:
            if num>0:
                result[pos]=num
                pos+=2
            else:
                result[nav]=num
                nav+=2
        return result

        
