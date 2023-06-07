# #소 -> 대문자
# s = 'hello'
# s1 = 'Hello World!'
# print(s.upper())
# print(s1.lower())
# print(s1.swapcase())
# print(s1.title())
# print(s1.islower())
# print(s1.istitle())
# print(s1.isdigit())
# print(s1.isalpha())

s="Hello, World!"
print(s.replace("world".title(),"there"))
split_s = s.split(',')
print(split_s)
print(''.join(split_s))
#문자열을 나누고 합치는 split 과 join !