"""
Day#: 5
Problem Title: Print Queue
Author: Muhammad Ahtesham Sarwar
"""

class Solution:

    def __init__(self, filename):

        self.printing_rules, self.manual_updates = self.read_input(filename=filename)

    def read_input(self,filename):

        printing_rules_dict = {}

        manual_updates = []

        try:
            
            with open(filename, 'r') as f:

                raw_printing_rules, raw_manual_updates = f.read().split('\n\n')

                raw_printing_rules = raw_printing_rules.split("\n")

                # Organizing Printing rules
                ## Printing rules organized in this format: {'number': {'before': [], 'after': []}}

                for rule in raw_printing_rules:

                    rule_parts_list = rule.split("|")

                    if rule_parts_list[0] in printing_rules_dict:

                        printing_rules_dict[rule_parts_list[0]]["after"].append(rule_parts_list[1])
                    
                    else:

                        printing_rules_dict[rule_parts_list[0]] = {"before": [],"after": [rule_parts_list[1]]}

                    if rule_parts_list[1] in printing_rules_dict:

                        printing_rules_dict[rule_parts_list[1]]["before"].append(rule_parts_list[0])

                    else:

                        printing_rules_dict[rule_parts_list[1]] = {"before": [rule_parts_list[0]], "after": []}

                # Organizing manual updates data

                manual_updates = [e.split(",") for e in raw_manual_updates.split("\n")]

        except Exception as e:

            print("Error in read_input():", e)

        return [printing_rules_dict, manual_updates]
    
    def solve_puzzle_1(self):

        total = 0

        try:

            for update in self.manual_updates:

                update_length = len(update)

                is_valid_update = True

                # Check whether update is satisfying the rules or not

                for index in range(update_length):

                    page_number = update[index]

                    page_number_rules = self.printing_rules[page_number]

                    # Validate rules for page numbers before target page number

                    if index > 0:

                        for before_page_number in update[:index]:

                            if before_page_number not in page_number_rules["before"]: # Rule voilation

                                is_valid_update = False

                                break

                    # Validate rules for page numbers after target page number

                    if is_valid_update and index != update_length - 1:

                        for after_page_number in update[index+1:]:

                            if after_page_number not in page_number_rules["after"]: # Rule voilation

                                is_valid_update = False

                                break
                
                # If update is valid, add middle number of update in total

                if is_valid_update:

                    total += int(update[update_length//2])

        except Exception as e:

            print("Error in solve_puzzle_1():", e)

        return total
    
    def solve_puzzle_2(self):

        pass

if __name__ == "__main__":

    s = Solution('input-day-5.txt')

    answer_puzzle_1 = s.solve_puzzle_1()

    print("Answer of Puzzle#1:", answer_puzzle_1)

    # answer_puzzle_2 = s.solve_puzzle_2()

    # print("Answer of Puzzle#2:", answer_puzzle_2)