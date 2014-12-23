def disjoint1(A, B, C):
    """Return True is there is no element common
    to all three lists.

    O(n3) running time...not good"""
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False
    return True

def disjoint2(A, B, C):
    """O(n2) worst case running time -
    large improvement"""
    for a in A:
        for b in B:
            if a == b:
                for c in C:
                    if a == c
                    return False
    return True