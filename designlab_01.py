
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
        sum_x = self.x + v.getX()
        sum_y = self.y + v.getY()

        return print('[{}, {}]'.format(sum_x,sum_y))

    def mul(self, scalar):
        prod_x = scalar * self.x
        prod_y = scalar * self.y

        return print('[{}, {}]'.format(prod_x, prod_y))

    def __str__(self):
        return ('[{}, {}]'.format(self.x, self.y))

    def __add__(self, v):
        return self.add(v)

    def __mul__(self, scalar):
        return self.mul(scalar)


v = vector(1.1, 2.2)
b = vector(4, 1)

print(v)
v.add(b)
b.mul(8)

vector(2, 2) + vector(2,2)
vector(3.14159, 2.71828183) * 10



# Problem 3
class Polynomial:


    def __init__(self, args):
        self.a = args[0]
        self.b = args[1]
        self.c = args[2]
    
    def __str__(self):
        a = self.a
        b = self.b
        c = self.c
        return print('{} z**2 + {} z + {}'.format(a, b, c))
    
    def add(self, poly):
        sum_a = self.a + poly.a
        sum_b = self.b + poly.b
        sum_c = self.c + poly.c
        return print('{} z**2 + {} z + {}'.format(sum_a, sum_b, sum_c))
    
    def __add__(self, poly):
        return self.add(poly)

# follow the lab manual, didnt even know they had that. Just scroll down

a = Polynomial([1, 2, 3])
b = Polynomial([3, 2, 1])
a.add(b)
a + b
