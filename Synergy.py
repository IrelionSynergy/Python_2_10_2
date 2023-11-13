numbers = dict()
print('Введите диапазон чисел')
fromNumber = int(input('от (включительно): '))
toNumber = int(input('по (включительно): '))

for i in range(fromNumber, toNumber):
    numbers[f'{i}'] = i * i

for key in numbers:
    value = numbers[key]
    print(f'"{key}" : {value}')