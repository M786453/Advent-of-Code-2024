"""
Day#: 7
Problem Title: Bridge Repair
Author: Muhammad Ahtesham Sarwar
"""

class Solution:

    def __init__(self, filename):

        self.data = self.read_input(filename=filename)

        for test in self.data:

            if len(test[1]) == 1:

                print(test)
            
            elif len(test[1]) == 0:

                print(test)

    def read_input(self,filename):

        data = []

        try:
            
            with open(filename, 'r') as f:

                raw_data_lines = f.read().split('\n')

                for line in raw_data_lines:

                    test_value, raw_nums = line.split(':')

                    nums_list = raw_nums.strip().split(' ')

                    data.append([int(test_value), nums_list])

        except Exception as e:

            print("Error in read_input():", e)

        return data
    
    def evaluate_combination(self, combination):

        result = -1

        op = ''

        try:
            
            for val in combination:

                if val == '*':

                    op = val
                
                elif val == '+':

                    op = val
                
                else:

                    if result == -1:

                        result = val

                    else:

                        if op == '*':
                            result = result * val
                        elif op == '+':
                            result = result + val

        except Exception as e:

            print("Error in evaluate_combination():", e)

        return result
    
    def generate_operators_combinations(self, total_operator_positions):

        """
        Generate all possible combinations of operators
        """

        combinations = []

        op_dict = {'*': '+', '+': '*'}

        try:
            for op in ['*','+']:

                op_comb = [op_dict[op]] * total_operator_positions

                for i in range(1,total_operator_positions+1):

                    tmp_sub_comb = [op] * i

                    for index in range(total_operator_positions):

                        new_op_comb = op_comb[:index] + tmp_sub_comb + op_comb[index+i:]

                        if len(new_op_comb) == total_operator_positions and new_op_comb not in combinations:

                            combinations.append(new_op_comb)

        except Exception as e:

            print("Error in generate_operators_combinations():", e)

        return combinations
    
    def generate_combinations(self, num_list):

        """
        Generate possible combinations of operators in num_list
        """

        combinations = []

        total_operator_positions = len(num_list) - 1

        try:
            
            operators_combinations = self.generate_operators_combinations(total_operator_positions)

            for op_comb in operators_combinations:

                new_comb = []

                for i in range(len(num_list)-1):

                    new_comb.append(int(num_list[i]))

                    new_comb.append(op_comb[i])

                new_comb.append(int(num_list[-1]))

                combinations.append(new_comb)

        except Exception as e:

            print("Error in generate_combinations_2():", e)

        return combinations
    
    def solve_puzzle_1(self):

        total = 0

        for test in self.data:

            test_value = test[0]

            nums_list = test[1]

            combinations = s.generate_combinations(nums_list)

            for comb in combinations:

                if s.evaluate_combination(comb) == test_value:

                    total += test_value

                    break

        return total
    
    def solve_puzzle_2(self):

        pass

if __name__ == "__main__":

    s = Solution('test-input-day-7.txt')

    combinations = s.generate_combinations(['1','2','3','4','5','6'])

    for comb in combinations:

        print(comb)

    # answer_puzzle_1 = s.solve_puzzle_1()

    # print("Answer of Puzzle#1:", answer_puzzle_1)

    # answer_puzzle_2 = s.solve_puzzle_2()

    # print("Answer of Puzzle#2:", answer_puzzle_2)