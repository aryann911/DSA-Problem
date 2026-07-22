class Solution(object):
    def fourSum(self, nums, target):
        ans=[]
        n=len(nums)
        if n<4:
            return ans
        nums.sort()
        for i in range(n):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                
                k=j+1
                l=n-1
                while k<l:
                    total=nums[i]+nums[j]+nums[k]+nums[l]
                    if total<target:
                        k+=1
                    elif total>target:
                        l-=1
                    else:
                        
                        ans.append([nums[i],nums[j],nums[k],nums[l]])
                        while k<l and nums[k]==nums[k+1]:
                            k+=1
                        while l!=n-1 and k<l and nums[l]==nums[l+1]:
                            l-=1
                        k+=1
                        l-=1

        return ans                    