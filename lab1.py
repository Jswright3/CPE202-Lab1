"""LAB1
CPE202
"""

#1
def get_max(arr):
    """finds the maximum in a list of integers, if arr is empty returns None
    Args:
        arr (list): list of integers
    Returns:
        (int): high integer in arr
    """
    high = 0
    if len(arr) == 0:
        return None
    for i in arr:
        if i > high:
            high = i
    return high



#2
def reverse(chars):
    """uses recursion to reverse a string
    Args:
        chars (str): string of characters to reverse
    Returns:
        (str): reversed string
    """
    length = len(chars)
    if length == 0:
        return ''
    return "{}{}".format(chars[length-1], reverse(chars[:-1]))


#3
def search(arr, target):
    """uses helper function to complete binary search to find target integer in list
    Args:
        arr (list): list of integers
        target (int): target integer
    Returns:
        (int): index of target integer
    """
    if len(arr) == 0:
        return None
    return helper(arr, target, 0, len(arr)-1)


#4
def fib(num):
    """computes the n th Fibonacci number
    Args:
        num (int): desired n for Fibonacci number (n)
    Returns:
        (int): nth Fibonacci number
    """
    if num in (0, 1):
        return num
    return fib(num - 2) + fib(num - 1)

#5.1 factorial iterative version
def factorial_iter(num):
    """computes a factorial number n! iteratively
    Args:
        num (int): integer to solve factorial of (n)
    Returns:
        (int): factorial of n
    """
    # to-do: write the function body.
    factorial = 1
    if num == 0:
        return 1
    for i in range(1, num+1):
        factorial *= i
    return factorial

#5.2 factorial recursive version
def factorial_rec(num):
    """computes a factorial number n! recursively
    Args:
        num (int): integer to solve factorial of (n)
    Returns:
        (int): factorial of n
    """
    if num in (0, 1):
        return 1
    return factorial_rec(num - 1) * num


def helper(arr, target, low, high):
    """binary search list for target integer
    Args:
        arr (list): list of integers
        target (int): target integer
        low (int): low index
        high (int): high index
    Returns:
        (int): index of target integer
    """
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == target:
            return mid
        if target < arr[mid]:
            return helper(arr, target, low, mid - 1)
        return helper(arr, target, mid + 1, high)
    return None
