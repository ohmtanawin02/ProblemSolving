def selection_sort(nums):
    for i, n in enumerate(nums):
        mn = min(range(i,len(nums)), key=nums.__getitem__)
        nums[i], nums[mn] = nums[mn], n
    return nums

nums = [14,46,43,27,57,41,45,21,70]
print(selection_sort(nums))