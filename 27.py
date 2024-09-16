''' Проходит только тестовый
Дан список. Выведите те его элементы, которые встречаются в списке только
 один раз.
Элементы нужно выводить в том порядке, в котором они встречаются в списке.
'''
def task():
    nums = list(map(int, input().split()))
    result = list()
    for i in range(len(nums)):
        if (nums[i] not in nums[:i]) and (nums[i] not in nums[i+1:]):
            return result.append(nums[i])
        
result = task()
print(result)