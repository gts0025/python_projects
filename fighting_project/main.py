#setup
import json 
import pygame
import menu_class

pygame.init()

class game:
    def __init__(self):
        self.screen = pygame.display.set_mode()
        self.data = []

class menu:
    def __init__(self,screen):
        self.screen = screen
        self.buttons = []

class fighter:
    def __init__(self):
        self.hp = 100
        self.color = "red"
        self.x = 100
        self.heavy = None
        self.light = None
        self.state  = (0,0)
        

    def show(self,surface:pygame.Surface):
        pygame.draw.rect(surface, "red",[self.x,100,100,100])
    

    
        
#update