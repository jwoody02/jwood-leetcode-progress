class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Time Complexity: O(log(m+n))
        combined_list = sorted(nums1 + nums2)

        # median index for the combined list
        median_index = len(combined_list) // 2

        # check if even
        if len(combined_list) % 2 == 0:
            el1 = combined_list[median_index]
            el2 = combined_list[median_index - 1]
            return (el1 + el2) / 2
        else:
            return combined_list[median_index]
            
        