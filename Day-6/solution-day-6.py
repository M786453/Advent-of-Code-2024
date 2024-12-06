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
    
    def move_guard(self):

        try:
            
            pass

        except Exception as e:

            print("Error in move_guard():",e )

    def show_map(self):

        try:

            for row in self.map:
                print("".join(row))
            
        except Exception as e:
            print("Error in show_map():",e)
    
    def solve_puzzle_1(self):

        distinct_positions = set()

        try:

            max_rows = len(self.map)

            max_cols = len(self.map[0])

            guard_standpoint = '^'
            
            guard_row_index, guard_col_index = self.find_guard_cords()

            while True:

                # self.show_map()

                # print("")

                # print("")

                if guard_standpoint == '^':
                    
                    if guard_row_index-1 >= 0:

                        if self.map[guard_row_index-1][guard_col_index] == '#': # Obstacle, turn right
                            
                            self.map[guard_row_index][guard_col_index] = '>'

                            guard_standpoint = '>'

                        else:

                            self.map[guard_row_index][guard_col_index] = 'X' # Footprint

                            guard_row_index -= 1

                            self.map[guard_row_index][guard_col_index] = '^' # No obstacle, move forward

                            distinct_positions.add(f'{guard_row_index}i{guard_col_index}j')

                    else:

                        distinct_positions.add(f'{guard_row_index}i{guard_col_index}j')

                        self.map[guard_row_index][guard_col_index] = 'X' # Footprint

                        # self.show_map()
                        
                        break # Guard moves out of map

                elif guard_standpoint == '>':

                    if guard_col_index+1 < max_cols:

                        if self.map[guard_row_index][guard_col_index+1] == '#': # Obstacle, turn right
                            
                            self.map[guard_row_index][guard_col_index] = 'v'

                            guard_standpoint = 'v'

                        else:

                            self.map[guard_row_index][guard_col_index] = 'X' # Footprint

                            guard_col_index += 1

                            self.map[guard_row_index][guard_col_index] = '>' # No obstacle, move forward

                            distinct_positions.add(f'{guard_row_index}i{guard_col_index}j')

                    else:

                        distinct_positions.add(f'{guard_row_index}i{guard_col_index}j')

                        self.map[guard_row_index][guard_col_index] = 'X' # Footprint

                        # self.show_map()
                        
                        break # Guard moves out of map

                elif guard_standpoint == 'v':

                    if guard_row_index+1 < max_rows:

                        if self.map[guard_row_index+1][guard_col_index] == '#': # Obstacle, turn right
                            
                            self.map[guard_row_index][guard_col_index] = '<'

                            guard_standpoint = '<'

                        else:

                            self.map[guard_row_index][guard_col_index] = 'X' # Footprint

                            guard_row_index += 1

                            self.map[guard_row_index][guard_col_index] = 'v' # No obstacle, move forward

                            distinct_positions.add(f'{guard_row_index}i{guard_col_index}j')

                    else:

                        distinct_positions.add(f'{guard_row_index}i{guard_col_index}j')

                        self.map[guard_row_index][guard_col_index] = 'X' # Footprint

                        # self.show_map()
                        
                        break # Guard moves out of map

                elif guard_standpoint == '<':

                    if guard_col_index-1 >= 0:

                        if self.map[guard_row_index][guard_col_index-1] == '#': # Obstacle, turn right
                            
                            self.map[guard_row_index][guard_col_index] = '^'

                            guard_standpoint = '^'

                        else:

                            self.map[guard_row_index][guard_col_index] = 'X' # Footprint

                            guard_col_index -= 1

                            self.map[guard_row_index][guard_col_index] = '<' # No obstacle, move forward

                            distinct_positions.add(f'{guard_row_index}i{guard_col_index}j')

                    else:

                        distinct_positions.add(f'{guard_row_index}i{guard_col_index}j')

                        self.map[guard_row_index][guard_col_index] = 'X' # Footprint

                        # self.show_map()
                        
                        break # Guard moves out of map


        except Exception as e:

            print("Error in solve_puzzle_1():", e)

        return len(distinct_positions)
    
    def solve_puzzle_2(self):

        pass

if __name__ == "__main__":

    s = Solution('input-day-6.txt')

    answer_puzzle_1 = s.solve_puzzle_1()

    print("Answer of Puzzle#1:", answer_puzzle_1)

    # answer_puzzle_2 = s.solve_puzzle_2()

    # print("Answer of Puzzle#2:", answer_puzzle_2)