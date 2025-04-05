#!/bin/python3

import os

#
# Complete the 'longestIncreasingSubsequence' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def longestIncreasingSubsequence(arr):
    sequence = []

    def place_in_sequence(value):
        size = len(sequence)

        if size < 1:
            sequence.append(value)
            return

        backward = size - 1

        if value == sequence[backward]:
            return

        if value > sequence[backward]:
            sequence.append(value)
            return

        while backward > 0:
            if value == sequence[backward - 1]:
                return
                
            if value > sequence[backward - 1]:
                backward = backward - 1
            else:
                break

        sequence.insert(backward, value)

    length = len(arr)

    if length == 0:
        return 0


    while index < length:
        place_in_sequence(arr[index])
        index = index + 1

    print(f'sequence is: {sequence}')
    return len(sequence)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = longestIncreasingSubsequence(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
