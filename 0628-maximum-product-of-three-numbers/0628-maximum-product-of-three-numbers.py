class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        fir=nums[-1]*nums[-2]*nums[-3]
        sec=nums[0]*nums[1]*nums[-1]
        return max(fir,sec)