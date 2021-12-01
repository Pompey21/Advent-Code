"""
Hello, hello! This is the second puzzle of Day 1!
Day 1: https://adventofcode.com/2021/day/1
"""

with open('input.txt') as f:
    lines = f.readlines()

nums = [int(num[:-1]) for num in lines]

# sliding window variables
first = 0
second = 1
third = 2
fourth = 3

counter = 0
for count,num in enumerate(nums,0):
    first = count
    second = count + 1
    third = count + 2
    fourth = count + 3
    if count+3 < len(nums):
        a = nums[first]+nums[second]+nums[third]
        b = nums[second]+nums[third]+nums[fourth]
        print(a)
        if a < b:
            counter += 1

print(counter)