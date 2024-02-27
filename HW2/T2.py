# 2、通话不中断的最短路径给定一个MxN的网格，其中每个单元格都填有数字，数字大小表示覆盖信号强度。灰色网格代表空地,橙色网格代表信号覆盖区域,绿色网格代表基站,绿色网格内数字大小表示该基站发射信号的初始强度。基站信号每向外(上下左右)传播一格,信号强度减1,最小减为0,表示无信号,如下图示。当某个位置可以同时接收到多个基站的信号时,取其中接收信号强度的最大值作为该位置的信号强度。对于给定网格，请判断是否存在一条路径，使得从左上角移动到右下角过程中信号不中断,只能上下左右移动。假设接收到的信号强度低于門限Th,信号就会中断。注意：出发点固定在网格的左上角，终点是网格的右下角。
# 第一行输入信号强度Th。 (1<= Th<=100)第二行输入矩阵M.N. (1<=M<=100, 1<=N<=100)第三行输入基站个数K, (1<=K <= 100)后续K行输入基站位置及初始信号强度。(前两个值表示基站所在行、列索引,第3个值表示基站初始信号强度）
# 输出：返回信号不中断的最短路径,不存在返回0
# 具体可以举一个例子如下：
# 样例1
# 在控制台中输入以下5行：
# 1
# 4 4
# 2
# 0 1 2
# 3 2 3
# 要求输出：6
# 解释如下：1）信号强度门限Th=1；
# 2) M= 4, N=4；
# 3) 4*4网格中一共包含2个基站；
# 4) 2个基站的位置，其中第1个基站在第0行第1列、初始信号强度=2;第2个基站在第3行第2列、初始信号强度=3
# 样例2
# 输入：
# 1
# 5 5
# 5
# 0 1 2
# 0 4 3
# 2 3 2
# 4 0 3
# 4 3 2
#
# 输出：8
#
# 解释:1)信号强度門限Th=1；
# 2) M=5, N=5；
# 3) 5*5网格中一共包含5个基站；
# 4) 5个基站的位置，其中第1个基站在第0行第1列、初始信号强度=2;第2个基站在第0行第4列、初始信号强度=3；第3个基站在第2行第3列、初始信号强度=2；第4个基站在第4行第0列、初始信号强度=3；第5个基站在第4行第3列、初始信号强度=2；
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

