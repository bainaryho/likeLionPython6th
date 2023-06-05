#논리 연산자
a=5
b=2
c=3
d=200

print('AND연산자')
print('a > b and a < c: ', a > b and a < c) #a > b and a < c:  False

print('OR연산자')
print('a > b or a < c: ', a > b or a < c) #a > b or a < c:  True

print('NOT연산자')
print('not(a < b): ', not(a < b)) #not(a < b):  True

#할당 연산자 =
a = 10
b = 20
m = 15

y = a + b
print(y) #30

m += 10
print(m) #25 #15+10

m **= 2
print(m) #625 #25의제곱

m //= 10
print(m) #62 #625를10으로 나눈 몫