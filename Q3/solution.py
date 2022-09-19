from cgitb import reset


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
            for i in nums2:
                nums1.append(i)
            nums1.sort()
            return (len(nums1)+1)/2

solution=Solution() 
rese=solution.findMedianSortedArrays(nums1=[1,2],nums2=[3])
print(rese)