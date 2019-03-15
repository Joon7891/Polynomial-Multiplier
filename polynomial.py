class Polynomial(object):
    def __init__(self, deg, coef):
        if deg + 1 != len(coef):
            raise Exception(f'A polynomial of degree {deg} should have {deg + 1} terms')
        
        if coef[deg] == 0:
            raise Exception(f'A polynomial should have a non-zero leading coefficient')

        else:
            self.deg = deg
            self.coef = coef

    def __add__(self, other):
        deg = max(self.deg, other.deg)
        coef = [0] * (deg + 1)

        for i in range(deg + 1):
            if i <= self.deg:
                coef[i] += self.coef[i]

            if i <= other.deg:
                coef[i] += other.coef[i]
        
        while coef[deg] == 0:
            coef = coef[:deg]
            deg -= 1

        return Polynomial(deg, coef)
    
    def __sub__(self, other):
        deg = max(self.deg, other.deg)
        coef = [0] * (deg + 1)

        for i in range(deg + 1):
            if i <= self.deg:
                coef[i] += self.coef[i]

            if i <= other.deg:
                coef[i] -= other.coef[i]
        
        while coef[deg] == 0:
            coef = coef[:deg]
            deg -= 1

        return Polynomial(deg, coef)

    def __str__(self):
        string = f'{self.coef[self.deg]}x^{self.deg}'

        for i in range(self.deg - 1, -1, -1):
            if self.coef[i] > 0:
                string += f' + {self.coef[i]}x^{i}'
            elif self.coef[i] < 0:
                string += f' - {abs(self.coef[i])}x^{i}'

        return string