"""
Day#: 1
Problem Title: Historian Hysteria
Author: Muhammad Ahtesham Sarwar
"""

class Solution:

    def __init__(self, filename):

        self.locations_lists = self.read_input(filename=filename)

    def read_input(self,filename):

        data = [[],[]]

        try:
            
            with open(filename, 'r') as f:

                raw_data_lines = f.read().split('\n')

                for line in raw_data_lines:

                    loc_id1, loc_id2 = line.split('   ')

                    data[0].append(int(loc_id1))

                    data[1].append(int(loc_id2))

        except Exception as e:

            print("Error in read_input():", e)

        return data
    
    def solve_puzzle_1(self):

        total_distance = 0

        try:

            sorted_loc_list_1 = sorted(self.locations_lists[0])

            sorted_loc_list_2 = sorted(self.locations_lists[1])

            for index in range(len(sorted_loc_list_1)):

                total_distance += abs(sorted_loc_list_1[index] - sorted_loc_list_2[index])

        except Exception as e:

            print("Error in solve():", e)

        return total_distance
    
    def solve_puzzle_2(self):

        similarity_score = 0

        try:

            for e in self.locations_lists[0]:

                similarity_score += e * self.locations_lists[1].count(e)

        except Exception as e:

            print("Error in solve_puzzle_2():", e)

        return similarity_score

if __name__ == "__main__":

    s = Solution('input-day-1.txt')

    answer_puzzle_1 = s.solve_puzzle_1()

    print("Answer of Puzzle#1:", answer_puzzle_1)

    answer_puzzle_2 = s.solve_puzzle_2()

    print("Answer of Puzzle#2:", answer_puzzle_2)