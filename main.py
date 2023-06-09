import os

filename = 'example.txt'

# if os.path.isfile(filename):
#     print(f'{filename}이 존재')
# else:
#     print(f'{filename}이 없음')

file_object = open('list_example.txt','w')
content_list = ['python','java,','c++','javascript']

for i in content_list:
    file_object.write(i + '\n')

file_object.close()