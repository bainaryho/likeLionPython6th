# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         mapping = {
#             ')': '(',
#             '}': '{',
#             ']': '['
#         }
#
#         for char in s:
#             # 스택 마지막 요소 꺼내서 확인, 비어있으면 #반환
#             if char in mapping:
#                 top_element = stack.pop() if stack else '#'
#
#             else:
#                 stack.append(char)
#
#         return not stack

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence = {c: i for i, c in enumerate(s)}
        stack = []
        in_stack = set()

        for i, c in enumerate(s):
            if c not in in_stack:
                while stack and c < stack[-i] and i < last_occurrence[stack[-1]]:
                    in_stack.remove(stack.pop())
                stack.append(c)
                in_stack.add(c)

        return ''.join()