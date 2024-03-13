#Lambda function

def squared(num):
    return num * num
print(squared(3))


sum = lambda a,b : a + b

print(sum(2,2))



###############

def funcBuilder(x):
    return lambda num : num + x
addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))



#################



numbers = [3,7,12,18,20,21]

square_nums = map(lambda num : num * num,numbers)

print(list(square_nums))


###################

odd_nums = filter(lambda num : num % 2 !=0,numbers)

print(list(odd_nums))


###################

from functools import reduce



numbers = [1,2,3,4,5,1]

total = reduce(lambda acc,curr: acc + curr,numbers)

print(total)
