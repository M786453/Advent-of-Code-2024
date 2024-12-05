"""
Day#: 4
Problem Title: Ceres Search
Author: Muhammad Ahtesham Sarwar
"""

class Solution:

    def __init__(self, filename):

        self.word_search = self.read_input(filename=filename)

    def read_input(self,filename):

        data = []

        try:
            
            with open(filename, 'r') as f:

                data = f.read().split('\n')

        except Exception as e:

            print("Error in read_input():", e)

        return data
    
    def solve_puzzle_1(self):

        """
        Find all possible matches of 'XMAS' in given word_search data.
        'XMAS' can be horizontal, vertical, diagonal, written backwards, or even overlapping other words.

        Returns:
        int: total matches of xmas found.
        """

        total_matches = 0

        try:
            
            for i in range(len(self.word_search)):

                row = self.word_search[i]

                for j in range(len(row)):

                    # Rows Forward Range Check

                    rfr_check = (i <= len(self.word_search) - 4)

                    # Rows Backward Range Check

                    rbr_check = (i - 3 >= 0)
                    
                    # Columns Forward Range Check

                    cfr_check = (j <= len(row) - 4)

                    # Columns Backward Range Check

                    cbr_check = (j - 3 >= 0)

                    if row[j] == 'X':

                        # Forward Horizontal Check

                        if cfr_check and row[j] + row[j+1] + row[j+2] + row[j+3] == 'XMAS':

                            total_matches += 1

                        # Backward Horizontal Check

                        if cbr_check and row[j] + row[j-1] + row[j-2] + row[j-3] == 'XMAS':

                            total_matches += 1

                        # Forward Vertical Check

                        if rfr_check and row[j] + self.word_search[i+1][j] + self.word_search[i+2][j] + self.word_search[i+3][j] == 'XMAS':

                            total_matches += 1

                        # Backward Vertical Check

                        if rbr_check and row[j] + self.word_search[i-1][j] + self.word_search[i-2][j] + self.word_search[i-3][j] == 'XMAS':

                            total_matches += 1

                        # Forward Up Right Diagonal Check

                        if cfr_check and rbr_check and row[j] + self.word_search[i-1][j+1] + self.word_search[i-2][j+2] + self.word_search[i-3][j+3] == 'XMAS':

                            total_matches += 1

                        # Forward Down Right Diagnoal Check

                        if cfr_check and rfr_check and row[j] + self.word_search[i+1][j+1] + self.word_search[i+2][j+2] + self.word_search[i+3][j+3] == 'XMAS':

                            total_matches += 1

                        # Backward Up Left Diagonal Check

                        if cbr_check and rbr_check and row[j] + self.word_search[i-1][j-1] + self.word_search[i-2][j-2] + self.word_search[i-3][j-3] == 'XMAS':

                            total_matches += 1

                        # Backward Down Left Diagonal Check

                        if cbr_check and rfr_check and row[j] + self.word_search[i+1][j-1] + self.word_search[i+2][j-2] + self.word_search[i+3][j-3] == 'XMAS':

                            total_matches += 1

        except Exception as e:
            print("Error in solve_puzzle_1():", e)

        return total_matches
    
    def solve_puzzle_2(self):

        """
        Find all possible X-MAS (two MAS in shape of X)
        Within the X, each MAS can be written forwards or backwards.

        Returns:
        int: total possible x-masses.
        """

        total_x_masses = 0

        try:
            
            for i in range(len(self.word_search)):

                row = self.word_search[i]

                for j in range(len(row)):

                    # Rows Forward Range Check

                    rfr_check = (i <= len(self.word_search) - 2)

                    # Rows Backward Range Check

                    rbr_check = (i - 1 >= 0)
                    
                    # Columns Forward Range Check

                    cfr_check = (j <= len(row) - 2)

                    # Columns Backward Range Check

                    cbr_check = (j - 1 >= 0)

                    if row[j] == 'A':

                        # Diagonal Check

                        if cfr_check and cbr_check and rfr_check and rbr_check:

                            mas_count = 0
                            
                            if self.word_search[i-1][j+1] + row[j] + self.word_search[i+1][j-1] == 'MAS':

                                mas_count += 1

                            if self.word_search[i+1][j-1] + row[j] + self.word_search[i-1][j+1] == 'MAS':

                                mas_count += 1
                            
                            if self.word_search[i-1][j-1] + row[j] + self.word_search[i+1][j+1] == 'MAS':

                                mas_count += 1
                            
                            if self.word_search[i+1][j+1] + row[j] + self.word_search[i-1][j-1] == 'MAS':

                                mas_count += 1

                            if mas_count == 2:

                                total_x_masses += 1

        except Exception as e:

            print("Error in solve_puzzle_2():", e)

        return total_x_masses

if __name__ == "__main__":

    s = Solution('input-day-4.txt')

    answer_puzzle_1 = s.solve_puzzle_1()

    print("Answer of Puzzle#1:", answer_puzzle_1)

    answer_puzzle_2 = s.solve_puzzle_2()

    print("Answer of Puzzle#2:", answer_puzzle_2)