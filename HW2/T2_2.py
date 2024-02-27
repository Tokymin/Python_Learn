
from queue import PriorityQueue

def shortest_path(Th, M, N, K, stations):
    grid = [[0]*N for _ in range(M)]
    for x, y, strength in stations:
        update_grid(grid, x, y, strength)
    if grid[0][0] < Th or grid[M-1][N-1] < Th:
        return 0
    return bfs(grid, Th)

def update_grid(grid, x, y, strength):
    for i in range(max(0, x-strength), min(len(grid), x+strength+1)):
        for j in range(max(0, y-strength), min(len(grid[0]), y+strength+1)):
            dist = abs(x-i) + abs(y-j)
            if dist <= strength:
                grid[i][j] = max(grid[i][j], strength-dist)

def bfs(grid, Th):
    M, N = len(grid), len(grid[0])
    visited = [[False]*N for _ in range(M)]
    q = PriorityQueue()
    q.put((0, 0, 0))
    while not q.empty():
        dist, x, y = q.get()
        if x == M-1 and y == N-1:
            return dist
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] >= Th:
                visited[nx][ny] = True
                q.put((dist+1, nx, ny))
    return 0



if __name__ == '__main__':
    Th = int(input())
    # 读取网格尺寸 M 和 N
    M, N = map(int, input().split())
    # 读取基站个数 K
    K = int(input())
    # 读取基站位置和初始信号强度
    base_stations = []
    for _ in range(K):
        x, y, strength = map(int, input().split())
        base_stations.append((x, y, strength))
print(shortest_path(Th, M, N, K, base_stations))