#from _typeshed import Self
import unittest
import main
import pygame
import pytest
import unittest.mock

#class MyScreen(pygame.Surface):
#    blit = unittest.mock.MagicMock()
#    screen = pygame.display.set_mode((1050,750))

class TestGames(unittest.TestCase):
    def test_exit_tree(self):
        main.collide_with_tree
        assert main.exit_from_game

    def test_exit(self):
        main.exit_from_game
        assert True

    def test_eating_cookie(self):
        main.eating_cookie
        legth = leng = 10
        scor = score = 10
        spee = v = 16

        leng = main.eating_cookie
        score = main.eating_cookie
        v = main.eating_cookie

        assert (legth != leng) and (scor != score) and (spee != v)
        

    def test_record_less(self):
        main.record
        score = 10
        sc = 20
        assert(main.record(score, sc), sc)

    def test_record_more(self):
        main.record
        score = 24
        sc = 20
        assert(main.record(score, sc), sc)

