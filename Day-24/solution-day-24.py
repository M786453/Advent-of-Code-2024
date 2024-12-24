"""
Day#: 24
Problem Title: Crossed Wires
Author: Muhammad Ahtesham Sarwar
"""
from collections import deque

class Soultion:

    def __init__(self, filename):

        self.wires, self.gates = open(filename, 'r').read().split('\n\n')

        self.wires = {wire.split(': ')[0]:int(wire.split(': ')[1]) for wire in self.wires.split('\n')}

        self.gates = deque([gate.replace(' -> ',' ').split(' ') for gate in self.gates.split('\n')])
    
    def simulate_gates(self):

        while self.gates:

            gate = self.gates.popleft()

            in_wire_1, gate_operation, in_wire_2, out_wire = gate

            # Check whether both input wires are available for gate operation
            if in_wire_1 in self.wires and in_wire_2 in self.wires:

                if gate_operation == 'AND':

                    self.wires[out_wire] =  self.wires[in_wire_1] and self.wires[in_wire_2]

                elif gate_operation == 'OR':

                    self.wires[out_wire] = self.wires[in_wire_1] or self.wires[in_wire_2]

                elif gate_operation == 'XOR':

                    self.wires[out_wire] = int(self.wires[in_wire_1] != self.wires[in_wire_2])
            
            else:
                # If both input wires are not available, then append the gate in queue
                self.gates.append(gate)
        
    def solve_puzzle_1(self):

        """
        Simulate the system of gates and wires. What decimal number does it output on the wires starting with z?
        """

        self.simulate_gates()

        bits = []

        z_wires = []

        for w in self.wires:

            if w.startswith('z'):

                z_wires.append(w)

        z_wires.sort() # Sort z wires in alphanumeric order

        bits = ''.join([str(self.wires[key]) for key in z_wires][-1::-1]) # Reverse the bits of z-wires and convert into string

        answer_1 = int(bits,2) # Convert binary bits into decimal

        print("Answer Puzzle#1:", answer_1)

if __name__ == "__main__":

    s = Soultion('input-day-24.txt')

    s.solve_puzzle_1()