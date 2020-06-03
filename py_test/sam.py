# import time
import math
# start = time.time()

def nearest_square(num):
    if num < 0:
        return 0
    else:
        lower_sqrt_num = (int(math.floor(math.sqrt(num))))**2
        high_sqrt_num = (int(math.ceil(math.sqrt(num))))**2
    
        difference = {lower_sqrt_num : num-lower_sqrt_num, high_sqrt_num : high_sqrt_num-num}

        min_key = min(difference,key=difference.get)
    
        return min_key

# if __name__ == "__main__":
#     print(nearest_square(25))

# print('Duration: {} seconds'.format(time.time() - start))