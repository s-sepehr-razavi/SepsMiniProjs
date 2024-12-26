import numpy as np
class Value:
    def __init__(self,v):
        self.v = v
        
    def __add__(self, other):
        return Value(max(self.v, other.v))
    
    def __mul__(self, other):
        return Value(min(self.v, other.v))
    
    def __pos__(self):
        return Value(self.v**2)
    
    def __neg__(self):
        return Value(self.v**0.5)
    
    def __str__(self):
        return str(self.v)
    
class Function:

    def __init__(self, type, **params):

        self.func = 1
        self.type=type
        if type == "tri":
            self.a = params['a']
            self.b = params['b']
            self.c = params['c']            
            self.func = self._triangle

        if type == 'trap':
            self.func = params['func']
            self.a=params['a']
            self.c=params['c']

    
    def _triangle(self, x):
        """
        Vectorized triangular membership function.
        
        Parameters:
        - x: np.ndarray or scalar, input values
        
        Returns:
        - np.ndarray or scalar, membership values
        """
        x = np.asarray(x)  # Ensure x is a NumPy array for element-wise operations

        # Calculate membership values
        left_slope = (1 / (self.b - self.a)) * (x - self.a)
        right_slope = (1 / (self.c - self.b)) * (self.c - x)
        
        # Combine conditions
        membership = np.where((x >= self.a) & (x < self.b), left_slope, 0)  # Rising edge
        membership = np.where((x >= self.b) & (x < self.c), right_slope, membership)  # Falling edge
        
        return membership


    def __call__(self, x):
        return self.func(x)
    
    
    def implication(self, type, alpha):
        if type == 'mamdani':            
            return Function(type='trap', func = lambda x: np.minimum(alpha, self(x)), a=self.a, c=self.c)
    

    def concentration(self):
        return Function(type='trap', func = lambda x: self(x)**2, a=self.a, c=self.c)
    
    
    def dialation(self):
        return Function(type='trap', func = lambda x: self(x)**(0.5), a=self.a, c=self.c)


class Term:

    def __init__(self, f:Function):
        self.f = f
    
    def __call__(self, v):        
        return Value(self.f(v))
    
    def __pos__(self):
        f = self.f.concentration()
        return Term(f)
    
    def __neg__(self):
        f = self.f.dialation()
        return Term(f)
    
    def __lshift__(self, other:Value):
        
        assert type(other) == Value, "You should provide an object of type value on the leftside of the implication"
        return self.f.implication('mamdani', other.v) # dirty

class Defuzzifier:

    def __init__(self, type):
        self.type = type
        if type == 'mom':
            self.func = self._mom

    
    def __call__(self, functions: list[Function]):
        return self.func(functions)

   
    def _mom(self, functions: list[Function]):   
        result = 0     
        for f in functions:            
            if f.type == 'trap':
                x = np.linspace(f.a, f.c, 10000)
                y = f(x)                
                maxs = x[y == y.max()]
                print(maxs[len(maxs)//2])
                result+=maxs[len(maxs)//2]
        return result / len(functions)
