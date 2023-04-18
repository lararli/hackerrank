"""
This code defines a function called pairs that takes
two arguments: an integer k and a list of integers arr.
The function returns the number of pairs of integers in
arr whose difference is k.

The function first converts the arr list to a set to remove any
duplicates and improve lookup times. Then, it initializes a variable
count to 0 to keep track of the number of pairs whose difference is k.

Next, the function iterates over each element i in the set. For each i,
it checks whether i+k is also in the set. If it is, that means there is a
pair of integers in arr whose difference is k, and the function increments
the count variable.

Finally, the function returns the count variable as the number of pairs of integers
in arr whose difference is k.
"""

import os


def pairs(difference: int, list_arr: list):
    """Returns the number of pairs in `arr` whose difference is `k`.

    Args:
        difference (int): The difference to look for.
        list_arr (list): The list of integers to search.

    Returns:
        int: The number of pairs whose difference is `k`.
    """
    list_arr = set(list_arr)
    count = 0
    for i in list_arr:
        if i + difference in list_arr:
            count += 1
    return count

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w', encoding='utf-8') as fptr:
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        arr = list(map(int, input().rstrip().split()))

        result = pairs(k, arr)  # pylint: disable=invalid-name

        fptr.write(str(result) + '\n')