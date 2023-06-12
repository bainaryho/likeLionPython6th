def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division to zero")
    else:
        print(f'result : {result}')
    finally:
        print('well done')

# divide(10,0)
# #Error: Division to zero
# #well done
# divide(5,6)
# #result : 0.8333333333333334
# #well done
try:
    number = int('not a num') #v Error
    number = 5 + 'not a num' #t Error
except ValueError:
    print("v Error")
except TypeError:
    print("t Error")
