import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,100)
y  = x + np.random.random(x.shape[0])*0.3 + 0.7


class gradientAgent():
    def __init__(self):
        self.wheight = 4
        self.basis = -5
    
    
    def descent(self,x:np.ndarray,y:np.ndarray,dw = 0.1,db = 0.1, rate = 0.1):
        
        dydw  = ( 
            ((x*(self.wheight + dw ) + self.basis) - y)**2 - 
            ((x*(self.wheight - dw ) + self.basis) - y)**2
            )/(2*dw)
        

        dydb  = ( 
            ((x*(self.wheight) + self.basis + db) - y)**2 - 
            ((x*(self.wheight) + self.basis - db) - y)**2
            )/(2*db)
        
        self.wheight -= dydw.mean()*rate
        self.basis -= dydb.mean()*rate

    def predict(self,x):
        return self.wheight*x + self.basis
    
        

test_agent = gradientAgent()

weight_line = np.linspace(-5,5,100)
basis_line = np.linspace(-5,5,100)
a,b = np.meshgrid(weight_line,basis_line)
z = ((((a*x) + b)-y)**2)
print(z)
basis_time = []
weight_time = []


fig, ax = plt.subplots(1,2)
def show_descent():
    ax[0].contourf(weight_line,basis_line,z,50)
    #plt.colorbar()
    for i in range(1,1000):
        test_agent.descent(x,y,0.1,0.1,0.01)
        basis_time.append(test_agent.basis)
        weight_time.append(test_agent.wheight)
        ax[0].plot(basis_time,weight_time,color="white")
        

        ax[1].plot(x,y)
        ax[1].plot(x,test_agent.predict(x))
        plt.pause(0.01)
        ax[1].cla()
    
    ax[1].plot(x,y)
    ax[1].plot(x,test_agent.predict(x))

show_descent()
plt.show()
