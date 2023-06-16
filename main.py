temperatures = [73,74,75,71,69,72,76,73]

answer = [0] * len(temperatures)
stack = [] #인덱스 저장리스트. temperatures의 0인덱스부터 저장함

for i, cur in enumerate(temperatures):
    # cur(밸류)가 temperatures[stack에서 pop된 인덱스] 보다 크면 반복
    while stack and cur > temperatures[stack[-1]]: #stack에서 원소는 그래도 pop할떄는 [-1] 사용
        last = stack.pop() #stack에서 pop된 인덱스
        answer[last] = i - last
    stack.append(i) #stack에 인덱스를 append

print(answer)