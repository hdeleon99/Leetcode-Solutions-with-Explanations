from collections import defaultdict


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
