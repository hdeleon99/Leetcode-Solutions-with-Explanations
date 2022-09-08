from collections import defaultdict
from collections import deque
from math import inf


def majorityElement(nums):
    count, curr_max = 0, -1

    for j in range(len(nums)):
        if count == 0:
            curr_max = nums[j]
            count += 1
        elif curr_max == nums[j]:
            count += 1
        else:
            count -= 1
    return curr_max


print("Question 1 input -------------------------------------------")
q1_input1 = [1, 2, 2, 3, 5, 1, 2]
q1_input2 = [6, 6, 6, 6, 7, 7]
print("Input 1: " + str(q1_input1) + " should return 2.")
print("Input 2: " + str(q1_input2) + " should return 6.")
print(f"majorityElement(Input1) returned: {str(majorityElement(q1_input1))}")
print(f"majorityElement(Input2) returned: {str(majorityElement(q1_input2))}")


def kThLargestElement(nums, k):
    k = len(nums) - k

    def quickSort(left, right):
        pivot = nums[right]
        pointer = left

        for i in range(left, right):
            if nums[i] < pivot:
                nums[pointer], nums[i] = nums[i], nums[pointer]
                pointer += 1
        nums[pointer], nums[right] = pivot, nums[pointer]
        if pointer > k:
            return quickSort(left, pointer - 1)
        elif pointer < k:
            return quickSort(pointer + 1, right)
        else:
            return nums[pointer]

    return quickSort(0, len(nums) - 1)


print("Question 2 input -------------------------------------------")
q2_input1 = [1, 2, 2, 3, 5, 1, 2]
k1 = 2
k2 = 3
q2_input2 = [6, 6, 6, 6, 7, 7, 1, 5]
print("Input 1: " + str(q2_input1) + f", and k = {k1} should return 3.")
print(f"Input 2: " + str(q2_input2) + f", and k = {k2} should return 5.")
print(f"kThLargestElement(Input1, k1): returned: {str(kThLargestElement(q2_input1, k1))}")
print(f"kThLargestElement(Input2, k2): returned: {str(kThLargestElement(q2_input2, k2))}")


def maximumGap(nums):
    # Need to do this in linear time
    # We will find the range of our numbers
    # Put our numbers into n-1 buckets

    length = len(nums)
    if length < 2:
        return 0
    low, high = min(nums), max(nums)
    bucket = defaultdict(list)

    for num in nums:
        if num == high:
            index = length - 1
        else:
            index = (abs(low - num)) * (length - 1) // (high - low)

        bucket[index].append(num)

    bucket2 = []

    for i in range(length):
        if bucket[i]:
            bucket2.append((min(bucket[i]), max(bucket[i])))
    output = 0

    for i in range(1, len(bucket2)):
        output = max(output, abs(bucket2[i - 1][-1] - bucket2[i][0]))
    return output


print("Question 3 input -------------------------------------------")
q3_input1 = [3, 6, 9, 1]
q3_input2 = [9, 10, 1, 2, 5, 4, 3, 11, 35]
print(f"maximumGap(input1): {maximumGap(q3_input1)}")
print(f"maximumGap(input2): {maximumGap(q3_input2)}")


def removeDuplicateLetters(s):
    # Use a stack
    # We need to keep track of greatest index number for each character
    # Build a stack to check if we have seen letter before

    lookup = defaultdict()

    for i in range(len(s)):
        lookup[s[i]] = i

    stack = []

    for i in range(len(s)):
        if s[i] in stack:
            continue
        while stack and stack[-1] > s[i] and lookup[stack[-1]] > i:
            #             b       >  c       lookup[b] > 2
            stack.pop()

        stack.append(s[i])

    return "".join(stack)


print("Question 4 input -------------------------------------------")
q4_input1 = "abcdcb"  # should return "abcd"
q4_input2 = "cbacdcbc"  # should return "acdb"
print(f"removeDuplicateLetters(input1): {removeDuplicateLetters(q4_input1)}")
print(f"removeDuplicateLetters(input2): {removeDuplicateLetters(q4_input2)}")


# 5
def shortestSubarray(nums, k):
    # thinking of sorting the array first, so we can use a sliding window to determine when and where we can shrink or expand our window/subarray
    # Each element in the queue will be [cumulativeSum, index]
    length = len(nums)
    deq = deque()

    cum_sum = 0
    shortest = float(inf)

    for i in range(length):
        cum_sum += nums[i]
        # if sum has now gotten bigger than k, our goal sum
        if cum_sum >= k:
            shortest = min(shortest, i + 1)

        # reduce window size to find min window with sum >= k
        curr = [float(-inf), float(-inf)]

        while deq and ((cum_sum - deq[-1][0]) >= k):
            curr = deq[-1]
            deq.pop()
        if curr[0] != float(-inf):
            shortest = min(shortest, (i - curr[1]))
        while deq and (cum_sum <= deq[0][0]):
            deq.popleft()
        deq.appendleft([cum_sum, i])
    print(shortest == float(inf))
    return -1 if shortest == float(inf) else shortest


print("Question 5 input -------------------------------------------")
q5_input1 = [2, -1, 2]  # should return 3
q5k1 = 3
q5_input2 = [1, 2]  # should return -1
q5k2 = 4
q5_input3 = [10, 200, 43, -100, 90, 3, 5, 19, 21]   # should return 2
q5k3 = 243
print(f"shortestSubarray(input1, k1): {shortestSubarray(q5_input1, q5k1)}")
print(f"shortestSubarray(input2, k2): {shortestSubarray(q5_input2, q5k2)}")
print(f"shortestSubarray(input3, k3): {shortestSubarray(q5_input3, q5k3)}")
