a = list(map(int, input().split()))
b = list(map(int, input().split()))
product = sum(list(map(lambda x: x[0]*x[1], list(zip(a, b)))))
print(product)