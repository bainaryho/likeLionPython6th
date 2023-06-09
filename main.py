class ParentClass:
    def __init__(self):
        self.name = 'parent'
        self.age = 20

    def __str__(self):
        return f'ParentClass name: {self.name}, number : {self.age}'

    def add_num(self, new_number):
        print('부모 : ', new_number, '만큼 더해야지')
        self.age = self.age + new_number


class ChildClass(ParentClass):
    def __init__(self):
        super().__init__() #이걸 꼭 넣어야함. 정의 해줘야지
        self.name = 'child' #그래야 이렇게 변경가능, 기본중의 기본

    def __str__(self):
        return f'ChildClass name : {self.name}, number:{self.age}'

    def add_num(self, new_number):
        print('말 안듣는 자식 : 고정적으로 5 더할건데?')
        self.age = self.age + 5

parent = ParentClass()
child = ChildClass()
print(parent)
print(child)

parent.add_num(7)
child.add_num(7)
print(parent)
print(child)