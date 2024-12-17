"""
Day#: 17
Problem Title: Chronospatial Computer
Author: Muhammad Ahtesham Sarwar
"""

class Solution:

    def __init__(self, filename):

        self.registers, self.program = self.read_input(filename=filename)

    def read_input(self,filename):

        registers, program = {}, []

        try:
            
            with open(filename, 'r') as f:

                raw_registers, raw_program = f.read().split('\n\n')

                # Extract and store registers

                raw_registers = raw_registers.split('\n')

                for reg in raw_registers:

                    reg_title, reg_value = reg.split(': ')

                    registers[reg_title[-1]] = int(reg_value)

                # Extract and store program

                program = [int(n) for n in raw_program.split(': ')[-1].split(',')]


        except Exception as e:

            print("Error in read_input():", e)

        return registers, program
    
    def calculate_combo(self, operand):

        combo = operand

        if operand == 4:
            combo = self.registers['A']
        elif operand == 5:
            combo = self.registers['B']
        elif operand == 6:
            combo = self.registers['C']
 
        return combo
    
    def execute_instruction(self, opcode, operand, instruction_pointer, output):

        ip_increment = 2

        if opcode == 0: # adv

            self.registers['A'] = (self.registers['A'] // (2 ** self.calculate_combo(operand)))
        
        elif opcode == 1: # bxl

            self.registers['B'] = (self.registers['B'] ^ operand)
        
        elif opcode == 2: # bst

            self.registers['B'] = (self.calculate_combo(operand) % 8)

        elif opcode == 3: # jnz

            if self.registers['A'] != 0:

                instruction_pointer = operand
                
                ip_increment = 0
        
        elif opcode == 4: # bxc

            self.registers['B'] = (self.registers['B'] ^ self.registers['C'])

        elif opcode == 5: # out

            output.append(str(self.calculate_combo(operand) % 8))

        elif opcode == 6: # bdv

            self.registers['B'] = (self.registers['A'] // (2 ** self.calculate_combo(operand)))

        elif opcode == 7: # cdv

            self.registers['C'] = (self.registers['A'] // (2 ** self.calculate_combo(operand)))
        
        instruction_pointer += ip_increment

        return instruction_pointer, output

    def solve_puzzle_1(self):

        instruction_pointer = 0

        output = []

        while instruction_pointer < len(self.program):

            opcode, operand = self.program[instruction_pointer:instruction_pointer+2]

            instruction_pointer, output = self.execute_instruction(opcode, operand, instruction_pointer, output)

        return ",".join(output) # Comma separated output


if __name__ == "__main__":

    s = Solution('input-day-17.txt')

    answer_puzzle_1 = s.solve_puzzle_1()

    print("Answer of Puzzle#1:", answer_puzzle_1)