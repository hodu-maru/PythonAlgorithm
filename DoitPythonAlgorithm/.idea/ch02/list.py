x = ['Joy','Garen','Paul','Ringo']

for i in range(len(x)):
    print(f'x[{i}] = {x[i]}')

print()
for i, name in enumerate(x):
    print(f'x[{i}] = {name}')

print()

for i, name in enumerate(x,1):
    print(f'{i}번째 = {name}')

print()

for i in x:
    print(i)

