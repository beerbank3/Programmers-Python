def solution(arr, intervals):
    # 첫 번째 구간과 두 번째 구간 추출
    first_interval = arr[intervals[0][0]:intervals[0][1] + 1]
    second_interval = arr[intervals[1][0]:intervals[1][1] + 1]
    
    # 두 구간을 앞뒤로 붙인 새로운 배열 생성
    new_array = first_interval + second_interval
    
    # 새로운 배열 반환
    return new_array