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
  
        self.directions = [
                      (-1,0), # UP
                      (1,0),  # DOWN
                      (0,-1), # LEFT
                      (0,1)   # RIGHT
                      ]

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
        
        queue = deque([(self.race_start[0], self.race_start[1], 0)]) # x,y, duration
        
        visited = list()

        while queue:

            x, y, duration = queue.popleft()

            # Check whether destination is reached
            if (x,y) == self.race_end:

                return visited, duration
            
            # Check neighbors
            for dx, dy in self.directions:

                nx, ny = x + dx, y + dy

                if 0 <= nx < self.track_bound and 0 <= ny < self.track_bound and (self.race_track[nx][ny] == '.' or self.race_track[nx][ny] == 'E') and (nx,ny) not in visited:

                    queue.append((nx, ny, duration+1))

                    visited.append((nx, ny))

        return [],-1

    def race_condition(self):

        """
        Race condition allows cheat once in a race by disabling collision with wall for 2 steps (picoseconds).
        """

        duration_cheat_map = {} # {"picoseconds": [[cheat_step_1, cheat_step_2]]}

        original_shortest_path, original_shortest_duration = self.shortest_duration() # coordinates list, duration (picoseconds)

        original_shortest_path.pop() # Remove 'End' cords from path

        # Apply cheat on every obstacle adjacent to every cords of origina_shortest_path 
        for i in range(len(original_shortest_path)):            

            duration = i+2

            x,y = original_shortest_path[i]

            for dx, dy in self.directions:

                nx, ny = x + dx, y + dy

                # Check for obstacle
                if 0 <= nx < self.track_bound and 0 <= ny < self.track_bound and self.race_track[nx][ny] == '#':

                    self.race_start = (nx,ny)

                    shortest_path, shortest_duration = self.shortest_duration()

                    shortest_duration += duration

                    saved_duration = original_shortest_duration - shortest_duration

                    if saved_duration in duration_cheat_map:
                        duration_cheat_map[saved_duration].append(shortest_path[:2])
                    else:
                        duration_cheat_map[saved_duration] = [shortest_path[:2]]
    
        for d in duration_cheat_map:

            print(len(duration_cheat_map[d]), d)

if __name__ == "__main__":

    s = Soultion('input-day-20.txt')

    s.race_condition()

    
   
