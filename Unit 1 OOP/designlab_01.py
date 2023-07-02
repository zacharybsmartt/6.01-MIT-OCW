
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


    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __str__(self):
        coefficients = self.coefficients[::-1]  # Reverse the coefficients list
        polynomial_str = ""

        for i, coef in enumerate(coefficients):
            if coef == 0:
                continue

            # Handle special cases for the first and last coefficients
            if i == 0:
                term_str = str(coef)
            elif i == 1:
                term_str = f"{coef}x"
            else:
                term_str = f"{coef}x^{i}"

            # Add the term string to the polynomial string
            if polynomial_str:
                polynomial_str = term_str + " + " + polynomial_str
            else:
                polynomial_str = term_str

        return polynomial_str

    def coef(self, i):
        print(self.coefficients[::-1][i]) #check
        return self.coefficients[::-1][i]
    
    def add(self, other):

        P1 = self.coefficients.copy()
        P2 = other.coefficients.copy()

        if len(P1) > len(P2):
            while len(P2) < len(P1):
                P2.append(0)
            coeff_sum = [sum(x) for x in zip(P1, P2)]
            print(coeff_sum) #check
            return coeff_sum

        elif len(P1) < len(P2):
            while len(P2) > len(P1):
                P1.append(0)
            coeff_sum = [sum(x) for x in zip(P1, P2)]
            print(coeff_sum) #check
            return coeff_sum

        else:
            coeff_sum = [sum(x) for x in zip(P1, P2)]
            print(coeff_sum) #check
            return coeff_sum
        
    def mul(self, other):
        P1 = self.coefficients
        P2 = other.coefficients
        degree1 = len(P1) - 1
        degree2 = len(P2) - 1

        # Create a list to store the resulting coefficients
        result = [0] * (degree1 + degree2 + 1)

        # Iterate over the coefficients of the first polynomial
        for i in range(len(P1)):
            # Within the first iteration, iterate over the coefficients of the second polynomial
            for j in range(len(P2)):
                # Multiply the coefficients and add the result to the corresponding position in the result list
                result[i + j] += P1[i] * P2[j]

        return result

    def val(self, v):
        degree = len(self.coefficients) - 1
        eval_coeff = []

        for element in self.coefficients:
            eval_coeff.append(element * (v ** degree))
            degree -= 1
        
        eval_total = sum(eval_coeff)
        print(eval_total)
        return eval_total

    def __add__(self,other):
        return self.add(other)
    
    def __mul__(self,other):
        return self.mul(other)
    
    def __call__(self, x):
        return self.val(x)
    
    def __repr__(self):
        return str(self)
    
a = Polynomial([1, 2, 3, 4])
a.val(4)
