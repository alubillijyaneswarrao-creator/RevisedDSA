# 4. Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged = sorted(nums1 + nums2)
        n = len(merged)
        
        if n % 2 == 1:  # odd length
            return float(merged[n // 2])
        else:  # even length
            return (merged[n // 2 - 1] + merged[n // 2]) / 2.0
