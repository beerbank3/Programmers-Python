def solution(date1, date2):
    # date1과 date2의 각 부분(year, month, day)을 추출합니다.
    year1, month1, day1 = date1
    year2, month2, day2 = date2
    
    # year1이 year2보다 작으면 date1은 date2보다 앞섭니다.
    if year1 < year2:
        return 1
    # year1이 year2와 같으면 month1을 비교합니다.
    elif year1 == year2:
        if month1 < month2:
            return 1
        # month1도 같다면 day1을 비교합니다.
        elif month1 == month2 and day1 < day2:
            return 1
    
    # 위의 모든 조건을 만족하지 않으면 date1은 date2보다 앞서지 않습니다.
    return 0