def removeDuplicates(nums):
    left = 1
    for right in range(1, len(nums)):
        if nums[right] != nums[right-1]:
            nums[left] = nums[right]
            left += 1
    return left


# [1,2,3,3] =>  [1,2,3] => return 3
#  [0,0,1,1,1,1,2,2,3,3,4] => [0,1,2,3,4] => return 5
print(removeDuplicates([1, 2, 3, 3]))  # 3

print(removeDuplicates([0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 4]))  # 5

# Time complexity 0(n)
