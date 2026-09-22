# Дан массив чисел, найти наибольшее число в массиве и вывести его
arr  = [1, 8, 0, -1, 59, 8, 79, 101, 9, -115, 16]
q=arr[0]
for hp in arr:
    if hp>q:
        q=hp
print(q)


# Пользователь последовательно вводит числа
# Когда пользователь вводит 0, ввод считает завершённым
# Найти минимум введённых чисел
n = int(input())
l = []

while n != 0:
    l.append(n)
    n = int(input())
m = l[0]
for num in l:
    if m > num:
        m = num
print(m)

n = int(input())
result = n
while n != 0:
    n = int(input())
    if result > n:
        result = n
print(result)

# Пользователь вводит данные следующего вида:
# число
# +, -, *, / (одно из)
# число
# Программа должна вывести резульатта запрошеноой операции,
# поддерживаются только +, -, *, /

x = float(input())
op = input()
while op not in ['+','-','*','/']:
    print('Поддерживаются только +,-,*,/')
    op = input()
y = float(input())
while y == 0 and op == '/':
    print('На ноль делить нельзя')
    y = float(input())
if op == '+':
    print(x + y)
elif op == '-':
    print(x - y)
elif op == '*':
    print(x * y)
elif op == '/':
    print(x/y)


# Сделать функицю, которая находит среднее значение чисел в списке
def sr(numbers):
    if not numbers:
        raise ArithmeticError()
    summ = 0
    count = 0
    for number in numbers:
        summ += number
        count += 1
    return summ / count
a = [2, 3, 4 , 8]
print(sr(a))

# Сделать класс для веткора в 2D пространстве
# Посчитать сумму списка таких векторов: (0, 1), (1, 2), (2, 3), (3, 4)

class vector:
    pass


v_arr = []

for i in range(4):
    v = vector()
    v.x = i
    v.y = i + 1
    v_arr.append(v)

v_sum = vector()
v_sum.x = 0
v_sum.y = 0

for vec in v_arr:
    v_sum.x += vec.x
    v_sum.y += vec.y

print(v_sum.x, v_sum.y)




