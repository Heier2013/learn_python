# def power(x, n=2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s

# print( power( 2 ) )

# def enroll(name, gender, age=6, city='Beijing'):
#     print('name:', name)
#     print('gender:', gender)
#     print('age:', age)
#     print('city:', city)

# enroll('heier', 'F', city='test')

# def add_end(L=[]):
#     L.append('END')
#     return L

# print( add_end() )

# print( add_end() )

# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L

# print( add_end() )

# print( add_end() )

# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print( calc(*[1, 2, 3]) )

# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30, city='beijing', test='test')

# 命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)

person( 'Heier', '22', city='zhengzhou', job='IT' )

# 使用参数组合
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)