import math

def average(data):
    mean = 0
    for i in data:
        mean += i
    mean /= len(data)
    return mean

def standardDeviation(data):
    mean = average(data)
    meanDiffs = []
    for i in data:
        meanDiffs.append((mean - i)**2)
    sd = sum(meanDiffs)
    sd /= len(meanDiffs) - 1
    sd = math.sqrt(sd)
    return sd

d = [60, 61, 65, 63, 98, 99, 90, 95, 91, 96]

print("Standard deviation: " + str(standardDeviation(d)))
