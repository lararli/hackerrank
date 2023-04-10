"""
The function takes a string of brackets and returns 'YES'
if the brackets are balanced, 'NO' otherwise.
The implementation uses a stack to keep track of opening
brackets and compares them to the corresponding closing bracket
as it traverses through the string. If at any point the brackets
do not match, the function returns 'NO'. If the stack is empty at
the end of the traversal, then the brackets are balanced and the
function returns 'YES'.
"""


def is_balanced(s: str) -> str:
    """
    Check if the input string contains balanced brackets.

    Args:
        s: A string of brackets.

    Returns:
        'YES' if the brackets are balanced, 'NO' otherwise.
    """
    stack = []
    bracket = {'{': '}', '(': ')', '[': ']'}

    for char in s:
        if char in ['{', '(', '[']:
            stack.append(char)
        else:
            # if brackets are present
            if stack:
                top = stack.pop()
                if bracket[top] != char:
                    return 'NO'
            # stack is empty
            else:
                return 'NO'

    return 'NO' if stack else 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = is_balanced(s)

        fptr.write(result + '\n')

    fptr.close()
