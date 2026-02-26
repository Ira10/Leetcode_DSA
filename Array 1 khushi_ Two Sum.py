##### 25th Feb    ### visit again

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict_ = {index: value for index, value in enumerate(nums)}  ## storing the array as dict in key value pair
        # print(result)

        for integer in nums:
            # print(integer)
            # first_int_key_in_dict = k for k, v in dict_.items() if v == integer
            first_int_key_in_dict = next(k for k, v in dict_.items() if v == integer)
            result = target - integer
            if result in nums:
                result_key = next((k for k, v in dict_.items() if v == result and k != first_int_key_in_dict), None)
                if result_key is not None:
                    return [first_int_key_in_dict, result_key]
                # final = [first_int_key_in_dict, result_key]
                # # final = [key for key, value in dict_.items() if value in [integer, result] and first_int_key_in_dict != ]
                # return final 




    # result_key = next(k for k, v in dict_.items() if v == result and k != first_int_key_in_dict)
    # final = [first_int_key_in_dict, result_key]
    # return final

                ## 25 mins gone, need new logic, because 3 is already there , it is taking this. 
                ## Edge case thinking gotta build okay!!!




  # for index, value in enumerate(nums):
        #     print(index, value)

        






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




