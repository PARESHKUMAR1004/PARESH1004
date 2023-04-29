import numpy as np
from methods.TOPSIS import TOPSIS
from methods.moora import MOORA
from helpers import rrankdata

topsis = TOPSIS()
moora = MOORA()


def getOrderByTopsis(DecisionMatrix, Weight, types):
    PrefValue = topsis(np.array(DecisionMatrix),
                       np.array(Weight), np.array(types))
    ranking = rrankdata(PrefValue)
    noOfAlternatives = len(DecisionMatrix)
    finalAlternativeTable = np.zeros(noOfAlternatives, np.ndarray)
    iter = 0
    for r, p in zip(ranking, PrefValue):
        finalAlternativeTable[int(r)-1] = np.array(DecisionMatrix[iter])
        iter += 1
    return finalAlternativeTable


def getOrderByMoora(DecisionMatrix, Weight, types):
    PrefValue = moora(np.array(DecisionMatrix),
                      np.array(Weight), np.array(types))
    ranking = rrankdata(PrefValue)
    noOfAlternatives = len(DecisionMatrix)
    finalAlternativeTable = np.zeros(noOfAlternatives, np.ndarray)
    iter = 0
    for r, p in zip(ranking, PrefValue):
        finalAlternativeTable[int(r)-1] = np.array(DecisionMatrix[iter])
        iter += 1
    return finalAlternativeTable