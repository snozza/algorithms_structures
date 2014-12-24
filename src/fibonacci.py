def bad_fibonacci(n):
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n-2) + bad_fibonacci(n-1)

def good_fibonacci(n):
    """much more efficient to avoid huge number of 
    recursive calls"""
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = good_fibonacci(n-1)
        return (a+b, a)