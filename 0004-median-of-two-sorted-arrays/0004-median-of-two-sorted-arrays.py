class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined_list = sorted(nums1 + nums2)
        if len(combined_list) % 2 == 0:
            # even amount, need to add two middle elements
            el1 = combined_list[(len(combined_list) // 2) - 1]
            el2 = combined_list[len(combined_list) // 2]
            return (el1 + el2) / 2
        else:
            return combined_list[len(combined_list) // 2]

            
        