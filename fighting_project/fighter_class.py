import pygame

class atack:
    def __init__(
            
            self,
            cooldown = 0,
            hit_range = 0,
            damage = 0,
            hitbox = [0,0,10,10]
            
            ):

        self.cooldow = cooldown
        self.hit_range = hit_range
        self.damage = damage
        self.hitbox = hitbox

class Fighter:
    def __init__(
            self, hp = 100,
            color = "red",
            heavy = None,
            light = None,
            state = ["iddle",0],
            facing = 0,
            hitbox = [10,200,100,100],
            x = 100
            ):
        
        self.hp = hp
        self.color = color
        self.x = x
        self.heavy = heavy
        self.light = light
        self.state  = state
        self.facing = facing
        self.hitbox = hitbox

    def update(self):
        if self.state[0] != "iddle":
            if self.state[1] > 0:
                self.state[1] -= 1 
            else:self.state = ["iddle",0]

    def walk(self,d):
        if self.state[0] == "walking" or "iddle":
            self.x += d
            self.hitbox[0] = self.x
            self.state = ["walking",1] #cooldown
    
    def show(self,surface:pygame.Surface):
        self.hitbox[0] = self.x
        pygame.draw.rect(surface, self.color,self.hitbox)


