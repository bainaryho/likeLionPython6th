# #제너레이터 실습
# def fibonacci_generator(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a+b
#
# fibonacci_sequence = fibonacci_generator(10)
#
# for number in fibonacci_sequence:
#     print(number)

# def yield_abc():
#   yield "A"
#   yield "B"
#   yield "C"
#
# for ch in yield_abc():
#   print(ch)

def generate_alphabat(sl, el):
    start = ord(sl)
    end = ord(el)
    while start <= end:
        yield chr(start)
        start += 1

runner = generate_alphabat('A','G')
print(type(runner))
for l in runner:
    print(l)