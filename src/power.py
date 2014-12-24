def power1(x, n):
    """Compute the value x**n for integer n.
    This function runs in O(n)"""
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)

def power2(x, n):
    """This version runs in O(logn)."""
    if n == 0:
        return 1
    else:
        partial = power(x, n // 2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result