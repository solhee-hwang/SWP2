number = ['one', 'two', 'three', 'four']
for i in number:
    if i == 'one':
        continue
    elif i == 'three':
        break
    print("number is", i)