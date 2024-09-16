'''N кеглей выставили в один ряд, занумеровав их слева направо числами от 1 до N. Затем по
этому ряду бросили K шаров, при этом i-й шар сбил все кегли с номерами от li до ri
включительно. Определите, какие кегли остались стоять на месте.'''
def task():
    n, k = list(map(int, input().split()))
    balls = ["I"]
    for i in range(k):
        l, r = list(map(int, input().split()))
        for j in range(l-1, r):
            balls[j] = '.'
            return (''.join(balls))
resolve = task()
print(resolve)