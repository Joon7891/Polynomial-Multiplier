from polynomial import Polynomial
from complex import Complex

a = Polynomial(2, [-3, -2, 3])
b = Polynomial(2, [-3, 4, 3])

print(a)
a.monic_reduce()
print(a)

d = Complex(0, -20)

print(d)

for i in range(10):
    print(a[i])