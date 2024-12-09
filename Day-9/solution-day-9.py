"""
Day#: 9
Problem Title: Disk Fragmenter
Author: Muhammad Ahtesham Sarwar
"""

class Solution:

    def __init__(self, filename):

        self.files, self.free_spaces = self.read_input(filename=filename)

    def read_input(self,filename):

        files, free_spaces = [],[]

        try:
            
            with open(filename, 'r') as f:

                data = f.read()

                for index in range(len(data)):

                    val = int(data[index])

                    if index % 2 == 0:

                        files.append(val)

                    else:

                        free_spaces.append(val)

        except Exception as e:

            print("Error in read_input():", e)

        return files, free_spaces
    
    def calculate_check_sum(self, diskmap):

        total_check_sum = 0

        for index in range(len(diskmap)):

            total_check_sum += index * int(diskmap[index])

        return total_check_sum
    
    def move_files(self, disk_map):

        """
        Move files to contagious locations
        """

        modified_diskmap = list(disk_map)

        for index in range(len(disk_map)-1, -1, -1):

            if "." not in modified_diskmap[:index]:
                break

            if modified_diskmap[index] == '.':
                continue

            first_free_space_index = modified_diskmap.index('.')

            modified_diskmap[first_free_space_index] = modified_diskmap[index]

            modified_diskmap[index] = '.'

        modified_diskmap = "".join(modified_diskmap)

        modified_diskmap = modified_diskmap.replace('.','')

        return modified_diskmap

    def create_disk_map(self):

        """
        Create diskmap using file ids and their size. Similar for free spaces.
        """

        disk_map = ""

        last_index = len(self.files)-1

        for index in range(last_index):

            disk_map += str(index)*self.files[index] + "."*self.free_spaces[index]

        disk_map += str(last_index) * self.files[-1]

        return disk_map
    
    def solve_puzzle_1(self):

        disk_map = self.create_disk_map()

        modified_diskmap = self.move_files(disk_map)

        return self.calculate_check_sum(modified_diskmap)

if __name__ == "__main__":

    s = Solution('sample-input-day-9.txt')

    answer_puzzle_1 = s.solve_puzzle_1()

    print("Answer of Puzzle#1:", answer_puzzle_1)

    # answer_puzzle_2 = s.solve_puzzle_2()

    # print("Answer of Puzzle#2:", answer_puzzle_2)