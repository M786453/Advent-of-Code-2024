"""
Day#: 2
Problem Title: Red-Nosed Reports
Author: Muhammad Ahtesham Sarwar
"""
import re

class Solution:

    def __init__(self, filename):

        self.reports = self.read_input(filename=filename)

    def read_input(self,filename):

        reports = []

        try:
            
            with open(filename, 'r') as f:

                raw_reports = f.read().split('\n')

                for rp in raw_reports:

                    new_report = []

                    levels = rp.split(" ")

                    for l in levels:

                        new_report.append(int(l))
                
                    reports.append(new_report)

        except Exception as e:

            print("Error in read_input():", e)

        return reports
    
    def solve_puzzle_1(self):

        """
        Find total number of safe reports.

        The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

        - The levels are either all increasing or all decreasing.
        - Any two adjacent levels differ by at least one and at most three.

        Returns:

        int: total number of safe reports.
        
        """

        total_safe_reports = 0

        try:
            
            for rp in self.reports:

                is_safe_report = False

                if rp == sorted(rp) or rp == sorted(rp,reverse=True):

                    are_all_levels_safe = True

                    for i in range(len(rp)-1):

                        abs_difference = abs(int(rp[i]) - int(rp[i+1])) 

                        if abs_difference < 1 or abs_difference > 3:

                            are_all_levels_safe = False

                            break
                    
                    if are_all_levels_safe:
                        is_safe_report = True

                if is_safe_report:

                    total_safe_reports += 1

        except Exception as e:

            print("Error in solve_puzzle_1():", e)

        return total_safe_reports
    
    def solve_puzzle_2(self):

        pass

if __name__ == "__main__":

    s = Solution('input-day-2.txt')

    answer_puzzle_1 = s.solve_puzzle_1()

    print("Answer of Puzzle#1:", answer_puzzle_1)

    # answer_puzzle_2 = s.solve_puzzle_2()

    # print("Answer of Puzzle#2:", answer_puzzle_2)