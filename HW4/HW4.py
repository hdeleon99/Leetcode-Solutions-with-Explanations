from collections import defaultdict, deque
from math import inf
from typing import List

# inputs for question 1
q1input1 = [1, 1, 1, 3, 3, 4]
q1k1 = 2  # q1input1 should return [1,3]

q1input2 = [1]
q1k2 = 1  # should return [1]

q1input3 = [4, 4, 4, 5, 5, 2]
q1k3 = 3  # should return [4,5,2]


def topKFrequentElements(nums, k):
    count_dict = defaultdict(int)

    freq = [[] for i in range(len(nums) + 1)]

    for num in nums:
        count_dict[num] += 1

    for num, count in count_dict.items():
        freq[count].append(num)

    result = []

    for i in range(len(freq) - 1, -1, -1):
        for num in freq[i]:
            result.append(num)
            if len(result) == k:
                return result


print("Question 1 output ================================")
print(topKFrequentElements(q1input1, q1k1))  # should return [1,3]
print(topKFrequentElements(q1input2, q1k2))  # should return [1]
print(topKFrequentElements(q1input3, q1k3))  # should return [4,5,2]

# inputs for question 2
arr1 = [1, 2, 3, 4, 5]  # should return [1,2,3,4]
k1 = 4
x1 = 3

arr2 = [1, 2, 3, 4, 5, 9, 20]  # should return [5,9,20]
k2 = 3
x2 = 14


def findClosestElements(arr, k, x):
    l, r = 0, len(arr) - 1

    val, idx = arr[0], 0

    while l <= r:
        mid = (l + r) // 2

        currDiff = abs(arr[mid] - x)
        resDiff = abs(val - x)

        if currDiff < resDiff or (currDiff == resDiff and arr[mid] < val):
            val = arr[mid]
            idx = mid

        if arr[mid] < x:
            l = mid + 1
        elif arr[mid] > x:
            r = mid - 1
        else:
            break
    l = r = idx

    for i in range(k - 1):
        if l == 0:
            r += 1
        elif r == len(arr) - 1 or (abs(x - arr[l - 1]) <= abs(x - arr[r + 1])):
            l -= 1
        else:
            r += 1
    return arr[l: r + 1]


print("Question 2 output ================================")
print(findClosestElements(arr1, k1, x1))
print(findClosestElements(arr2, k2, x2))

# inputs for question 3
q3input1 = [15, 13, 12, 10, 8, 9]
q3k1 = 5  # should return 15, 13, 12, 10, 9

q3input2 = []
q3k2 = 1

def peekTop(arr: List[int], k: int):
    if len(arr) == 0:
        return []
    arr.sort(reverse=True)
    res = []
    for i in range(k):
        res.append(arr[i])
    return res


print("Question 3 output ================================")
print(peekTop(q3input1, q3k1))
print(peekTop(q3input2, q3k2))

# input for question 4
q4input1 = [1]
q4k1 = 1

q4input2 = [1, 2]
q4k2 = 4

q4input3 = [2,-1,2]
q4k3 = 3

def shortestSubarray(nums: List[int], k:int) -> int:
    length = len(nums)
    deq = deque()
    # [6, -3, 0] goal is 3
    cumSum = 0
    shortest = float(inf)

    for i in range(length):
        cumSum += nums[i]

        if cumSum >= k:
            shortest = min(shortest, i + 1)

        curr = [float(-inf), float(-inf)]

        while deq and ((cumSum - deq[-1][0]) >= k):
            curr = deq[-1]
            deq.pop()
        if curr[0] != float(-inf):
            shortest = min(shortest, (i - curr[1]))
        while deq and (cumSum <= deq[0][0]):
            deq.popleft()
        deq.appendleft([cumSum, i])
    return -1 if shortest == float(inf) else shortest

print("Question 4 output ================================")
print(shortestSubarray(q4input1, q4k1))
print(shortestSubarray(q4input2, q4k2))
print(shortestSubarray(q4input3, q4k3))

print("Question 5 output =========================================")
def kthSmallestPrimeFraction(arr: List[int], k: int) -> List[int]:
    dictionary = defaultdict(list)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            dictionary[arr[i] / arr[j]] = [arr[i], arr[j]]
    sorted_results = sorted(dictionary.keys())
    # return dictionary.get(sorted_results[k-1])
    return dictionary[sorted_results[k - 1]]

q5input1 = [1,3,4,6]
q5k1 = 1 # should return [1,6]

q5input2 = [1,6,10,20]
q5k2 = 2 # should return [1,10]

q5input3 = [i for i in range(10000)]
q5k3 = 540 # should return
print(kthSmallestPrimeFraction(q5input1, q5k1))
print(kthSmallestPrimeFraction(q5input2, q5k2))
print(kthSmallestPrimeFraction(q5input3, q5k3))