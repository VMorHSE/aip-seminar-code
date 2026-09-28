# Есть три вида "манипуляторов" переменными
# 1. Операторы
# 2. Функции
# 3. Методы

a = ['1', 2, True]
b = [7, False]
c = a + b # Оператор +
c.append('t') # Метод append класса list (класс = тип)

# def len(l):
#   ...
ln = len(c) # Функция len

print(c, ln)

b = 't' in c # Оператор
c.pop() # Метод
#cs = sorted(c) # Функция


# Код, который пишем мы
def length(v):
    return ((v.x)**2+(v.y)**2)**0.5

def initilize(v, x, y):
    v.x = x 
    v.y = y 
    
class vector:

    def length(self):
        return ((self.x) ** 2 + (self.y) ** 2) ** 0.5

    def initilize(self, x, y):
        self.x = x 
        self.y = y
    
    
    

# Код, который пишет пользователь

w = vector()
w.x = 6
w.y = 5

r = length(w)
print(r)

c = vector()
c.coord_x = 10
c.coord_y = 20

# print(length(c))

l = vector()
initilize(l, 10, 20)
print(length(l))

m = vector()
m.initilize(20,10)
print(m.length())

sp = [1,3,2,5,7,3,]
print(sp)
sp.append(9)
print(sp)
sp.pop()
print(sp)
sp.pop(0)
print(sp)

# class list:
#   ...
#   def insert(self, pos, val)

sp.insert(3,10)
print(sp)
print(sp.index(5))
sp.reverse()
print(sp)
sp.extend([1,2,3])
print(sp)
c = sp.count(3)
print(c)
sp.extend(range(5))
print(sp)

b = []
for k in sp:
    b.append(k**2)
b = [q**2 for q in sp]

x = sp[4]

marks = [10, 8, 9, 10, 7, 5, 6, 10, 10, 8, 9]

students = [c for c in 'ABCDEFGHIJK'] # list('ABCDEFGHIJK')

mark = marks[students.index('D')] # Оценка студента D

# "Словари" - ассоциативные массивы - упорядоченная коллекция элементов, но ключи - произвольных типов (а не только числа)

marks_d = {'A' : 10, 'B' : 8, 'C' : 9}

marks_d = {name : marks[students.index(name)] for name in students}

print(marks_d)

print(marks_d['E']) # print specific element

marks_d['L'] = 7 # make new element named 'L'
# will NOT work if you try to just index it w/o setting a value

print(marks_d['L']) # element should effectively exist

# using cycles on dictionaries
for name in marks_d.keys(): # keys only
    print(name, end=' ') # print all dict.' keys
    # note that this does not print the values of those keys
print()
for marks in marks_d.values():
    print(marks, end=' ') # print all dict.' keys' values
    # note that this does not print the keys of those values
print()
for name, marks in marks_d.items():
    print(name, marks, sep=": ", end='\n') # print all dict. contents
    
# [ End of the 2026-09-28 seminar ]