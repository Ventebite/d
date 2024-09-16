'''Август и Беатриса играют в игру. Август загадал натуральное число от 1 до n . Беатриса
пытается угадать это число, для этого она называет некоторые множества натуральных
чисел. Август отвечает Беатрисе YES , если среди названных ей чисел есть задуманное или
NO в противном случае. После нескольких заданных вопросов Беатриса запуталась в том,
какие вопросы она задавала и какие ответы получила и просит вас помочь ей определить,
какие числа мог задумать Август.
Август начал жульничать. На каждый из вопросов Беатрисы он выбирает такой вариант
ответа YES или NO , чтобы множество возможных задуманных чисел оставалось как можно
больше. Например, если Август задумал число от 1 до 5, а Беатриса спросила про числа 1 и
2, то Август ответит NO , а если Беатриса спросит про 1, 2, 3, то Август ответит YES .
Если же Беатриса в своем вопросе перечисляет ровно половину из задуманных чисел, то
Август из вредности всегда отвечает NO . Наконец, Август при ответе учитывает все
предыдущие вопросы Беатрисы и свои ответы на них, то есть множество возможных
задуманных чисел уменьшается'''
def task():
    def possible_numbers(n, queries):
        possible_set = set(range(1, n + 1))
        answers = []
        for query in queries:
            query_set = set(query)
            if len(query_set & possible_set) > len(possible_set) / 2:
                answers.append("YES")
                possible_set &= query_set
            else:
                answers.append("NO")
                possible_set -= query_set
        return sorted(possible_set), answers
    n = int(input().strip())
    queries = []
    while True:
        line = input().strip()
        if line == "HELP":
            break
        numbers = list(map(int, line.split()))
        queries.append(numbers)
    result, answers = possible_numbers(n, queries)
    for answer in answers:
        print(answer)
    for answer in answers:
        print(answer)
    print(" ".join(map(str, result)))