def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x > 0:
        return int(str(x)[::-1])
    else:
        return -int((str(x)[1:])[::-1])


print(reverse(-123))
