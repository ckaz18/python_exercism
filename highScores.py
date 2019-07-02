# Implement 3 methods
# 1 - Return the highest score from list
# 2 - Return the last added score
# 3 - Return the highest scores

def getHighestScore(list):
    max = 0
    for x in list:
        if x > max:
            max = x

    return list.index(max)


def getLastScore(list):
    return list[-1]

def getTopThreeHighestScores(list):
    sortArr = list
    sortArr.sort()

    return sortArr[-3:]