
#Problem 1
def fib(n):
    n1, n2 = 0, 1
    count = 0

    if n <= 0:
        print("Invalid number")
    
    elif n == 0:
        print(n1)

    elif n == 1:
        print(n2)
    
    elif n > 1:
        while count < n:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1


#Problem 2
class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self): 
        return self.x

    def getY(self):
        return self.y

    def add(self, v):
        
        





v = vector(11, 12)

