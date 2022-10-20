from collections import deque
from math import inf
#from typing import List
import typing

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def removeInvalidParentheses(s):
    """"""
    # count the number of '(' and ')' needs to be removed
    if not s:
        return ['']
    stack = []
    del_l = del_r = 0
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                del_r += 1
    del_l += len(stack)

    # apply dfs
    def dfs(i, curr, half, l, r):  # half: number of excess half parenthesis '(' in curr
        if l < 0 or r < 0 or half < 0:
            return
        if i == len(s):
            if l == r == half == 0:  # push valid result
                res.add(curr)
            return
        if s[i] == '(':
            dfs(i + 1, curr, half, l - 1, r)  # del l
            dfs(i + 1, curr + s[i], half + 1, l, r)  # keep l
        elif s[i] == ')':
            dfs(i + 1, curr, half, l, r - 1)  # del r
            dfs(i + 1, curr + s[i], half - 1, l, r)  # keep r
        else:
            dfs(i + 1, curr + s[i], half, l, r)  # add letters

    res = set()
    dfs(0, '', 0, del_l, del_r)
    return list(res)


print("#1 Input and Outputs ====================================================")
q1i1 = "((a)))"
q1i2 = "()()((()"
print(removeInvalidParentheses(q1i1))
print(removeInvalidParentheses(q1i2))


def getMinimumDifference(root: TreeNode):
    def inorderTraversal(root, array):
        if root:
            inorderTraversal(root.left, array)
            array.append(root.val)
            inorderTraversal(root.right, array)

    inorder_array = []
    inorderTraversal(root, inorder_array)

    minDiff = float(inf)
    for i in range(len(inorder_array) - 1):
        minDiff = min(minDiff, abs(inorder_array[i] - inorder_array[i - 1]),
                      abs(inorder_array[i] - inorder_array[i + 1]))
    return minDiff


print("#1 Input and Outputs ====================================================")
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(6)
root.right.left = TreeNode(4)
root.right.right = TreeNode(7)
print("getMinimumDifference(root) returned: ", getMinimumDifference(root)) # --> should return 1

root2 = TreeNode(100)
root2.left = TreeNode(30)
root2.left.left = TreeNode(20)
root2.left.right = TreeNode(40)
root2.right = TreeNode(150)
root2.right.left = TreeNode(120)
print("getMinimumDifference(root2) returned: ", getMinimumDifference(root2)) # --> should return 10


def shortestPathLength(graph):
    if len(graph[0]) == 0:
        return 0

    n = len(graph)

    q = deque()

    for i in range(n):
        q.append((i, frozenset([i])))
    seen = set(q)

    steps = 0

    while q:
        temp = deque()
        while q:
            cur, mask = q.popleft()
            mask = list(mask)
            for node in graph[cur]:
                mask.append(node)
                nextMask = frozenset(mask)
                if len(nextMask) == n:
                    return steps + 1
                if (node, nextMask) not in seen:
                    temp.append((node, nextMask))
                    seen.add((node, nextMask))
                mask.pop()
        steps += 1
        q = temp
    return steps


print("#3 Input ----------------------------------------")
graph = [[1,2,3],[0],[0],[0]]
print("shortestPathLength:", shortestPathLength(graph))

def maxPathSum(root):
    res = [root.val]

    def dfs(root):
        if not root:
            return 0
        leftMax = dfs(root.left)
        rightMax = dfs(root.right)

        leftMax = max(leftMax, 0)
        rightMax = max(rightMax, 0)

        res[0] = max(res[0], root.val + leftMax + rightMax)

        # cant choose both or else this means we're splitting.
        # when we split we don't have a valid path

        return root.val + max(leftMax, rightMax)

    dfs(root)
    return res[0]


print("#4 Input ----------------------------------------")
num3_root = TreeNode(1)
num3_root.left = TreeNode(2)
num3_root.right = TreeNode(3)
num3Root1 = [1,2,3] # should return 6
print("MaxPathSum(): ", maxPathSum(num3_root))


def LexigraphicalOrder(n: int) -> List[int]:
    result = []
    def dfs(temp, n, result_list):
        if temp > n:
            return
        result_list.append(temp)
        dfs(temp * 10, n, result_list)
        if temp % 10 != 9:
            dfs(temp + 1, n, result_list)

    dfs(1, n, result)
    return result

print("#5 Input and Output ==========================================")
n1 = 11
n2 = 9
n3 = 20
print(LexigraphicalOrder(n1))
print(LexigraphicalOrder(n2))
print(LexigraphicalOrder(n3))
