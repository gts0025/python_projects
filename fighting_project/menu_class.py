#main_menu
import pygame
pygame.init()
from random import randint

class Button:
    def __init__(self,text:str = None ,quad = [0,0,0,0],t_color = "white",q_color = (50,50,50),action:function = 0):
        self.quad = quad
        self.text  = text
        self.quad_color = q_color
        self.text_color = t_color
        self.action = action
        self.fonts = pygame.font.SysFont("Arial",round(quad[3]/2))
        self.text_pos = (self.quad[0]+(quad[3]/2),self.quad[1]+2)
        
    
    def render(self,surface):
        self.render_text = self.fonts.render(self.text, True,self.text_color)
        pygame.draw.rect(surface,self.quad_color,self.quad)
        
        if self.text != None:
            surface.blit(self.render_text,self.text_pos)
    
    def is_holver(self):
        mouse_pos = pygame.mouse.get_pos()
        if (mouse_pos[0] > self.quad[0] and 
            mouse_pos[1] > self.quad[1] and
            mouse_pos[0] < self.quad[0]+self.quad[2] and 
            mouse_pos[1] < self.quad[1]+self.quad[3]
            ):
            return True
        
    def click(self, s):
        if self.is_holver():
            pressd = pygame.mouse.get_pressed()
            if pressd[0] == True:
                self.action()
                    
        
class slider(Button):
    def __init__(quad):
        super().__init__(quad=quad)
        
class Menu:
    def __init__(self,button_list:list, background_color = "black"):
        self.button_list = button_list
        self.background_color = background_color
            
    def run(self,loop,surface):
        if loop:
            for button in self.button_list:
                button.render(surface)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
  

