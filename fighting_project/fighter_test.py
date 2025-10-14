

import pygame
from fighter_class import Fighter


pygame.init()
screen =pygame.display.set_mode([400,400])
loop = 1
value = 0
def print_value():
    print(value)

fighter_test = Fighter()
held = []
clock = pygame.time.Clock()
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            held.append(event.key)
        if event.type == pygame.KEYUP:
            held.remove(event.key)
    print(held)
    for i in held: 
        match i:
            case 97:
                fighter_test.walk(-2)
            case 100:
                fighter_test.walk(2)

    screen.fill("black")   
    fighter_test.show(screen)
    fighter_test.update()
    
    pygame.display.flip()
    clock.tick(60)
    
    

#update