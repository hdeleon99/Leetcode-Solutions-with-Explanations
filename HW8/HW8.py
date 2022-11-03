from math import inf
from typing import List


def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    preMap = {i: [] for i in range(numCourses)}
    for course, prereq in prerequisites:
        preMap[course].append(prereq)
    visited = set()
    result = []
    cycle = set()
    '''
    course | prereq
    0      | [2]
    1      | [3]
    2      | [1, 4]
    3      | []
    4      | [3]
    visited = (3, 1, 4, 2, 0)
    '''

    def dfs(course):
        if course in cycle:
            return False
        if course in visited:
            return True

        cycle.add(course)

        for prereq in preMap[course]:
            if not dfs(prereq):
                return False

        cycle.remove(course)
        visited.add(course)
        result.append(course)

        return True

    for course in preMap.keys():
        if not dfs(course):
            return []
    return result
print("#1 input/output")
print(findOrder(numCourses=5, prerequisites=[[0,2], [2,1], [2,4], [1,3], [4,3]])) # should return [3, 1, 4, 2, 0]
print(findOrder(numCourses=2, prerequisites=[[0,1], [1,0]])) # should return []


def divide(dividend, divisor):
    if divisor == 0:
        return "can't divide by 0"
    positive = (dividend < 0) is (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)
    res = 0
    j = 0
    while dividend >= divisor:
        temp, i = divisor, 1

        while dividend >= temp:
            #print(j)
            j-=1
            dividend -= temp
            res += i
            i <<= 1
            temp <<= 1
    if not positive:
        res = -res
    return min(max(-2147483648, res), 2147483647)
print("#2 input/output")
print(divide(dividend=1000, divisor=2))
print(divide(dividend=10, divisor=0))
print(divide(dividend=-20, divisor=10))


def coinChange(coins: List[int], amount: int) -> int:
    cache = [float(inf)] * (amount + 1)
    # dynamic programming base case
    cache[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            diff = i - coin
            if diff >= 0:
                cache[i] = min(cache[i], 1 + cache[diff])
    return cache[amount] if cache[amount] != float(inf) else -1

'''
coins = [1,3,4,5]
cache[0] = 0
             i - coin
cache[1] --> 1 - 1 = 0 >= 0, so 1 + cache[0] = 1 + 0, cache[1] = 0
cache[1] --> 1 - 3 = -2 !>= 0, so we cannot access an element in cache at cache[-2]
'''
print("#3 input/output")
print(coinChange(coins=[1,3,4,5], amount=7)) # should return 2, 3 + 4 = 7
print(coinChange(coins=[2, 7], amount=5)) # should return -1