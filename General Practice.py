import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mergeTreesRecursive(root1, root2):
    if not root1:
        return root2
    if not root2:
        return root1

    root1.val += root2.val

    root1.left = mergeTreesRecursive(root1.left, root2.left)
    root1.right = mergeTreesRecursive(root1.right, root2.right)

    return root1
'''
root2       root1
    4           4
   / \         / \
  2   5       6   8
 / \         / \
1   3       1   2

'''

root2 = TreeNode(4)
root2.left = TreeNode(2)
root2.left.left = TreeNode(1)
root2.left.right = TreeNode(3)
root2.right = TreeNode(5)

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
k = 1
mergeTreesRecursive(root1, root2)


def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    def dfs(root):
        nonlocal diameter
        if not root:
            return 0

        left = dfs(root.left)
        right = dfs(root.right)

        diameter = max(diameter, left + right)

        return max(left, right) + 1

    diameter = 0

    dfs(root)

    return diameter

diameterOfBinaryTree(root2)



def kthSmallest(root: TreeNode, k: int) -> int:
    stack = []
    curr = root
    n = 0

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        print(curr.val)
        curr = curr.right


kthSmallest(root2, k=1)


def mergeTreesIterative(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    if root1 is None:
        return root2

    queue = [(root1, root2)]

    while len(queue):
        node1, node2 = queue.pop()
        if node1 is None or node2 is None:
            continue

        node1.val += node2.val

        if node1.left is None:
            node1.left = node2.left
            node2.left = None

        if node1.right is None:
            node1.right = node2.right
            node2.right = None

        queue.append((node1.left, node2.left))
        queue.append((node1.right, node2.right))

    return root1

def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
    # using BFS
    queue = collections.deque([root])
    ans = 0

    while queue:

        for i in range(len(queue)):

            node = queue.popleft()
            ans += node.val
            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        print(ans)


def partition(array, begin, end):
    pivot = begin

    for i in range(begin + 1, end + 1):

        if array[i] <= array[begin]:
            pivot += 1

            array[i], array[pivot] = array[pivot], array[i]

    array[pivot], array[begin] = array[begin], array[pivot]

    return pivot


def quicksort(array, begin, end):
    if begin >= end:
        return

    pivot = partition(array, begin, end)

    quicksort(array, begin, pivot - 1)

    quicksort(array, pivot + 1, end)


# added calling code


mylist = [8, 2, 17, 4, 12]

quicksort(mylist, 0, 4)