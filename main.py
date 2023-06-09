class Mobile:
    fp = 'yes'

realme = Mobile()
redme = Mobile()
geek = Mobile()

print(Mobile.fp)
print(redme.fp)
print(realme.fp)

Mobile.fp = 'no' #클래스 변수에 직접 접근 가능
print(Mobile.fp)
print(redme.fp) #클래스로 생성된 객체들도 변경됨
print('----------------')
realme.fp = 'not work'
print(Mobile.fp)
print(redme.fp)
print(realme.fp)
print(type(realme))