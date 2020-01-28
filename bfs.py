class Bfs:

    def __init__(self, starting_point, finish_point, grid, square, square_size):
        super().__init__()
        self.starting_point = starting_point
        self.finish_point = finish_point
        self.grid = grid
        self.square = square
        self.square_size = square_size

    def solve(self):
        tmp1 = ['2,3', '2,4', '2,5']
        for x in range(len(tmp1)):
            tmp = tmp1[x].split(',')
            self.square.itemconfig(self.square.find_closest((int(tmp[0]) * self.square_size), (int(tmp[1]) * self.square_size)), fill='pink')