import pygame
import random
from random import randrange

pygame.init()
w = 1050
h = 750
win = pygame.display.set_mode((w, h))
pygame.display.set_caption("Snakey 90s, Happy New Year Edition")

background = pygame.image.load("snow.png").convert()
snakey = (252, 186, 3)
cookie = pygame.image.load("cookie.png").convert()
tree = pygame.image.load("tree.png").convert()

win.blit(background, (0, 0))

a = 50

clock = pygame.time.Clock()

fontgameover = pygame.font.SysFont("Pixeboy", 160)
fontscore = pygame.font.SysFont("Pixeboy", 50)
fontagain = pygame.font.SysFont("Pixeboy", 50)


def snakeyy(arrsnakey, x, y):
    for i in arrsnakey:
        [(pygame.draw.rect(win, pygame.Color(252, 186, 3), [i, j, a, a]))
         for i, j in arrsnakey]


def scoresee(score):
    scoresee = fontscore.render(f'SCORE: {score}', 1, pygame.Color('brown'))
    win.blit(scoresee, [0, 0])


def gameoverseee():
    gameoversee = fontgameover.render('GAME OVER', 1, pygame.Color('red'))
    win.blit(gameoversee, [w/6, h/3])


def start_againsee():
    start_againsee = fontagain.render(
        'Press space to start again', 1, pygame.color('red'))
    win.blit(start_againsee, [w/6, h/3+10])


def cookiee():
    cookiex = randrange(0, 1040, a)
    cookiey = randrange(0, 740, a)
    win.blit(cookie, (cookiex, cookiey))
    pygame.display.flip()


def treee():
    treex = randrange(0, 1040, a)
    treey = randrange(0, 750, a)
    win.blit(tree, (treex, treey))


def collide_with_tree(treex, treey, x, y, score, gameover):
    if x == treex and y == treey:
        game_over(score, gameover)
        pygame.display.update
        exit_from_game(gameover)


def eating_cookie(cookiex, cookiey, x, y, leng, head, arrsnakey, score):
    if x == cookiex and y == cookiey:
        cookiee()
        leng += 1
        head = [x, y]
        arrsnakey.append(head)
        score += 1
        treee()
        pygame.display.update()
        pygame.display.flip()


def game_over(score, gameover):
    win.blit(background, (0, 0))
    start_againsee()
    gameoverseee()

    scoresee(score)
    pygame.display.update()
    exit_from_game(gameover)


def exit_from_game(gameover):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
            exit()


def gameplay():
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

            if x == cookiex and y == cookiey:
                eating_cookie(cookiex, cookiey, x, y,
                              leng, head, arrsnakey, score)

                win.blit(background, (0, 0))

                cookiex = randrange(0, 1040, a)
                cookiey = randrange(0, 740, a)

                win.blit(cookie, (cookiex, cookiey))

                treex = randrange(0, 1040, a)
                treey = randrange(0, 740, a)
                win.blit(tree, (treex, treey))

                score += 1

                pygame.display.update

            if x == treex and y == treey:
                closing = True
                collide_with_tree(treex, treey, x, y, score, gameover)
                game_over(score, gameover)

            if x >= w or x < 0 or y >= h or y < 0:
                closing = True

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
            # pygame.display.update()

            pygame.display.flip()
            clock.tick(1000)


if __name__ == "__main__":
    gameplay()
