from collections import defaultdict

# inputs for question 1
q1input1 = [1,1,1,3,3,4]
q1k1 = 2  # q1input1 should return [1,3]

q1input2 = [1]
q1k2 = 1    # should return [1]

q1input3 = [4,4,4,5,5,2]
q1k3 = 3    # should return [4,5,2]


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
print(topKFrequentElements(q1input1, q1k1))     # should return [1,3]
print(topKFrequentElements(q1input2, q1k2))     # should return [1]
print(topKFrequentElements(q1input3, q1k3))     # should return [4,5,2]



