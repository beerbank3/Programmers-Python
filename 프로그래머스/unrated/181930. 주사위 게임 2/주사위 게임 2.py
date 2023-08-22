def solution(a, b, c):
    if a == b == c:  # 모두 같은 숫자인 경우
        return (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    elif a == b or a == c or b == c:  # 두 숫자가 같은 경우
        return (a + b + c) * (a**2 + b**2 + c**2)
    else:  # 모두 다른 숫자인 경우
        return a + b + c