# Given a list of numbers, nums
# And a target return the indices
# Of 2 values in nums such that
# they add up to the target value

def two_sum(nums, target):
    for i in nums:
        if (target-i) in nums:
            return [i, target-i]
        else:
            return "Can not find the two numbers"