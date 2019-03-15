class Polynomial(object):
    def __init__(self, deg, coef):
        if deg + 1 != len(coef):
            raise Exception(f'A polynomial of degree {deg} should have {deg + 1} terms')
        
        if coef[deg] == 0:
            raise Exception(f'A polynomial should have a non-zero leading coefficient')

        else:
            self.deg = deg
            self.coef = coef

    def monic_reduce(self):
        lead_coef = self.coef[self.deg]

        for i in range(self.deg + 1):
            self.coef[i] /= lead_coef

    def __getitem__(self, index):
        result = 0

        for i in range(self.deg + 1):
            result += self.coef[i] * index ** i
        
        return result

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
    
    def __mult__(self, other):
        raise NotImplementedError('Polynomial multiplication is not implementated yet')
    
    def __pow__(self, power):
        raise NotImplementedError('') # Will use Pascal's Triangle for fast computation

    def __eq__(self, other):
        if self.deg != other.deg:
            return False
        
        for i in range(self.deg + 1):
            if self.coef[i] != other.coef[i]:
                return False

        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        coef_mag = [abs(x) for x in self.coef]

        string = f'{self.coef[self.deg]}x^{self.deg}'

        for i in range(self.deg - 1, 1, -1):
            if self.coef[i] > 0:
                string += f' + {coef_mag[i]}x^{i}'
            elif self.coef[i] < 0:
                string += f' - {coef_mag[i]}x^{i}'

        if self.coef[1] > 0:
            string += f' + {coef_mag[1]}x'
        elif self.coef[1] < 0:
            string += f' - {coef_mag[1]}x'

        if self.coef[0] > 0:
            string += f' + {coef_mag[0]}'
        elif self.coef[0] < 0:
            string += f' - {coef_mag[0]}'

        return string