# a = [0, 1,2,3,4,5,6,7,8]

# for x in a:
#     print(x)
#     var = 8 - x 
#     if var in a:
#         print(f'var and x makes 8')


a = [0, 1,2,3,4,5,6,7,8]

for x in a:
    var = 8 - x
    if var in a:
        print(f"{x} and {var} make 8")



#   a  would contain n numbers

import random
n = int(input("How many numbers? "))
target = 8
a = [random.randint(0, target) for _ in range(n)]  ## instead of target, if put 100, it will throw error in the next line while doing 8 - 100, 100 generated through the random number
# print(a)

for x in a:
    var = target - x
    if var in a and x <= var:   # chatgpt
        print(f"{x} and {var} make 8")

# when this code will fail, when array size is 1, but i need to return in pair
# always think about edge cases, explainability

