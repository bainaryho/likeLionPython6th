# def disp(sh):
#     print(type(sh))
#     print("Disp Function "+sh())
#     #sh() 이거 실화냐? 진짜 몰랐다. 함수에 함수를 넣어버리는..
# def show():
#     return  "Show Func"
#
# disp(show)

def disp():
    def show():
        return "Show Func"
    print('disp')
    return show()
s = disp()
print(s)
#disp
#Show Func



