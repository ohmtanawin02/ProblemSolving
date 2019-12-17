import timeit

nums = [1,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]

def method1(value):
    found = False
    for i in range(len(nums)):
        print(i,nums[i])
        if nums[i] == value :
            found = True
            break
    return found, i
print(method1(37))