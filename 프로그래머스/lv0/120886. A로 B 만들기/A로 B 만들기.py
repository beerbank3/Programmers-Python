def solution(before, after):
    # 문자열을 정렬하여 알파벳 순서를 비교하기 위해 리스트로 변환합니다.
    before_list = list(before)
    after_list = list(after)

    # 정렬된 리스트를 비교하여 같으면 1을 반환, 다르면 0을 반환합니다.
    before_list.sort()
    after_list.sort()

    if before_list == after_list:
        return 1
    else:
        return 0