print('ㅇ거듭제곱함수')
def pw(x,y):
    z = x**y
    print(z)
pw(2,5)

print('ㅇ아규먼트 2개인 함수')
def show(name,age):
    print(f"Name:{name} Age:{age}")
show('이진호','24')

print('함수실습2')
def add(*num):
    z = num[0] + num[1] + num[2]
    print('add : ',z)
add('5','2','4')

print('함수실습3')
def add(x, *num):
    z = x + num[0] + num[1]
    print('Add x *: ',z)
add(5, 2, 4, 5)
