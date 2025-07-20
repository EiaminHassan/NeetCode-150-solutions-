nums = [3,4,5,6]
target = 7

def two_sum(numbers, target):
    num_dict = {}
    for i in range(len(numbers)):
        # calculate the complement of the current number
        complement = target - numbers[i]
        if complement in num_dict:
            return [num_dict[complement], i] # return indices of the two numbers
        num_dict[numbers[i]] = i             # store index of the number

result = two_sum(nums, target)
print(result)