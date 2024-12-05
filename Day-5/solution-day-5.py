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

        invalid_updates = []

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
                
                else:

                    invalid_updates.append(update)

        except Exception as e:

            print("Error in solve_puzzle_1():", e)

        return total, invalid_updates
    
    def solve_puzzle_2(self, invalid_updates):

        total = 0

        try:

            for update in invalid_updates:                

                validated_update = [update[0]]

                for page_number in update:

                    page_number_index = validated_update.index(page_number)

                    rules = self.printing_rules[page_number]

                    update_copy = list(update)

                    # Removed current page number from update in order to check rules (relevant to current page number) for other page numbers

                    update_copy.remove(page_number) 

                    for n in update_copy:                        

                        if n in rules["before"]:

                            if n in validated_update:
                                
                                if n in validated_update[:page_number_index]:

                                    # If page number is already present in required part of list, then move to next page number

                                    continue 

                                else:

                                    # If page number is not present in required part of list, then remove it

                                    validated_update.remove(n) 

                            # Insert the page number before the current page number

                            validated_update.insert(page_number_index,n)

                            page_number_index += 1
                        
                        elif n in rules["after"]:

                            if n in validated_update:
                                
                                if n in validated_update[page_number_index+1:]:

                                    # If page number is already present in required part of list, then move to next page number

                                    continue
                                
                                else:

                                    # If page number is not present in required part of list, then remove it

                                    validated_update.remove(n)

                                    page_number_index -= 1

                            # Insert the page number after the current page number

                            validated_update.insert(page_number_index+1, n)

                total += int(validated_update[len(validated_update)//2])

        except Exception as e:
            print("Error in solve_puzzle_2():", e)

        return total

if __name__ == "__main__":

    s = Solution('input-day-5.txt')

    answer_puzzle_1, invalid_updates = s.solve_puzzle_1()

    print("Answer of Puzzle#1:", answer_puzzle_1)

    answer_puzzle_2 = s.solve_puzzle_2(invalid_updates)

    print("Answer of Puzzle#2:", answer_puzzle_2)