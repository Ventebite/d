'''Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается,
что любые два элемента, равные друг другу образуют одну пару, которую необходимо
посчитать.'''
def task():
    nums = list(map(int, input().split()))
    count = 0
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                count+=1
    return count
result = task()
print(result)