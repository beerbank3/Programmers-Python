def solution(nums):
    answer = len(nums) // 2
    list = set(nums)
    if len(nums) // 2 > len(list):
        answer = len(list)
    return answer