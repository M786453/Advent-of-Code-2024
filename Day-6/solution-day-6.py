"""
Day#: 6
Problem Title: Guard Gallivant
Author: Muhammad Ahtesham Sarwar
"""

class Solution:

    def __init__(self, filename):

        self.map = self.read_input(filename=filename)

        self.map_max_rows = len(self.map)

        self.map_max_cols = len(self.map[0])

        self.guard_movement_dict = {
                '^': [(-1,0), '>'],
                'v': [(1,0), '<'],
                '>': [(0,1), 'v'],
                '<': [(0,-1), '^']
            }

    def read_input(self,filename):

        data = ""

        try:
            
            with open(filename, 'r') as f:

                data = f.read().split('\n')

                data = [list(row) for row in data]

        except Exception as e:

            print("Error in read_input():", e)

        return data
    
    def find_guard_cords(self):

        guard_coordinates = []

        try:
            
            for i in range(len(self.map)):

                row = self.map[i]

                if '^' in row:

                    guard_coordinates.append(i)

                    guard_coordinates.append(row.index('^'))

        except Exception as e:

            print("Error in find_guard_position:", e)

        return guard_coordinates
    
    def guard_movement(self, guard_standpoint, guard_row_index, guard_col_index):

        """
        Visit different positions of map until moved out of map.
        """

        guard_visited_distinct_positions = set()

        try:
            
            while True:
                    
                if (guard_standpoint == '^' and guard_row_index-1 >= 0) or \
                    (guard_standpoint == 'v' and guard_row_index+1 < self.map_max_rows) or \
                        (guard_standpoint == '>' and guard_col_index+1 < self.map_max_cols) or \
                            (guard_standpoint == '<' and guard_col_index-1 >= 0):

                    tmp_row_index = guard_row_index + self.guard_movement_dict[guard_standpoint][0][0]

                    tmp_col_index = guard_col_index + self.guard_movement_dict[guard_standpoint][0][1]

                    if self.map[tmp_row_index][tmp_col_index] == '#': # Obstacle, turn right
                        
                        self.map[guard_row_index][guard_col_index] = self.guard_movement_dict[guard_standpoint][1] # Guard new standpoint

                        guard_standpoint = self.guard_movement_dict[guard_standpoint][1] # Guard new standpoint

                        # guard_engaged_obtacles.append([(tmp_row_index, tmp_col_index), guard_standpoint])

                    else:

                        self.map[guard_row_index][guard_col_index] = 'X' # Footprint

                        guard_row_index = tmp_row_index

                        guard_col_index = tmp_col_index

                        self.map[guard_row_index][guard_col_index] = guard_standpoint # No obstacle, move forward

                        guard_visited_distinct_positions.add(f'{guard_row_index}i{guard_col_index}j')

                else:

                    guard_visited_distinct_positions.add(f'{guard_row_index}i{guard_col_index}j')

                    self.map[guard_row_index][guard_col_index] = 'X' # Footprint
                    
                    break # Guard moves out of map

        except Exception as e:

            print("Error in guard_movement():", e)

        return guard_visited_distinct_positions
    
    def solve_puzzle_1(self):

        """
        Find total number of distinct positions visited by guard.
        """

        total_visited_distinct_postions = 0

        # guard_engaged_obtacles = [] # format of sublist: [cordinates, guard_future_standpoint], coordinates in tuple form: (i,j), e.g, [(1,3), '^']

        try:

            guard_row_index, guard_col_index = self.find_guard_cords()

            guard_initial_standpoint = '^' # Starting standpoint of Guard

            total_visited_distinct_postions = len(self.guard_movement(guard_initial_standpoint, guard_row_index, guard_col_index))

        except Exception as e:

            print("Error in solve_puzzle_1():", e)

        return total_visited_distinct_postions
    
    def solve_puzzle_2(self, visited_positions, engaged_obstacles):

        """
        Find total number of possible loop obstructions to make the guard move in a loop.
        """

        pass

if __name__ == "__main__":

    s = Solution('input-day-6.txt')

    answer_puzzle_1 = s.solve_puzzle_1()

    print("Answer of Puzzle#1:", answer_puzzle_1)

    # answer_puzzle_2 = s.solve_puzzle_2(guard_visited_distinct_positions, guard_engaged_obtacles)

    # print("Answer of Puzzle#2:", answer_puzzle_2)