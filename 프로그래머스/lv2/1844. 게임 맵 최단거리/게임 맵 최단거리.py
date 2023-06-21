from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque()
    queue.append((0, 0, 1))
    maps[0][0] = 0

    while queue:
        x, y, distance = queue.popleft()

        if x == n - 1 and y == m - 1:
            return distance

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                queue.append((nx, ny, distance + 1))
                maps[nx][ny] = 0

    return -1
