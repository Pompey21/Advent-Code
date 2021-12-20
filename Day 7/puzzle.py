"""
Hello, hello! This is the puzzle of Day 7!
Day 7: https://adventofcode.com/2021/day/7
"""

""" NOTE: I tried using both, mode and mean but nothing worked.. Hence, 
	I will need to use the median. And for that I need to find an efficient
	sorting algorithm! I was pointed to QuickSelect, here is a link to the
	video & explanation :) 
	video: https://www.youtube.com/watch?v=v-1EGgaTFuw 
"""
import statistics

with open('input.txt') as f:
	lines = [int(elem) for elem in f.readlines()[0].split(',')]

# print(lines)
dict_nums = {}
for elem in lines:
	if elem not in dict_nums.keys():
		dict_nums[elem] = 1
	else:
		dict_nums[elem] = dict_nums.get(elem)+1

mode = max(dict_nums, key=dict_nums.get)
print(mode)

mean = round(sum(lines)/len(lines))
print(mean)

median = int(statistics.median(lines))
print(median)

# Task 1:
result = sum([abs(elem-median) for elem in lines])
print(result)

def spending(difference):
	n = difference
	result = (n*(n+1))/2
	return result

# Task 2:
result2 = int(sum([spending(abs(elem-mean)) for elem in lines]))
print(result2)


