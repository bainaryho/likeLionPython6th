#멤버 in 연산자
st1 = "Welcome to 멋쟁이 사자"
print("to" in st1) #True

st2 = "Welcome top 멋쟁이 사자"
print("to" in st2) #True

st3 = "Welcome top 멋쟁이 사자"
print("et" in st3) #False

#is 연산자
a = 10
b = 10
print(a is b) #True
c = 10.0
print(a is c) #False
d = 10.0
print(c is d) #True