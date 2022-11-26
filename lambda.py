square = lambda x:x*x

result = square(6)
print(result)

numbers = [12, 45, 65, 23, 89]

def double_it(x):
    return x*2

doubled_numbers = map(double_it,numbers)
doubled_numbers2 = map(lambda x : x*2,numbers)
print(numbers)
print(list(doubled_numbers2))