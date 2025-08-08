import numpy as np, pygame as pg
window = [400,400]  
pg.init()
screen = pg.display.set_mode(window)
clock  = pg.time.Clock()
dt = 0.1

class graph:
    data: list
    limit: int

    def __init__(self, limit: int):
        self.data = []
        self.limit = limit
        self.full = False

    def push(self, point: float):
        self.data.append(point)
        if len(self.data) > self.limit:
            self.data.pop(0)
       
    def mean(self):
        return sum(self.data)/len(self.data)      

class Spring:

    pos:np.ndarray
    vel:np.ndarray
    k:float

    def __init__(self,pos, vel, k ):
        "vel, pos: numpy array,  k: float"
        self.pos = pos
        self.vel = vel
        self.k = k

    def update(self):
        self.pos += self.vel*dt
        pg.draw.circle(screen,"red",self.pos,10)
    
    
def hook(a:Spring, b: Spring, rest_length: float, k: float):
    displacement = b.pos - a.pos
    distance = np.linalg.norm(displacement)
    if distance == 0:
        return  # avoid division by zero
    direction = displacement / distance
    force = k * (distance - rest_length) * direction
    a.vel += force * dt
    b.vel -= force * dt


test1 = Spring(np.array([200,200],float),np.array([1,0],float),0.1)
test2 = Spring(np.array([100,200],float),np.array([0,0],float),0.1)

loop = 1
frame_stack = graph(10)
frame_stack.push(10)
while loop:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            loop = 0
    screen.fill("black")
    test1.update()
    test2.update()
    hook(test1,test2,20,(test1.k+test2.k)/2)
    pg.display.flip()
    
  
    
    