# def add(**num):
#     z = num['a'] + num['b'] + num['c']
#     print('addition: ',z)
# add(a=5,b=2,c=4,d=6)
#
# #지역변수와 전역변수
# i = 1
# def plus1():
#     b = i + 1
#     print('i =', b)
# plus1()

a=50
def show():
    a = 10
    print('show a:', a)

show()
print(a)

def show2():
    global a
    print('show2-a',a)
    a = 20
    print('show2-a2',a)
show2()
print('a:',a)