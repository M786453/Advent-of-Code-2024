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

def solve_puzzle_1(initial_secrets_list):

    last_sec_list = []

    for init_sec in initial_secrets_list:

        last_sec_list.append(generate_last_secret(int(init_sec)))

    print('Answer Puzzle#1:',sum(last_sec_list))


with open('input-day-22.txt','r') as f:

    data = f.read()

    initial_secrets_list = data.split('\n')

    solve_puzzle_1(initial_secrets_list)