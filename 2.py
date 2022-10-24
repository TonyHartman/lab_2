d = [1, 2, 4, 9, 100, 64]
squares = [i**2 for i in range(1, 10)]
d = list(filter(lambda x: x in squares, d))
print(d)
# добавлять генератор прямо в lambda будет работать дольше
