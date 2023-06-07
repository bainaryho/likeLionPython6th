print('인자가 없는 함수')
def disp():
    name = '멋쟁이 사자'
    print("Welcome to", name)
disp()

print('인자가 1개인 함수')
def disp1(name):
    print("Welcome to", name)
disp1('멋쟁이 사자')

print('인자가 2개인 함수')
def disp2(str1,name):
    print(str1, name)
disp2('Welcome to','멋쟁이 사자')

print('가변 매개 함수')
def disp3(*keywords):
    for i in keywords:
        print(i,end=' ')
disp3('welcome','to','멋쟁이','사자')

print('\nadd 함수만들기')
def add(y):
    x = 10.2334
    print(x + y)
    print(f"Formatted Output {x+y:10.2f}")
    #{x+y:.2f} .2f앞에 나오는 숫자는 출력하는 공간의 크기, 10으로하면 차이가 보이네
add(20)

print('add return만들기')
def add1():
    x = 10
    y = 20
    return x+y
print(add1())

def add(y):
    x = 10
    c = x + y
    d = y - x
    return c, d, 30
print(add(10))

