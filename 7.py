'''Дан текст: в первой строке записано число строк, далее идут сами строки. Определите,
сколько различных слов содержится в этом тексте.'''
def task():
    n = int(input())
    count_words = set()
    for i in range(n):
        for word in input().split(' '):
            count_words.add(word)
    if '' in count_words:
        count_words.remove('')
    return len(count_words)
result = task()
print(result)