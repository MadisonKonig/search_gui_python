import collections
import time

class Bfs:

    def __init__(self, starting_point, finish_point, grid, square, square_size):
        super().__init__()
        self.starting_point = starting_point
        self.finish_point = finish_point
        self.grid = grid
        self.square = square
        self.square_size = square_size
        self.reached_end = False
        self.dx = [0, 0, 1, -1]
        self.dy = [-1, 1, 0, 0]
        self.nodes_left_in_layer = 1
        self.nodes_in_next_layer = 0
        self.move_count = 0
        self.visited = [[False for x in range(10)] for y in range(10)]
        self.xqueue = collections.deque([self.starting_point[0]])
        self.yqueue = collections.deque([self.starting_point[1]])
        self.prev = [None for nu in range(100)]
        self.next_node = 0

    def explore_neightbours(self, x, y):
        for i in range(4):
            yy = y + self.dy[i]
            xx = x + self.dx[i]

            if yy < 0 or xx < 0: continue
            if yy >= 10 or xx >= 10: continue

            if self.visited[xx][yy]: continue

            self.xqueue.append(xx)
            self.yqueue.append(yy)
            self.visited[xx][yy] = True
            # self.prev[self.move_count] = (x, y)
            # self.prev[self.move_count] = (xx, yy)
            if self.grid[xx][yy] != self.finish_point:
                self.square.itemconfig(self.square.find_closest((xx * self.square_size),  (yy * self.square_size)), fill='blue')
            self.nodes_in_next_layer += 1
            # self.next_node += 1

    def solve(self):
        #row is y, col is x
        self.visited[self.starting_point[0]][self.starting_point[1]] = True
        # print(f'{self.grid[self.xqueue.popleft()][self.yqueue.popleft()]}, {self.finish_point}')
        
        while len(list(self.xqueue)) > 0:
            print(len(list(self.xqueue)))
            x = self.xqueue.popleft()
            y = self.yqueue.popleft()
            if self.grid[x][y] == self.finish_point:
                self.reached_end = True
                break
            self.explore_neightbours(x, y)
            self.nodes_left_in_layer -= 1
            if self.nodes_left_in_layer == 0:
                self.nodes_left_in_layer = self.nodes_in_next_layer
                self.nodes_in_next_layer = 0
                self.move_count += 1
        if self.reached_end:
            # print(self.prev)
            return self.move_count
        return -1