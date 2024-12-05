"""
Day#: 3
Problem Title: Mull It Over
Author: Muhammad Ahtesham Sarwar
"""
import re

class Solution:

    def __init__(self, filename):

        self.corrupted_memory = self.read_input(filename=filename)

    def read_input(self,filename):

        data = ""

        try:
            
            with open(filename, 'r') as f:

                data = f.read()

        except Exception as e:

            print("Error in read_input():", e)

        return data
    
    def solve_puzzle_1(self):

        """
        Find all possible expression matching the pattern: mul(digit,digit) and then
        calculating sum of after multiplying the found expressions.

        Returns:

        int: sum of all results of mul expressions.

        """

        total = 0

        try:
            
            mul_matches = re.findall('mul[(][0-9]+,[0-9]+[)]', self.corrupted_memory)

            for match in mul_matches:

                match = match.replace('mul(','').replace(')','')

                num1, mum2 = match.split(',')

                total += int(num1) * int(mum2)

        except Exception as e:

            print("Error in solve_puzzle_1():", e)

        return total
    
    def solve_puzzle_2(self):

        """
        Remove all don't() relevant mul instructions from given data and then calculate result by
        add results of all mul expressions.

        - The do() instruction enables future mul instructions.
        - The don't() instruction disables future mul instructions.

        Returns:

        int: sum of results of all mul instructions
        """

        total = 0

        try:

            modified_corrupted_memory = str(self.corrupted_memory).replace('\n','')

            disabled_mul_pattern_1 = "don.*?do[(][)]"

            modified_corrupted_memory = re.sub(disabled_mul_pattern_1, '', modified_corrupted_memory)

            disabled_mul_pattern_2 = "don.*"

            modified_corrupted_memory = re.sub(disabled_mul_pattern_2, '', modified_corrupted_memory)

            mul_matches = re.findall('mul[(][0-9]+,[0-9]+[)]', modified_corrupted_memory)

            for match in mul_matches:

                match = match.replace('mul(','').replace(')','')

                num1, mum2 = match.split(',')

                total += int(num1) * int(mum2)

        except Exception as e:

            print("Error in sovle_puzzle_2():", e)

        return total

if __name__ == "__main__":

    s = Solution('input-day-3.txt')

    answer_puzzle_1 = s.solve_puzzle_1()

    print("Answer of Puzzle#1:", answer_puzzle_1)

    answer_puzzle_2 = s.solve_puzzle_2()

    print("Answer of Puzzle#2:", answer_puzzle_2)