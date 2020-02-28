a=int(input('Enter the size of rows in matrix 1: '))
b=int(input('Enter the size of columbs in matrix 1: '))
c=int(input('Enter the size of rows in matrix 2: '))
d=int(input('Enter the size of columbs in matrix 2: '))

x=[[int(input()) for i in range(a)]for j in range(b)]

y = [[int(input()) for i in range(c)]for j in range(d)]

result = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            result[i][j] += x[i][k] * y[k][j]

for r in result:
    print(r)