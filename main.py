from operator import index

nums = [2,7,11,15]
target = 9



def twoSum(nums, target):
    for i in nums:
        for j in nums:
            print(nums.index(i), nums.index(j))
            if nums.index(i) != nums.index(j):
                if i + j == target:
                    return print([nums.index(i), nums.index(j)])


twoSum(nums, target)
