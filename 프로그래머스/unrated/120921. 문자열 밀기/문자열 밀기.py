def solution(A, B):
    if len(A) != len(B):
        return -1

    for i in range(len(A)):
        shifted_A = A[-i:] + A[:-i]
        if shifted_A == B:
            return i

    return -1