#암시적 타입 변환
a = 5
b = 2
value = a/b
print(value) #2.5
print(type(value)) #<class 'float'>
j = 'Hello'
k = 'like lion'
value = j+k
print(value) #Hellolike lion
print(type(value)) #<class 'str'>
# u = 10
# q = '20'
# print(u+q) #error!

#명시적 타입 변환
q = 20
u = '10'
r = q + int(u)
print(r, type(r)) #30 <class 'int'>

n1 = 10.36
vn1 = int(n1)
print(vn1, type(vn1)) #10 <class 'int'>

n1 = 10
vn1 = complex(n1)
print(vn1, type(vn1)) #(10+0j) <class 'complex'>

#튜플
n5 = '멋쟁이 사자'
vn5 = tuple(n5)
print(vn5, type(vn5)) #('멋', '쟁', '이', ' ', '사', '자') <class 'tuple'>

n6 = 'kim', 'lee', 'park', 'bae'
vn6 = list(n6)
print(n6) #('kim', 'lee', 'park', 'bae')
print(vn6) #['kim', 'lee', 'park', 'bae']