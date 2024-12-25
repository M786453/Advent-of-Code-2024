def generateSecList(s):

    step1 = ((s * 64) ^ s) % 16777216
    
    step2 = (( step1 // 32) ^ step1) % 16777216

    step3 = (( step2 * 2048) ^ step2) % 16777216

    return step3


def generateLastSecNum(secretNum):

    x = 0

    while x < 2000:

        secretNum = generateSecList(secretNum)

        x = x + 1

    return secretNum


with open('input-day-22.txt','r') as f:

    data = f.read()

    dataList = data.split('\n')

    lastSecNumList = []

    for initsecnum in dataList:

        lastSecNumList.append(generateLastSecNum(int(initsecnum)))

    print(sum(lastSecNumList))