# import array
# stu_roll = array.array('i',[101,102,103,104,105])
#
# for e in stu_roll:
#     print(e)
#
from array import *

# stu_roll = array('i',[101,102,103,104,105])
# n = len(stu_roll)
# i = 0
#
# print('array index 메소드')
# print(stu_roll.index(101)) #0
#
# print('extend() 메소드')
# arr = array('i',[201,208,209])
# stu_roll.extend(arr)
# print(stu_roll)
#
# print('reverse() 메소드')
# stu_roll.reverse()
# print(stu_roll)

# print('sort()')
# stu_roll.sort() #sort가 없다네
# print(stu_roll) #에러

print('slicing')
stu_roll = array('i',[101,102,103,104,105,106,107])
print(stu_roll)
print('0:5',stu_roll[:5])
print('1:5',stu_roll[1:5])
print('-3:',stu_roll[-3:]) #마지막 3개
print('4:',stu_roll[4:]) #4번째부터
print('2:7:2',stu_roll[2:7:2]) #2번째 103부터 2개씩 건너띄며 7번째인덱스 107까지
