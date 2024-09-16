'''Переставьте соседние элементы списка ( A[0] c A[1] , A[2] c A[3] и т. д.). Если элементов
нечетное число, то последний элемент остается на своем месте'''
def task():
    nums = list(map(int, input().split()))
    tmp = 0
    if len(nums)%2!=0:
        tmp = nums.pop(len(nums)-1)
    for i in range(0, len(nums), 2):
        if i == len(nums)-1:
            break
        nums[i], nums[i+1] = nums[i+1], nums[i]
    if tmp:
        nums.append(tmp)
    return (nums)
resolve = task()
print(resolve)