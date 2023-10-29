class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # return index
        index = -1

        # helper func to check if target could be in subarray
        def couldTargetBeInArray(array, targ):
            return len(array) > 0 and min(array) <= targ and max(array) >= targ
        
        # modified binary search, relativeIndex is the start index of current subarray
        def rotatedBinarySearch(subArray: List[int], goal: int, relativeIndex: int):
            nonlocal index
            if len(subArray) == 1 and subArray[0] == goal:
                print("found goal!")
                index = relativeIndex

            if index != -1:
                return

            leftSide = subArray[0:(len(subArray) // 2)]
            rightSide = subArray[(len(subArray) // 2):len(subArray)]
            print("left side:", leftSide)
            print("right side:", rightSide)
            if couldTargetBeInArray(leftSide, goal):
                rotatedBinarySearch(leftSide, goal, relativeIndex)
            if couldTargetBeInArray(rightSide, goal):
                rotatedBinarySearch(rightSide, goal, relativeIndex + (len(subArray) // 2))

        rotatedBinarySearch(nums, target, 0)
        return index