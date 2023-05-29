import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    mix_count = 0
    
    while scoville[0] < K:
        
        if len(scoville) == 1:
            return -1
        
        mix = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        
        heapq.heappush(scoville, mix)
        
        mix_count += 1
    
    return mix_count