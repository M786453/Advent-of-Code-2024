"""
Day#: 10
Problem Title: Hoof It
Author: Muhammad Ahtesham Sarwar
"""

class Solution:

    def __init__(self, filename):

        self.map = self.read_input(filename=filename)

        self.rating = 0 # sum of the ratings of all trailheads; [A trailhead's rating is the number of distinct hiking trails which begin at that trailhead.]

        self.map_bound = len(self.map[0])

    def read_input(self,filename):

        data = []

        try:
            
            with open(filename, 'r') as f:

                raw_data_lines = f.read().split('\n')

                for line in raw_data_lines:

                    data.append([int(chr) for chr in line])

        except Exception as e:

            print("Error in read_input():", e)

        return data
    
    def hike(self, cord, visited_heights):

        """"
        hike() is a recursive function which finds a number (which should be greater than it by 1) in it's adjacent location (left,right,up and down).
        If number found, then it will change the current coordinates to that location and repeat the process until it finds the number 9 which is highest.
        Finding number 9 mean it found the highest point of trail and trail completed.

        If more than one numbers are found which is greater than current number by 1, then it will call the hike function recursiving on the coordinates of each number
        to start a different hiking trial.

        visited_height: it will store the unique coordinates of highest point visited. It will be used to find the score for first part of puzzle.

        """

        is_trail_found = False

        while True:

            tmp_cord = list(cord)

            if self.map[cord[0]][cord[1]] == 9:
                visited_heights.add((cord[0],cord[1]))
                self.rating += 1 # Each highest 9 point is found by distinct trail, so increase rating.
                break      

            if tmp_cord[0]-1 >= 0 and (self.map[tmp_cord[0]-1][tmp_cord[1]] - self.map[tmp_cord[0]][tmp_cord[1]] == 1): # UP

                cord[0] -= 1

                is_trail_found = True
            
            if tmp_cord[0]+1 < self.map_bound and (self.map[tmp_cord[0]+1][tmp_cord[1]] - self.map[tmp_cord[0]][tmp_cord[1]] == 1): # Down
                
                if is_trail_found:
                    self.hike(cord=list([tmp_cord[0]+1, tmp_cord[1]]),visited_heights=visited_heights)
                else:
                    cord[0] += 1
                    is_trail_found = True

            if tmp_cord[1]-1 >= 0 and (self.map[tmp_cord[0]][tmp_cord[1]-1] - self.map[tmp_cord[0]][tmp_cord[1]] == 1): # Left

                if is_trail_found:
                    self.hike(cord=list([tmp_cord[0], tmp_cord[1]-1]), visited_heights=visited_heights)
                else:
                    cord[1] -= 1
                    is_trail_found = True

            if tmp_cord[1]+1 < self.map_bound and (self.map[tmp_cord[0]][tmp_cord[1]+1] - self.map[tmp_cord[0]][tmp_cord[1]] == 1): # Right

                if is_trail_found:
                    self.hike(cord=list([tmp_cord[0], tmp_cord[1]+1]), visited_heights=visited_heights)
                else:
                    cord[1] += 1
                    is_trail_found = True

            if is_trail_found == False:
                break # No trial found, break loop

            is_trail_found = False # Reset
    
    def solve_puzzle_1(self):

        total_score = 0

        for row_index in range(len(self.map)):

            row = self.map[row_index]

            for col_index in range(len(row)):

                if row[col_index] == 0: # Find 0 (starting point of trial) and start hiking from found coordinates
                    visited_heights = set()
                    self.hike(cord=[row_index, col_index], visited_heights=visited_heights)
                    total_score += len(visited_heights)

        return total_score
    
    def solve_puzzle_2(self):

        return self.rating

if __name__ == "__main__":

    s = Solution('input-day-10.txt')

    answer_puzzle_1 = s.solve_puzzle_1()

    print("Answer of Puzzle#1:", answer_puzzle_1)

    answer_puzzle_2 = s.solve_puzzle_2()

    print("Answer of Puzzle#2:", answer_puzzle_2)