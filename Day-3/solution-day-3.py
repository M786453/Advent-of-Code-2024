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

        total = 0

        try:
            
            mul_matches = re.findall(r'mul[(][0-9]+,[0-9]+[)]', self.corrupted_memory)

            for match in mul_matches:

                match = match.replace('mul(','').replace(')','')

                num1, mum2 = match.split(',')

                total += int(num1) * int(mum2)

        except Exception as e:

            print("Error in solve_puzzle_1():", e)

        return total
    
    def solve_puzzle_2(self):

        pass

if __name__ == "__main__":

    s = Solution('input-day-3.txt')

    answer_puzzle_1 = s.solve_puzzle_1()

    print("Answer of Puzzle#1:", answer_puzzle_1)

    # answer_puzzle_2 = s.solve_puzzle_2()

    # print("Answer of Puzzle#2:", answer_puzzle_2)