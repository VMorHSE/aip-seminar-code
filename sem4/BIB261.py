l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2 # Оператор +
l3.append(42) # Метод .append
x = len(l3) # Функция len
print(l3, x) # Функция print

s1 = 'abc'
s2 = s1 * 3 # Оператор *
print(s2) # Функция

b = 'a' in s2 # Оператор in

l3.pop() # Метод pop

class vector:
    # Метод initialize класса vector
    def initialize(self, x, y):
        self.x = x
        self.y = y
    # Метод dln класса vector
    def dln(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

v4 = vector()
v4.initialize(4, 8)
print(v4.dln())


v1 = vector()
v1.x = 1
v1.y = 2

def dln(v):
    return (v.x ** 2 + v.y ** 2) ** 0.5

a = dln(v1)

v2 = vector()
v1.X = 1
v1.Y = 2

#a_1 = dln(v2)

def initialize(v, x, y):
    v.x = x
    v.y = y
    
v3 = vector()
initialize(v3, 5, 7)

print(dln(v3))


l = [1, 2, 3]
l.append(4) # Метод append класса list

# class list:
#   def append(self, x):
#       ...

l.pop()
print(l)
l.pop(0)
print(l)

l.insert(0,5)
print(l)

l.reverse()
print(l)
a = l.index(3)
print(a)
l.extend([9,8,7])

ll=[]
for t in l:
    ll.append(t**2)

ll = [t**2 for t in l]

l = [10, 21, 34, 47, 59, 60]

x = l[2] # 34

marks_l = [10, 8, 7, 7, 8, 9, 9, 10, 4, 5]
students = [c for c in 'ABCDEFGHIJ']

n = students.index('D')
marks_l[n]

marks_l[students.index('D')]

# ассоциативные массивы - "словари" - упорядоченная коллекция элементов

marks = {'A' : 10, 'B' : 8, 'C' : 7}
marks['C']

marks = {name : marks_l[students.index(name)] for name in students}

powers = {x : 2 ** x for x in [1, 2, 3, 4, 5, 6]}

print(marks)
print(powers)


for mark in marks_l:
    print(mark)
    
for key in powers.keys():
    print(key)
    
for val in powers.values():
    print(val)

for key, val in powers.items():
    print(key, "=>", val)




