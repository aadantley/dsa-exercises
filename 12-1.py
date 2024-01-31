def add_until_100(input, memo={}):
    if len(input) == 0:
        return 0
    
    sum_of_remainder = add_until_100(input[1:])
    print(sum_of_remainder)

    if input[0] + sum_of_remainder > 100:
        return sum_of_remainder
    else:
        return input[0] + sum_of_remainder
    

print(add_until_100([1,2,3,4,5,6,7,8,9]))