class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        m=len(nums1)
        n=len(nums2)
        i,j=0,0
        result=[]
        while i<m and j<n:
            if nums1[i]<nums2[j]:
                result.append(nums1[i])
                i+=1
            else:
                result.append(nums2[j])
                j+=1
        if i<m:
            while i<m:
                result.append(nums1[i])
                i+=1
        if j<n:
            while j<n:
                result.append(nums2[j])
                j+=1
        
        s=len(result)
        mid=s//2
        if s%2==0:
            add=(result[mid-1]+result[mid])/2.0
            return add
        else:
            return float(result[mid])