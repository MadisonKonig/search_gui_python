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


    def solve(self):
        queue = list()
        queue.append(self.starting_point)
        visited = set()

        parents = dict()
        parents[self.starting_point] = None

        while queue: 
            v = queue[0]
            if self.grid[v[0]][v[1]] == self.finish_point:
                print("found!")
                break
            queue = queue[1:]
            visited.add(v)
            for u in self.neighbors(v):
                if u not in visited:
                    parents[u] = v
                    queue.append(u)
        
        path = list()
        while v != None:
            path.append(v)
            v = parents[v]

        path.reverse()
        return path
    
    def neighbors(self, v):
        diff = [(0,1), (0,-1), (1,0), (-1,0)]
        retval = list()
        for d in diff:
            newr = d[0] + v[0]
            newc = d[1] + v[1]
            if newr < 0 or newr >= len(self.grid) or newc < 0 or newc >= len(self.grid[0]):
                continue
            # if self.grid[newr][newc] == 'X':
            #     continue
            retval.append((newr, newc))
        return retval

    # def explore_neightbours(self, x, y):
    #     #loop through possible neighbours, up, side, down, side
    #     for i in range(4):
    #         yy = y + self.dy[i]
    #         xx = x + self.dx[i]

    #         #if the neighbour is off the grid, skip
    #         if yy < 0 or xx < 0: continue
    #         if yy >= 10 or xx >= 10: continue

    #         #if the neighbour is already visited, skip
    #         if self.visited[xx][yy]: continue

    #         #add the new neighbour to the list of next neighbours to explore
    #         self.xqueue.append(xx)
    #         self.yqueue.append(yy)
    #         #mark that current neighbour as visited
    #         self.visited[xx][yy] = True
    #         #unsure of this one, but keep track of that neighbour x y
    #         self.prev[self.next_node] = (xx, yy)
    #         # self.prev[self.next_node] = (xx, yy)
    #         #this is marking the square blue for visual purposes
    #         if self.grid[xx][yy] != self.finish_point:
    #             self.square.itemconfig(self.square.find_closest((xx * self.square_size),  (yy * self.square_size)), fill='blue')
    #         #increase the neighbour count
    #         self.nodes_in_next_layer += 1
    #         #increment the recording neighbours index
    #         self.next_node += 1

    # #for those attempting to help me, https://www.youtube.com/watch?v=KiCBXu4P-2Y is the video I based this off of

    # def solve(self):
    #     #row is y, col is x
    #     #mark the first point as being visited
    #     self.visited[self.starting_point[0]][self.starting_point[1]] = True
        
    #     #while there is still nodes to visit
    #     while len(list(self.xqueue)) > 0:
    #         #create two queues, one for x and y
    #         x = self.xqueue.popleft()
    #         y = self.yqueue.popleft()
    #         #if the current x y is the goal, break
    #         if self.grid[x][y] == self.finish_point:
    #             self.reached_end = True
    #             break
    #         self.explore_neightbours(x, y)
    #         #decrease the nodes in the layer to 0 on first loop
    #         self.nodes_left_in_layer -= 1
    #         if self.nodes_left_in_layer == 0:
    #             #change layers to be newly found neighbours
    #             self.nodes_left_in_layer = self.nodes_in_next_layer
    #             #put neighbours back to 0 for next loop
    #             self.nodes_in_next_layer = 0
    #             #increase the amount of steps needed for shortest path
    #             self.move_count += 1
    #     if self.reached_end:
    #         tmp = [h for h in self.prev if h]
    #         print(tmp)
    #         return self.move_count
    #     return -1