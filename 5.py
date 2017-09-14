i=1
while i>0:
    age=input('age')
    a=list(range(120))
    a=list(map(str,a))
    if age not in a:
        break
    age=int(age)
    if age < 3:
        print('free')
    elif age >12:
        print('$15')
    else:
        print('$12')
