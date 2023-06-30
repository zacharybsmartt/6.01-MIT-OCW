
# #Problem 1
# def fib(n):
#     n1, n2 = 0, 1
#     count = 0

#     if n <= 0:
#         print("Invalid number")
    
#     elif n == 0:
#         print(n1)

#     elif n == 1:
#         print(n2)
    
#     elif n > 1:
#         while count < n:
#             print(n1)
#             nth = n1 + n2
#             n1 = n2
#             n2 = nth
#             count += 1


# #Problem 2
# class vector:


#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def getX(self):
#         return self.x

#     def getY(self):
#         return self.y

#     def add(self, v):
#         sum_x = self.x + v.getX()
#         sum_y = self.y + v.getY()

#         return print('[{}, {}]'.format(sum_x,sum_y))

#     def mul(self, scalar):
#         prod_x = scalar * self.x
#         prod_y = scalar * self.y

#         return print('[{}, {}]'.format(prod_x, prod_y))

#     def __str__(self):
#         return ('[{}, {}]'.format(self.x, self.y))

#     def __add__(self, v):
#         return self.add(v)

#     def __mul__(self, scalar):
#         return self.mul(scalar)


# v = vector(1.1, 2.2)
# b = vector(4, 1)

# print(v)
# v.add(b)
# b.mul(8)

# vector(2, 2) + vector(2,2)
# vector(3.14159, 2.71828183) * 10



# Problem 3
class Polynomial:


    def __init__(self, coefficients):
        self.coefficients = coefficients


    def coef(self, i):
        print(self.coefficients[::-1][i])
        return self.coefficients[::-1][i]
    
    def add(self, other):
        print(self.coefficients)
        print(len(self.coefficients))
        print(other.coefficients)
        print(len(other.coefficients))
        if len(self.coefficients) < len(other.coefficients):
            while len(self.coefficients) < len(other.coefficients):
                self.coefficients.append(0)
                coef_sum = [self.coefficients[i] + other.coefficients[i] for i in enumerate(self.coefficients)]
                print(coef_sum)
                return coef_sum
    
        elif len(self.coefficients) > len(other.coefficients):
            while len(self.coefficients) > len(other.coefficients):
                other.coefficients.append(0)
                coef_sum = [self.coefficients[i] + other.coefficients[i] for i in enumerate(self.coefficients)]
                print(coef_sum)
                return coef_sum


a = Polynomial([6, 4, 2, 1])
b = Polynomial([1, 2, 4])
a.coef(3)
a.add(b)
