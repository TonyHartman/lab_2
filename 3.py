'''
x = input()
s = 0
for i in range(len(x)):
    s += int(x[i])
print(s)
но это явно не то, чего хотят)
'''
x = int(input())
numbers = []
while x > 0:
    numbers.append(x % 10)
    x = x // 10
print(sum(numbers))
