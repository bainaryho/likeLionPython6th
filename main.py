class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            # 스택 마지막 요소 꺼내서 확인, 비어있으면 #반환
            if char in mapping:
                top_element = stack.pop() if stack else '#'

            else:
                stack.append(char)

        return not stack