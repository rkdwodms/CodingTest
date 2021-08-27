from collections import deque
 
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
 
    while queue:
        x, y = queue.popleft()
        pop_cnt += 1
 
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
 
            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] == 1 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
 
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
 
while True:
    w, h = map(int, input().split())
    if not w and not h:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    cnt = 0
    max_width = []
 
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and visited[i][j] == False:
                bfs(i, j)
                cnt += 1
                max_width.append(pop_cnt)
                
                
    print(cnt)
    print(max(max_width))
