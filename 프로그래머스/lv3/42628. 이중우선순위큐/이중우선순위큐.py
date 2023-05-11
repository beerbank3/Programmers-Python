def solution(operations):
    answer = [0,0]
    heap = []
    for i in operations:
        if 'I' in i:
            heap.append(int(i.split()[1]))
            heap.sort()
        else:
            if not heap:
                continue
            if '-1' in i.split()[1]:
                heap.pop(0)
            else:
                heap.pop()
    if heap:
        answer[0] = max(heap)
        answer[1] = min(heap)
    return answer