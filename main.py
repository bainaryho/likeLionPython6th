# import array
# stu_roll = array.array('i',[101,102,103,104,105])
#
# for e in stu_roll:
#     print(e)
#
from array import *

stu_roll = array('i',[101,102,103,104,105])
n = len(stu_roll)
i = 0
while i < n :
    print(stu_roll[i])
    i += 1

print('Array After Insert')
stu_roll.insert(1, 106)
stu_roll.insert(3, 107)
n = len(stu_roll)
i = 0
while i < n :
    print(stu_roll[i])
    i += 1


print('요소삭제')
stu_roll.remove(101)
n = len(stu_roll)
i = 0
while i < n :
    print(stu_roll[i])
    i += 1

print('배열 pop() 실습')
element = stu_roll.pop()
n = len(stu_roll)
i = 0
print('pop data : ',element)
while i < n :
    print(stu_roll[i])
    i += 1

