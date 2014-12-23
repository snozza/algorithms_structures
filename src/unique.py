def unique1(S):
    """simple iterative algorithm, Return True if
    there are no duplicate elements in sequence S.
    runs in O(n2)"""
    for j in range(len(S)):
        for k in range(j+1, len(S)):
            if S[j] == S[k]:
                return False
    return True

def unique2(S):
    """use sorting algorithm to achieve O(nlogn)"""
    temp = sorted(S)
    for j in range(1, len(temp)):
        if S[j-1] == S[j]:
            return
    return True