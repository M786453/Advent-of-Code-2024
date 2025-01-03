"""
Day#: 18
Problem Title: RAM Run
Author: Muhammad Ahtesham Sarwar
"""

from collections import deque

class Solution:

    def __init__(self, filename):
        
        self.corrupted_cords = [(int(line.split(',')[1]), int(line.split(',')[0]),) for line in open(filename,'r').read().split('\n')]

    def generate_map(self, map_bound, bytes_fallen):

        map_ = []

        for i in range(map_bound):

            row = []

            for j in range(map_bound):

                if (i,j,) in self.corrupted_cords[:bytes_fallen]:

                    row.append('#')
                
                else:

                    row.append('.')

            map_.append(row)

        return map_

    def show_map(self, map_):

        for row in map_:

            print("".join(row))
    
    def shortest_path(self, map_, map_bound, start, end):

        # Find shortest path using BFS (Breadth-First Search)

        directions = [(-1,0),(1,0),(0,-1),(0,1)] # Up, Down, Left, Right

        queue = deque([(start[0], start[1], 0)]) # x, y, distance

        visited = set()

        while queue:

            x, y, dist = queue.popleft()

            # Check if destination is reached
            if (x,y) == end:

                return dist
            
            # Explore neighbors
            for dx, dy in directions:

                nx, ny = x + dx, y + dy

                if 0 <= nx < map_bound and 0 <= ny < map_bound and map_[nx][ny] == '.' and (nx,ny) not in visited:

                    queue.append((nx, ny, dist+1))

                    visited.add((nx,ny))
   
        return -1


    def solve_puzzle_1(self, bytes_fallen, map_bound, start, end):

        """
        Find the minimum number of steps needed to reach the exit from starting position.
        """
        
        map_ = self.generate_map(map_bound, bytes_fallen)

        print('Answer Puzzle#1:',self.shortest_path(map_, map_bound, start, end))
    
    def solve_puzzle_2(self, bytes_fallen, map_bound, start, end):

        """
        Find coordinates of the first byte that will prevent the exit from being reachable from starting position.
        """

        map_ = self.generate_map(map_bound, bytes_fallen)

        for cord in self.corrupted_cords[bytes_fallen:]:

            map_[cord[0]][cord[1]] = '#' # Adding fallen byte (corrupted space) in map; it is not walkable

            if self.shortest_path(map_, map_bound, start, end) == -1: # Exit not reachable

                print('Answer Puzzle#2:', f'{cord[1]},{cord[0]}')

                break

if __name__ == "__main__":

    s = Solution(filename='input-day-18.txt')

    s.solve_puzzle_1(bytes_fallen=1024, map_bound=71, start=(0,0), end=(70,70))

    s.solve_puzzle_2(bytes_fallen=1024, map_bound=71, start=(0,0), end=(70,70))