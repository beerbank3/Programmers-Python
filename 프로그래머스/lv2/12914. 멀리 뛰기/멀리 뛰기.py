def solution(n):
    if n <= 2:
        return n

    answer = [0] * (n + 1)  # 메모이제이션을 위한 배열 초기화
    answer[1] = 1
    answer[2] = 2

    for i in range(3, n+1):
        answer[i] = (answer[i-1] + answer[i-2]) % 1234567

    return answer[n]