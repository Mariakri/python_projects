def number_pattern(n):
    numbers = []
    for i in range(1,n+1):
        numbers.append(str(i))
    if not isinstance (n,int) or isinstance (n,bool):
        return 'Argument must be an integer value.'
    if (n < 0):
        return 'Argument must be an integer greater than 0.'

    return  ' '.join(numbers)

print(number_pattern(4))
print(number_pattern(12))