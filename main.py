from operator import index

nums = [3, 2, 4]
target = 6



def twoSum(nums, target):
    for i in nums:
        for j in nums:
            print(i, j)
            if nums.index(j) == nums.index(i):
                continue
            elif i + j == target:
                return print([nums.index(i), nums.index(j)])


twoSum(nums, target)
