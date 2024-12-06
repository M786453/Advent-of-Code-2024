"""
Day#: 6
Problem Title: Guard Gallivant
Author: Muhammad Ahtesham Sarwar
"""
import re

class Solution:

    def __init__(self, filename):

        self.map = self.read_input(filename=filename)

        print(len(self.map))

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
    
    def solve_puzzle_1(self):

        guard_visited_distinct_positions = set()

        guard_engaged_obtacles = [] # format of sublist: [cordinates, guard_future_standpoint], coordinates in tuple form: (i,j), e.g, [(1,3), '^']

        try:

            max_rows = len(self.map)

            max_cols = len(self.map[0])

            guard_standpoint = '^'
            
            guard_row_index, guard_col_index = self.find_guard_cords()

            while True:

                if guard_standpoint == '^':
                    
                    if guard_row_index-1 >= 0:

                        if self.map[guard_row_index-1][guard_col_index] == '#': # Obstacle, turn right
                            
                            self.map[guard_row_index][guard_col_index] = '>'

                            guard_standpoint = '>'

                            guard_engaged_obtacles.append([(guard_row_index-1, guard_col_index), guard_standpoint])

                        else:

                            self.map[guard_row_index][guard_col_index] = 'X' # Footprint

                            guard_row_index -= 1

                            self.map[guard_row_index][guard_col_index] = '^' # No obstacle, move forward

                            guard_visited_distinct_positions.add(f'{guard_row_index}i{guard_col_index}j')

                    else:

                        guard_visited_distinct_positions.add(f'{guard_row_index}i{guard_col_index}j')

                        self.map[guard_row_index][guard_col_index] = 'X' # Footprint
                        
                        break # Guard moves out of map

                elif guard_standpoint == '>':

                    if guard_col_index+1 < max_cols:

                        if self.map[guard_row_index][guard_col_index+1] == '#': # Obstacle, turn right
                            
                            self.map[guard_row_index][guard_col_index] = 'v'

                            guard_standpoint = 'v'

                            guard_engaged_obtacles.append([(guard_row_index, guard_col_index+1), guard_standpoint])

                        else:

                            self.map[guard_row_index][guard_col_index] = 'X' # Footprint

                            guard_col_index += 1

                            self.map[guard_row_index][guard_col_index] = '>' # No obstacle, move forward

                            guard_visited_distinct_positions.add(f'{guard_row_index}i{guard_col_index}j')

                    else:

                        guard_visited_distinct_positions.add(f'{guard_row_index}i{guard_col_index}j')

                        self.map[guard_row_index][guard_col_index] = 'X' # Footprint
                        
                        break # Guard moves out of map

                elif guard_standpoint == 'v':

                    if guard_row_index+1 < max_rows:

                        if self.map[guard_row_index+1][guard_col_index] == '#': # Obstacle, turn right
                            
                            self.map[guard_row_index][guard_col_index] = '<'

                            guard_standpoint = '<'

                            guard_engaged_obtacles.append([(guard_row_index+1, guard_col_index), guard_standpoint])

                        else:

                            self.map[guard_row_index][guard_col_index] = 'X' # Footprint

                            guard_row_index += 1

                            self.map[guard_row_index][guard_col_index] = 'v' # No obstacle, move forward

                            guard_visited_distinct_positions.add(f'{guard_row_index}i{guard_col_index}j')

                    else:

                        guard_visited_distinct_positions.add(f'{guard_row_index}i{guard_col_index}j')

                        self.map[guard_row_index][guard_col_index] = 'X' # Footprint
                        
                        break # Guard moves out of map

                elif guard_standpoint == '<':

                    if guard_col_index-1 >= 0:

                        if self.map[guard_row_index][guard_col_index-1] == '#': # Obstacle, turn right
                            
                            self.map[guard_row_index][guard_col_index] = '^'

                            guard_standpoint = '^'

                            guard_engaged_obtacles.append([(guard_row_index, guard_col_index-1), guard_standpoint])

                        else:

                            self.map[guard_row_index][guard_col_index] = 'X' # Footprint

                            guard_col_index -= 1

                            self.map[guard_row_index][guard_col_index] = '<' # No obstacle, move forward

                            guard_visited_distinct_positions.add(f'{guard_row_index}i{guard_col_index}j')

                    else:

                        guard_visited_distinct_positions.add(f'{guard_row_index}i{guard_col_index}j')

                        self.map[guard_row_index][guard_col_index] = 'X' # Footprint
                        
                        break # Guard moves out of map


        except Exception as e:

            print("Error in solve_puzzle_1():", e)

        return len(guard_visited_distinct_positions), guard_visited_distinct_positions, guard_engaged_obtacles
    
    def solve_puzzle_2(self, visited_positions, engaged_obstacles):

        """
        Find total number of possible loop obstructions to make the guard move in a loop.

        Loop is formed by 4 obstacles making closed path. If we have info of first threee obstacles engaged by guard, we can find possible fourth loop obstacle.

        """

        total_possible_loop_obstructions = 0

        try:
            
            # loop_obs_cal_dict contains values for finding obstruction possible for making guard move in loop according to guard standpoint
            loop_obs_cal_dict = {
                '^': (-1,1),
                '>': (1,1),
                'v': (1,-1),
                '<': (-1,-1)
            }

            for i in range(len(engaged_obstacles)-2):

                """
                Find possible fourth loop obstacle by using the information of any 3 pair of obstacles in sequential form.
                """

                first_obs = engaged_obstacles[i]

                third_obs = engaged_obstacles[i+2]

                guard_future_standpoint = third_obs[1]

                possible_loop_obs_row = -1

                possible_loop_obs_col = -1

                if guard_future_standpoint == '^' or guard_future_standpoint == 'v':

                    possible_loop_obs_row = first_obs[0][0] + loop_obs_cal_dict[guard_future_standpoint][0]

                    possible_loop_obs_col = third_obs[0][1] + loop_obs_cal_dict[guard_future_standpoint][1] 

                elif guard_future_standpoint == '>' or guard_future_standpoint == '<':

                    possible_loop_obs_row = third_obs[0][0] + loop_obs_cal_dict[guard_future_standpoint][0]

                    possible_loop_obs_col = first_obs[0][1] + loop_obs_cal_dict[guard_future_standpoint][1] 

                print(f'{possible_loop_obs_row}i{possible_loop_obs_col}j')

                if f'{possible_loop_obs_row}i{possible_loop_obs_col}j' in visited_positions:

                    total_possible_loop_obstructions += 1

        except Exception as e:

            print("Error in solve_puzzle_2():", e)

        return total_possible_loop_obstructions

if __name__ == "__main__":

    s = Solution('sample-input-day-6.txt')

    answer_puzzle_1, guard_visited_distinct_positions, guard_engaged_obtacles = s.solve_puzzle_1()

    print("Answer of Puzzle#1:", answer_puzzle_1)

    answer_puzzle_2 = s.solve_puzzle_2(guard_visited_distinct_positions, guard_engaged_obtacles)

    print("Answer of Puzzle#2:", answer_puzzle_2)