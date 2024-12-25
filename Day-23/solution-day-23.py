networks = open('input-day-23.txt','r').read().split('\n')

computers_connections = {}

def add_computer_conn(c1, c2):

    if c1 in computers_connections:

        computers_connections[c1].append(c2)
    
    else:

        computers_connections[c1] = [c2]

for net in networks:

    c1, c2 = net.split('-')

    add_computer_conn(c1, c2)
    add_computer_conn(c2, c1)

def solve_puzzle_1():
    # Pairs of Three Interconnected computers set
    three_ics_pair = set()

    for c in computers_connections:

        connected_computers = computers_connections[c] # computers connected to current computer

        for i in range(len(connected_computers)):

            for j in range(len(connected_computers)):

                c1 = connected_computers[i]
                c2 = connected_computers[j]

                if c1 != c2:
                    
                    if c1 in computers_connections[c2]:
                        ics = [c, c1, c2] # Interconnected computers
                        if any([c.startswith('t')for c in ics]):
                            ics.sort()
                            three_ics_pair.add(tuple(ics))

    print('Answer Puzzle#1:',len(three_ics_pair))

def solve_puzzle_2():

    largest_set = []

    for c in computers_connections:

        connected_computers = computers_connections[c] # computers connected to current computer

        ics = [] # interconnected computers

        ics.append(c)

        for i in range(len(connected_computers)):

            c1 = connected_computers[i]

            connections_list = [c1]

            for j in range(len(connected_computers)):

                c2 = connected_computers[j]

                if c1 != c2:
                    
                    if c1 in computers_connections[c2]:
                        connections_list.append(c2)
            
            if len(connections_list) == len(connected_computers)-1: # Connected to all

                ics.append(c1)           

        if len(ics) > len(largest_set):

            largest_set = ics
    
    largest_set.sort()

    print("Answer Puzzle#2:", ",".join(largest_set))

solve_puzzle_1()
solve_puzzle_2()
                


