from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def maxDepth(self, root: TreeNode):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# test cases for #1
root1 = TreeNode(3)
node1 = TreeNode(5)
node2 = TreeNode(10)
node3 = TreeNode(7)
node4 = TreeNode(9)
node2.right = node3
node3.right = node4

#           3
#         /   \
#        5     10
#                \
#                 7
#                  \
#                   9
# depth should be 4

root1.left = node1
root1.right = node2

root2 = TreeNode(1)
root2.right = TreeNode(2)
root2.right.right = TreeNode(3)

example1 = Solution1()
print(example1.maxDepth(root1))  # 4
print(example1.maxDepth(root2))  # 3


# The time complexity of this solution in the worst case is O(n), where every node must be visited
# up until a node with no children is reached. We know that with recursion each function call
# is stored on the program stack, so the space complexity will be O(tree depth)
# or O(k) where k is the depth of the tree

class Solution2:
    @staticmethod
    def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
        # will use a set
        set_of_nums = set()
        result = set()

        for num in nums1:
            set_of_nums.add(num)
        for num in nums2:
            if num in set_of_nums:
                result.add(num)
        return list(result)


# inputs for #2
num2input1 = [1, 1, 2, 3, 4, 5]
num2input2 = [1, 4, 9]
# result should be [1,4]

num2input3 = [10, 20, 30]
num2input4 = [30, 100, 400]  # should return [30]

num2input5 = [1, 2, 3]
num2input6 = [4, 5, 6]  # should return nothing

example2 = Solution2()
print(Solution2.intersection(num2input1, num2input2))
print(Solution2.intersection(num2input3, num2input4))
print(Solution2.intersection(num2input5, num2input6))

# The solution to this problem takes advantage of the fact that a set will never have repeating elements. So we can
# define and initialize two empty sets, setOfNums and result Into setOfNums we add all the contents of one list into
# that set. It does not matter which list's contents are added to the set, because an intersection looks for numbers
# that are in BOTH sets So we add nums1 contents to the set. Then we iterate through nums2, and check if each number
# is in the setOfNums. If it is in setOfNums, add it to the result. Since our result is a set as well, we will never
# add duplicates to that data structure. Therefore, the time complexity of adding elements of one list into a set,
# and then iterating through the contents of the second set is O(n + m), where n is the length of the first list and
# m is the length of the second list. Space complexity: Since we use two sets, we won't quite hold every single value
# from one list into a set, however in the worst case the contents of either array provided will be entirely unique.
# So the space complexity in the worst case is O(n+m) where n is the length of list 1 with all unique elements,
# and m is the length of list 2 with all unique elements.
