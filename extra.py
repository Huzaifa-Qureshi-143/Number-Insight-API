from number import Number

numbers = [153, 370, 371, 407, 9474]

for i in numbers:
    obj = Number(i)
    if obj.is_armstrong() ==  False:
        print('Test failed')
        break