import cmath
a = int(input('Enter a new number: '))
b = int(input('Enter a new number: '))
c = int(input('Enter a new number: '))

d = (b ** 2) - (4 * a * c)
sol1 = (-b - cmath.sqrt(d)) / (2 * a)
sol2 = (-b + cmath.sqrt(d)) / (2 * a)
print('The solution are {0} and {1}'.format(sol1, sol2))