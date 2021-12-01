with open('input.txt') as f:
    lines = f.readlines()

nums = [int(num[:-1]) for num in lines]

counter = 0
for count,num in enumerate(nums,1):
    if count < len(nums):
        print(num)
        print(nums[count])
        print('--------')
        # break
        if num < nums[count]:
            counter += 1

print(counter)
