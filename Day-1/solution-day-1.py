"""
Day#: 1
Problem Title: Historian Hysteria
Author: Muhammad Ahtesham Sarwar
"""

class Solution:

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
    
    def solve_puzzle_1(self, input_filename):

        total_distance = 0

        try:

            locations_lists = self.read_input(filename=input_filename)

            sorted_loc_list_1 = sorted(locations_lists[0])

            sorted_loc_list_2 = sorted(locations_lists[1])

            for index in range(len(sorted_loc_list_1)):

                total_distance += abs(sorted_loc_list_1[index] - sorted_loc_list_2[index])

        except Exception as e:

            print("Error in solve():", e)

        return total_distance

    
if __name__ == "__main__":

    answer_puzzle_1 = Solution().solve_puzzle_1('input-day-1.txt')

    print("Answer of Puzzle#1:", answer_puzzle_1)

