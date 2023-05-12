def solution(n):
    num = [0, 1]
    for i in range(1,n):
        num.append(num[i-1]+num[i])
    return (num[n-2] + num[n-1])  % 1234567