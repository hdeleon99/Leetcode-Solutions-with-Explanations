# Python script for CS497-4 Homework 1
from typing import List, Tuple, Any


# Question 1
def twoSum(nums, target):
    for left in range(len(nums)):
        for right in range(left + 1, len(nums)):
            if nums[left] + nums[right] == target:
                print([left, right])
                return [left, right]


# Question 2
def searchRange(nums: List[int], target: int) -> tuple[int, int]:
    # Must be O(log n) complexity
    # If we used a for loop, that would be O(n) complexity, going through every element in the list
    # We know that the list is sorted in increasing order, this can help us
    # Will use Binary Search Algorithm

    left = binSearch(nums, target, True)
    right = binSearch(nums, target, False)
    print([left, right])
    return left, right


def binSearch(nums, target, search_left: bool):
    left, right = 0, len(nums) - 1
    answer = -1
    while left <= right:
        midpoint = (left + right) // 2

        if nums[midpoint] == target:
            answer = midpoint
            if search_left:
                right = midpoint - 1
            else:
                left = midpoint + 1
        elif nums[midpoint] < target:
            left = midpoint + 1

        else:
            right = midpoint - 1

    return answer


# Question 1 Input ===========================================================
example1 = [1, 2, 3, 4, 5, 6]
target1 = 8  # should return [1, 5]

example2 = [3, 2, 4]
target2 = 6  # should return [1, 2]

example3 = [3, 3]
target3 = 6  # should return [0, 1]

print("Question 1 Output =====================================================")
twoSum(example1, target1)
twoSum(example2, target2)
twoSum(example3, target3)

# Question 2 Input ===========================================================
nums1 = [5, 7, 7, 8, 8, 10]
target1 = 6  # Output: [-1,-1]

nums2 = [5, 7, 7, 8, 8, 10]
target2 = 8  # Output: [3,4]

nums3 = [1]
target3 = 1  # Output: [0,0]

print("Question 2 Output =====================================================")
searchRange(nums1, target1)
searchRange(nums2, target2)
searchRange(nums3, target3)


# Question 3
