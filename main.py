import pygame
import random
from random import randrange

pygame.init()
w = 1050
h = 750
sc = 20
pygame.display.set_caption("Snakey 90s, Happy New Year Edition")
a = 50

clock = pygame.time.Clock()

fontgameover = pygame.font.SysFont("Pixeboy", 160)
fontscore = pygame.font.SysFont("Pixeboy", 50)
fontsc = pygame.font.SysFont("Pixeboy", 50)
fontagain = pygame.font.SysFont("Pixeboy", 90)


def snakeyy(arrsnakey, x, y):
    """
    Задать змейку, ее размеры, цвет

    arrsnakey -- массив змейки, состоящий из чисел
    x, y -- координаты змейки
    """
    for i in arrsnakey:
        [(pygame.draw.rect(win, pygame.Color(156, 154, 217), [i, j, a, a]))
         for i, j in arrsnakey]


def scoresee(score):
    """
    Выводит количество очков, зарабатонных в игре.
    """
    scoresee = fontscore.render(f'SCORE: {score}', 2, pygame.Color('brown'))
    win.blit(scoresee, [0, 0])


def gameoverseee(score, sc):
    """
    При прогрыше выводит GAME OVER и рекордное количество очков

    score -- текущее набранное значение во время игры
    sc -- рекордное значение
    """
    gameoversee = fontgameover.render("GAME OVER", 1, pygame.Color('red'))
    win.blit(gameoversee, [w/6, h/3])
    sc = record(score, sc)
    scsee = fontsc.render(f'RECORD SCORE: {sc}', 1, pygame.Color(110, 47, 49))
    win.blit(scsee, [w/6, h/3+200])
    againsee = fontagain.render(
        "PRESS SPACE TO START AGAIN", 1, pygame.Color('red'))
    win.blit(againsee, [w/6-138, h/3+400])


def cookiee():
    """
    Выводит на экран печеньку, с помощью которой змейка будет расти
    """
    cookiex = randrange(0, 1040, a)
    cookiey = randrange(0, 740, a)
    win.blit(cookie, (cookiex, cookiey))
    pygame.display.flip()


def treee():
    """
    Выводит на экран дерево, столкнувшись с которым игра заканчивается
    """
    treex = randrange(0, 1040, a)
    treey = randrange(0, 750, a)
    win.blit(tree, (treex, treey))


def record(score, sc):
    """
    Набранные очки сравнивает с рекордом,
    и если они больше - набранные становятся рекордом,
    если нет - рекорд остановится прежним

    score -- набранные очки
    sc -- рекордные очки

    return измененные sc, если score оказалась больше
    если score меньше, sc остается прежним
    """
    maxscore = score
    recordscore = sc

    if maxscore > recordscore:
        sc = maxscore
    maxscore = 0
    return(sc)


def collide_with_tree(treex, treey, x, y, score, gameover):
    """
    Проверяет на столкновение с деревом,
    если столкнулась - игра окончена

    treex, treey -- координаты дерева
    x, y -- координаты змейки
    score -- заработанные на данный момент очки
    gameover -- является параметром, идентифицирующим False
    """
    if x == treex and y == treey:
        game_over(score, gameover)
        pygame.display.update()
        exit_from_game(gameover)


def eating_cookie(cookiex, cookiey, x, y, leng, head, arrsnakey, score, v):
    """
    Проверяет на поедание печеньки, 
    после поедания увеличивает змейку, увеличивает очки, скорость

    leng -- длина змейки
    head -- голова змейки
    score -- очки
    v -- скорость
    x, y -- координаты змейки
    cookiex, cookiey -- координаты печеньки
    arrsnakey -- массив змейки, состоящий из чисел
    """
    if x == cookiex and y == cookiey:
        cookiee()
        leng += 1
        head = [x, y]
        arrsnakey.append(head)
        score += 1
        v += 1
        treee()
        pygame.display.update()
        pygame.display.flip()


def game_over(score, gameover):
    """
    Проверяет на то, было ли окончание игры,
    если да - вызывается заливка экрана и надписи GAME OVER, score,
    recordscore, 
    показывается экран с нужными надписями

    score -- набранные очки
    gameover -- является параметром, идентифицирующим False
    """
    win.blit(background, (0, 0))
    gameoverseee(score, sc)
    scoresee(score)
    pygame.display.update()
    exit_from_game(gameover)


def exit_from_game(gameover):
    """
    Проверяет нажатие кнопок: крестик наверху окна
    и пробел на клавиатуре.

    Нажатие крестика -- выход из игры
    Нажатие пробела -- перезапуск игры

    gameover -- является параметром, идентифицирующим False
    """
    for event in pygame.event.get():
        key = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            gameover = True
            exit()
        if key[pygame.K_SPACE]:
            gameplay()


