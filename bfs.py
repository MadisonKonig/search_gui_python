import collections

class Bfs:

    def __init__(self, starting_point, finish_point, grid, square, square_size):
        super().__init__()
        self.starting_point = starting_point
        self.finish_point = finish_point
        self.grid = grid
        self.square = square
        self.square_size = square_size

    def solve(self):

        current_coordx, current_coordy = self.starting_point[0], self.starting_point[1]
        print(f'{current_coordx} & {current_coordy}')

        # queue = collections.deque([self.starting_point])
        
        # seen = set([self.starting_point[0]])
        # path = queue.popleft()
        # print(queue)
        # while queue:
        #     path = queue.popleft()
        #     x, y = path[-1]
        #     if self.grid[x][y] == self.finish_point:
        #         print("found it!" + path)
        #         return 0
        #     for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
        #         if 0 <= x2 < 10 and 0 <= y2 < 10 and (x2, y2) not in seen:
        #             queue.append(path + [(x2,y2)])
        #             seen.add((x2,y2))


        
        # for x in range(len(self.grid[0])):
        #     print(self.grid[x])
        # print(self.grid)
        # tmp1 = ['2,3', '2,4', '2,5']
        # for x in range(len(tmp1)):
        #     tmp = tmp1[x].split(',')
        #     self.square.itemconfig(self.square.find_closest((int(tmp[0]) * self.square_size), (int(tmp[1]) * self.square_size)), fill='pink')