

def generate_secret(s):

    step1 = ((s * 64) ^ s) % 16777216
    
    step2 = (( step1 // 32) ^ step1) % 16777216

    step3 = (( step2 * 2048) ^ step2) % 16777216

    return step3


def generate_last_secret(secretNum):

    x = 0

    while x < 2000:

        secretNum = generate_secret(secretNum)

        x = x + 1

    return secretNum

def generate_last_secret_2(secretNum):

    x = 0

    prev_sec = None

    price_change_sequence = []

    price_changes_mapping = {} # price_change_sequence: list_of_price_of_each_buyer

    while x < 2000:

        prev_sec = secretNum

        secretNum = generate_secret(secretNum)

        if prev_sec != None:

            p1 = int(str(prev_sec)[-1])
            p2 = int(str(secretNum)[-1])

            price_change_sequence.append(p2 - p1)

            if len(price_change_sequence) == 4:                
                
                pc_key = tuple(price_change_sequence)

                if pc_key not in price_changes_mapping:
                    price_changes_mapping[pc_key] = p2

                price_change_sequence = price_change_sequence[1:]

        x = x + 1

    return price_changes_mapping

def solve_puzzle_1(initial_secrets_list):

    last_sec_list = []

    for init_sec in initial_secrets_list:

        last_sec_list.append(generate_last_secret(int(init_sec)))

    print('Answer Puzzle#1:',sum(last_sec_list))

def solve_puzzle_2(initial_secrets_list):

    all_buyers_price_change_mapping = {}

    counter = 1

    for init_sec in initial_secrets_list:

        # print("Counter:", counter)

        pc_mapping = generate_last_secret_2(int(init_sec))

        for pc_key in pc_mapping:

            if pc_key in all_buyers_price_change_mapping:

                all_buyers_price_change_mapping[pc_key].append(pc_mapping[pc_key])
            
            else:

                all_buyers_price_change_mapping[pc_key] = [pc_mapping[pc_key]]

        counter += 1

    
    best_price = max([sum(all_buyers_price_change_mapping[pc_key]) for pc_key in all_buyers_price_change_mapping])

    print('Answer Puzzle#2:', best_price)

with open('input-day-22.txt','r') as f:

    data = f.read()

    initial_secrets_list = data.split('\n')

    # solve_puzzle_1(initial_secrets_list)
    solve_puzzle_2(initial_secrets_list)