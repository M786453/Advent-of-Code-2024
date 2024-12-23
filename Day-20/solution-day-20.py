"""
Day#: 20
Problem Title: Race Condition
Author: Muhammad Ahtesham Sarwar
"""
from collections import deque

class Soultion:

    def __init__(self, filename):
        
        self.race_track = [list(row) for row in open(filename, 'r').read().split('\n')]

        self.track_bound = len(self.race_track)

        self.race_start, self.race_end = self.find_cords()

    def show_track(self):

        for row in self.race_track:

            print("".join(row))
    
    def find_cords(self):


        """
        Find start and end coordinates of race track.
        """

        cords = []

        for i in range(self.track_bound):

            for j in range(self.track_bound):

                if len(cords) == 2:
                    return cords

                if self.race_track[i][j] == 'S':

                    cords.insert(0,(i,j))
                
                elif self.race_track[i][j] == 'E':

                    cords.append((i,j))
    
    def shortest_duration(self):

        """
        Find shortest duration to reach from start to end position using BFS (Breadth-First Search)

        Each step of race track is equal to one picosecond duration.
        """

        directions = [
                      (-1,0), # UP
                      (1,0),  # DOWN
                      (0,-1), # LEFT
                      (0,1)   # RIGHT
                      ]
        
        queue = deque([(self.race_start[0], self.race_start[1], 0)]) # x,y, distance
        
        visited = set()

        while queue:

            x, y, dist = queue.popleft()

            # Check whether destination is reached
            if (x,y) == self.race_end:

                return dist
            
            # Check neighbors
            for dx, dy in directions:

                nx, ny = x + dx, y + dy

                if 0 <= nx < self.track_bound and 0 <= ny < self.track_bound and (self.race_track[nx][ny] == '.' or self.race_track[nx][ny] == 'E') and (nx,ny) not in visited:

                    queue.append((nx, ny, dist+1))

                    visited.add((nx, ny))

        return -1        

if __name__ == "__main__":

    s = Soultion('example-input-day-20.txt')

    print("Shortest Duration:", s.shortest_duration())
    