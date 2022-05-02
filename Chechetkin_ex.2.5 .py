price = [21.54, 88.21, 65.32, 85.06, 10.11, 99.99, 92.88, 43.43, 38.87, 84.2]
#print('Вывести на экран эти цены через запятую в одну строку')
for z in price:
    print(f'{int(z)} руб. {int(z * 100 % 100):02} коп.', end=", ")
# Вывести цены, отсортированные по возрастанию
print(f'{price}{id(price)}')
price.sort()
print('Cортировка по возрастанию')
print(f'{price}{id(price)}')
# Вывести цены, отсортированные по убыванию
reverse_price = sorted(price, reverse=True)
print(f'{reverse_price}')

print('5 самых дорогих')
print(price[-5:])