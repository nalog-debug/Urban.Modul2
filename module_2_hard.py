kamen_1 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
           17, 18, 19, 20]
import random
def who_():
    kamen_1 = list(range(3, 21))
    win = random.choice(kamen_1)
    return win
win = who_()
def get_password(win):
    password = ''
    for i in range(1, win):
        for j in range(2, win):
            if j <= i:
                continue
            if win % (i + j) == 0:
                password += str(i) + str(j)
    return password


kamen_2 = get_password(win)
print(f'Камень 1: {win}')
print(f'Камень 2 (пароль): {kamen_2}')
