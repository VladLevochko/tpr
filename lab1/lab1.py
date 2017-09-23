import numpy as np
import matplotlib.pyplot as plt
from past.builtins import xrange


def get_numbers(path_to_data_file):
    i = 0
    all = []
    pareto_set = []
    sleiter_set = []
    with open(path_to_data_file, 'r') as file:
        for line in file:
            values = line.split()
            if len(values) < 2:
                i += 1
                continue

            if i == 0:
                all.append([int(values[0]), int(values[1])])
            elif i == 1:
                pareto_set.append([int(values[0]), int(values[1])])
            elif i == 2:
                sleiter_set.append([int(values[0]), int(values[1])])
            else:
                break

    all = np.array(all)
    pareto_set = np.array(pareto_set)
    sleiter_set = np.array(sleiter_set)

    return all, pareto_set, sleiter_set

# def transform_to_alternatives(numbers):
#     n = len(numbers)
#     alternatives = np.zeros((n, 2))
#     for i in xrange(n):
#         alternatives[i, 0] = numbers[i] // 10
#         alternatives[i, 1] = numbers[i] % 10
#
#     return alternatives


if __name__ == '__main__':
    all, pareto_set, sleiter_set = get_numbers('ans_set_global')

    plt.plot(all[:, 0], all[:, 1], 'ro', label='alternatives')
    # plt.plot(pareto_set[:, 1], pareto_set[:, 0], 'go' if len(pareto_set) == 1 else 'g--', label='pareto')
    plt.plot(sleiter_set[:, 1], sleiter_set[:, 0], 'bo' if len(sleiter_set) == 1 else 'b--', label='sleiter')
    plt.show()


