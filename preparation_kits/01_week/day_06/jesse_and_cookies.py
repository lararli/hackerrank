"""
The code is an implementation of the HackerRank challenge "Jesse and Cookies".
The challenge is about using a priority queue to solve the problem of mixing two cookies.

The "cookies" function receives two parameters: an integer "k" representing
the minimum sweetness value required to be acceptable, and an integer array "A"
containing the initial sweetness values of the cookies.

The algorithm starts by sorting the array of cookies in reverse order,
in order to facilitate the search for cookies with the lowest sweetness values.

The "count" variable is initialized to zero, and it will be used to count
the number of operations necessary to mix two cookies with a sweetness
value greater than or equal to "k".

The "temp" list is initialized to an empty list, and it will be used
to store the result of the mixing operations.

The "l" variable is initialized to zero, and it will be used to keep
track of the index of the last cookie in the "temp" list that was used in the mixing operation.

The algorithm runs a while loop, which will continue as long as the
conditions specified in the loop header are met.

Inside the loop, the algorithm checks whether the last cookie in the
"A" array or the last cookie in the "temp" list is greater than or
equal to "k". If neither condition is met, the algorithm exits the loop.

If at least one of the conditions is met, the algorithm proceeds to
check whether there are enough cookies to perform the mixing operation.
If there are not enough cookies, the "count" variable is set to -1, and the algorithm
exits the loop.

If there are enough cookies, the "count" variable is incremented, and
two lists are created: "a0" and "a1". "a0" is populated with the two
cookies with the highest sweetness value in the "A" array, while "a1"
is populated with the two cookies with the highest sweetness value in the
"temp" list. The two lists are then concatenated and sorted based on their
sweetness value. The two cookies with the lowest sweetness value are selected,
and their indexes are used to remove them from either the "A" array or the "temp" list,
depending on their origin.

The two cookies are then mixed, and their result is added to the "temp" list.
The "l" variable is incremented to reflect the fact that a new cookie has been
added to the list.

Once the loop finishes, the "count" variable is returned, indicating the number
of operations required to mix two cookies with a sweetness value greater than
or equal to "k".
"""
import os
from typing import List


def cookies(k: int, A: List[int]) -> int:
    """
    Calculates the minimum number of times cookies should be combined to make
    a sweetness greater than or equal to the required minimum sweetness k.

    :param k: The minimum sweetness required.
    :type k: int
    :param A: An array of integers representing the sweetness of each cookie.
    :type A: List[int]
    :return: The minimum number of times cookies should be combined to make a sweetness
        greater than or equal to the required minimum sweetness k.
    :rtype: int
    """
    A = sorted(A, reverse=True)
    count = 0
    temp = []
    l = 0

    # While there is at least one cookie in A with sweetness less than k,
    # and temp array contains at least one cookie with sweetness less than k,
    # we continue to combine the cookies.
    while A and A[-1] < k or temp and temp[l] < k:
        if len(A) + len(temp[l:l + 2]) < 2:
            count = -1  # If there are not enough cookies to combine, set count to -1.
            break
        else:
            count += 1
            # We create two arrays to contain the two least sweet cookies to be combined.
            # a0 contains the least sweet cookies in A and a1 contains the least sweet cookies in temp.
            a0 = []
            for num, i in enumerate(range(min(2, len(A)))):
                a0.append((A[-num - 1], 0))
            a1 = []
            tmp = temp[l:l + 2]
            for num, i in enumerate(range(min(2, len(tmp)))):
                a1.append((tmp[num], 1))
            # We combine the two least sweet cookies from a0 and a1 to make a new cookie with sweetness
            # equal to the sum of the two least sweet cookies.
            # We pop the two least sweet cookies from their respective arrays.
            b = sorted(a0 + a1, key=lambda x: x[0])[:2]
            for i in range(2):
                if b[i][1] == 0:
                    A.pop()
                else:
                    l += 1
            temp.append(b[0][0] + b[1][0] * 2)
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
