import numpy as np


def play(guesses: np.array):
    target = guesses.mean()*.75
    smallestDelta = 20
    winners = []

    for guess in guesses:
        d = np.abs(target-guess)
        if d < smallestDelta:
            smallestDelta = d
            winners = []
            winners.append(guess)
        elif d == smallestDelta:
            winners.append(guess)

    return winners


print(play(np.array([20, 20, 20, 20, 19])))
