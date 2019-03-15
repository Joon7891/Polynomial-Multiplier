class Complex(object):
    def __init__(self, real = 0, imag = 0):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)
    
    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag, self.real * other.imag + other.real * self.imag)
    
    def __str__(self):
        if self.real == 0 and self.imag == 0:
            return '0'
        
        if self.real == 0:
            return f'{self.imag}i'
        
        if self.imag == 0:
            return f'{self.real}'
        
        return f'{self.real}' + f' + {self.imag}i' if self.imag > 0 else f' - {abs(self.imag)}i'