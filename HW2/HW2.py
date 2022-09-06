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