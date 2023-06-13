def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for i, price in enumerate(prices):
        while stack and price < prices[stack[-1][0]]:
            j = stack.pop()[0]
            answer[j] = i - j
        stack.append((i, price))
    while stack:
        j = stack.pop()[0]
        answer[j] = len(prices) - 1 - j
    return answer
