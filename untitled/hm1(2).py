n = int(input('n = '))

array = []
for i in range(n):
    x = int(input(f'x[{i}] = '))
    array.append(x)

array.sort()
print(array[-2], array[-1])