def buttons_click(dx, dy, key):
    """Проверяет, какая клавиша была нажата.
    При нажатии опредленных клавиш меняются скорость, а также ращрешение, какую кнопку нажать

    dx, dy -- изменение координат змейки
    key -- параметр запускающий метод pygame для читания нажатых клавиш

    return: измененные в соотвествии с нажатой клавишей dx, dy
    """
    buttons = {'W': True, 'S': True, 'A': True, 'D': True}
    if (key[pygame.K_UP] or key[pygame.K_w]) and buttons['W']:
        dx, dy = 0, -a
        buttons = {'W': True, 'S': False, 'A': True, 'D': True}
    if (key[pygame.K_DOWN] or key[pygame.K_s]) and buttons['S']:
        dx, dy = 0, a
        buttons = {'W': False, 'S': True, 'A': True, 'D': True}
    if (key[pygame.K_LEFT] or key[pygame.K_a]) and buttons['A']:
        dx, dy = -a, 0
        buttons = {'W': True, 'S': True, 'A': True, 'D': False}
    if (key[pygame.K_RIGHT] or key[pygame.K_d]) and buttons['D']:
        dx, dy = a, 0
        buttons = {'W': True, 'S': True, 'A': False, 'D': True}
    return(dx, dy)


def colliding_with_walls(x, y, w, h):
    """Удар со стенами.
    Если змейка ударяется о стену, она не может дальше идти, игра заканчивается

    x, y -- координаты змейки
    w -- ширина экрана (плоскости, где двигается змейка)
    h -- высота экрана 

    return: возвращает True, если змейка встретилась со стеной
    возврващает False, если змейка не ударяется о стену 
    """
    if x >= w or x < 0 or y >= h or y < 0:
        return True
    return False


def gameplay():
    """
    Сама игра, ее суть
    """
    x = randrange(0, 1040, a)
    y = randrange(0, 740, a)
    dx = 0
    dy = 0
    arrsnakey = []
    leng = 1
    v = 15

    cookiex = randrange(0, 1040, a)
    cookiey = randrange(0, 740, a)

    treex = randrange(0, 1040, a)
    treey = randrange(0, 740, a)

    score = 0

    gameover = False
    closing = False

    while not gameover:
        key = pygame.key.get_pressed()

        dx, dy = buttons_click(dx, dy, key)

        win.blit(background, (0, 0))
        while closing == True:
            game_over(score, gameover)
        for event in pygame.event.get():
            key = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                gameover = True
                exit()
            if key[pygame.K_SPACE]:
                gameplay()

            if key[pygame.K_SPACE]:
                gameplay()

            if x == cookiex and y == cookiey:
                eating_cookie(cookiex, cookiey, x, y,
                              leng, head, arrsnakey, score, v)

                win.blit(background, (0, 0))

                cookiex = randrange(0, 1040, a)
                cookiey = randrange(0, 740, a)

                win.blit(cookie, (cookiex, cookiey))

                treex = randrange(0, 1040, a)
                treey = randrange(0, 740, a)
                win.blit(tree, (treex, treey))

                score += 1
                v += 1
                pygame.display.update

            if x == treex and y == treey:
                closing = True
                collide_with_tree(treex, treey, x, y, score, gameover)
                game_over(score, gameover)

            if x >= w or x < 0 or y >= h or y < 0:
                closing = colliding_with_walls(x, y, w, h)

            x += dx
            y += dy

            win.blit(background, (0, 0))
            #pygame.draw.rect(win, cookie,[cookiex, cookiey, a, a])
            win.blit(cookie, (cookiex, cookiey))

            win.blit(tree, (treex, treey))

            pygame.display.update

            head = [x, y]
            arrsnakey.append(head)
            #score += 1
            v += 1

            if len(arrsnakey) > leng:
                del arrsnakey[0]

            for f in arrsnakey[:-1]:
                if f == head:
                    closing = True

            snakeyy(arrsnakey, x, y)
            scoresee(score)

            pygame.display.flip()
            clock.tick(v)


if __name__ == "__main__":
    win = pygame.display.set_mode((w, h), 1)
    background = pygame.image.load("snow.png").convert()
    snakey = (252, 186, 3)
    cookie = pygame.image.load("cookie.png").convert_alpha()
    tree = pygame.image.load("tree.png").convert_alpha()
    win.blit(background, (0, 0))

    gameplay()
    pygame.QUIT()
