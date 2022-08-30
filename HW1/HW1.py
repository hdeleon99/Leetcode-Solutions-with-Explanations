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


# Question 3
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    A, B = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2

    if len(B) < len(A):
        A, B = B, A

    left, right = 0, len(A) - 1

    while True:
        i = (left + right) // 2  # A
        j = half - i - 2  # B

        Aleft = A[i] if i >= 0 else float("-infinity")
        Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
        Bleft = B[j] if j >= 0 else float("-infinity")
        Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

        if Aleft <= Bright and Bleft <= Aright:
            # odd
            if total % 2:
                print(min(Aright, Bright))
                return min(Aright, Bright)
            print((max(Aleft, Bleft) + min(Aright, Bright)) / 2)
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

        elif Aleft > Bright:
            right = i - 1
        else:
            left = i + 1


# Question 4
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printLinkedList(head):
    node = head
    while node is not None:
        print(node.val)
        node = node.next


def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    left = dummy
    right = head

    while n > 0 and right is not None:
        right = right.next
        n -= 1
    while right is not None:
        left = left.next
        right = right.next

    left.next = left.next.next
    printLinkedList(dummy.next)
    return dummy.next


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

# Question 3 Input ===========================================================
nums1 = [1, 3]
nums2 = [2]
# Should return 2

nums3 = [1, 2]
nums4 = [3, 4]

print("Question 3 Output =====================================================")
findMedianSortedArrays(nums1, nums2)
findMedianSortedArrays(nums3, nums4)
# Should return 2.5

# Question 4 Input ===========================================================
linkedlist1 = ListNode(1)
linkedlist1.next = ListNode(5)
n1 = 2

linkedlist2 = ListNode(1)
linkedlist2.next = ListNode(2)
linkedlist2.next.next = ListNode(3)
n2 = 2

print("Question 4 Output =====================================================")
removeNthFromEnd(linkedlist1, n1)  # Should return 5
print("=======")
removeNthFromEnd(linkedlist2, n2)  # Should return [1, 3]
