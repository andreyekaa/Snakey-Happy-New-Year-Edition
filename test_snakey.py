import unittest
import main
import pygame
import unittest.mock


class TestGames(unittest.TestCase):
    def test_button_click(self):
        dx, dy = 0, 0
        key = {pygame.K_UP: True, pygame.K_w: False, pygame.K_DOWN: False, pygame.K_s: False,
                pygame.K_LEFT: False, pygame.K_a: False,  pygame.K_RIGHT: False, pygame.K_d: False}
        self.assertEquals(main.buttons_click(dx, dy, key), (0, -50))

        key[pygame.K_UP] = False
        key[pygame.K_DOWN] = True
        self.assertEquals(main.buttons_click(dx, dy, key), (0, 50))
        
        key[pygame.K_DOWN] = False 
        key[pygame.K_a] = True
        self.assertEquals(main.buttons_click(dx, dy, key), (-50, 0))

        key[pygame.K_a] = False 
        key[pygame.K_d] = True
        self.assertEquals(main.buttons_click(dx, dy, key), (50, 0))

    def test_record_less(self):
        main.record
        score = 10
        sc = 20
        self.assertEquals(main.record(score, sc), sc)

    def test_record_more(self):
        main.record
        score = 24
        sc = 20
        self.assertEqual(main.record(score, sc), score)

    def test_colliding_with_walls(self):
        '''Удар со стенами.'''
        self.assertTrue(main.colliding_with_walls(-10, 10, 20, 20))  
        self.assertTrue(main.colliding_with_walls(10,-1, 20, 20)) 
        self.assertTrue(main.colliding_with_walls(21, 10, 20, 20))  
        self.assertTrue(main.colliding_with_walls(10,21, 20, 20)) 
        '''Нет удара со стенами'''
        self.assertFalse(main.colliding_with_walls(19, 10, 20, 20))  
        self.assertFalse(main.colliding_with_walls(10,19, 20, 20)) 
                    
         
