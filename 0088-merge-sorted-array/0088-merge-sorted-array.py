class Solution(object):
    def merge(self, nums1, m, nums2, n):
        arr1 = nums1[:m]
        k = 0
        i = 0
        j = 0
        while(i<m and j<n and k<(n+m)):
            if(arr1[i] <= nums2[j]):
                nums1[k] = arr1[i]
                k+=1
                i+=1
            else:
                nums1[k] = nums2[j]
                k+=1
                j+=1    
        while(i<m):
            nums1[k] = arr1[i]
            k+=1
            i+=1
        while(j<n):
            nums1[k] = nums2[j]
            k+=1
            j+=1    
        return nums1
        