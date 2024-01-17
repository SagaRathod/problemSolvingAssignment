ANSWERS:
#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict

#
# Complete the 'mostActive' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY customers as parameter.
#

def mostActive(customers):
    d = defaultdict(int)
    for c in customers:
        d[c] += 1
    return sorted([c for c, cnt in d.items() if cnt / len(customers) >= 0.05])
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    customers_count = int(input().strip())

    customers = []

    for _ in range(customers_count):
        customers_item = input()
        customers.append(customers_item)

    result = mostActive(customers)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()






SubArrays sum in python HackerRank

#!/bin/python3
import math
import os
import random
import re
import sys


#
# Complete the 'findSum' function below.
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY numbers
#  2. 2D_INTEGER_ARRAY queries
#

def findSum(numbers, queries):
    # Write your code here
    tempRes=0
    temp = []
    for b in range(len(queries)):
        for k in range(queries[b][0]-1, queries[b][1]):
            if numbers[k] == 0:
                tempRes = tempRes + queries[b][2]
            tempRes = tempRes + numbers[k]
        temp.append(tempRes)
        tempRes = 0
        

    return temp
    

if __name__ == '__main__':
