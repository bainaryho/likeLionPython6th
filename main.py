a = ['a1','b2','c3']
for i in range(len(a)):
    print(i,a[i])

i = 0
p_list = []
for n in a:
    p_list.append([i,n])
    i += 1
print(p_list)

for i,v in enumerate(a):
    print(i,v)