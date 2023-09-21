def solution(myString, pat):
    count = 0
    start = 0

    while start < len(myString):
        index = myString.find(pat, start)  # 패턴을 찾는다

        if index == -1:
            break  # 패턴을 더 이상 찾을 수 없으면 종료

        count += 1
        start = index + 1  # 다음 탐색을 위해 시작 위치를 조정

    return count