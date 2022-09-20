from collections import defaultdict

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
