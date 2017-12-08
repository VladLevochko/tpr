import numpy as np


def get_candidates_with_max_votes(votes):
    """
    Returns list of candidates who have the most votes
    :param votes: dict with candidates and votes for them
    :return: list of candidates
    """
    candidates = []
    max_votes = max(votes.values())
    for candidate, votes in votes.items():
        if votes == max_votes:
            candidates.append(candidate)

    return candidates


def get_candidates_with_min_votes(votes):
    """
    Returns list of candidates who have the least votes
    :param votes: dict with candidates and votes for them
    :return: list of candidates
    """
    candidates = []
    min_votes = min(votes.values())
    for candidate, votes in votes.items():
        if votes == min_votes:
            candidates.append(candidate)

    return candidates


def relative_majority(election_matrix):
    votes = {}
    for candidates_order, votes_number in election_matrix.items():
        candidate = candidates_order[0]
        votes[candidate] = votes.get(candidate, 0) + votes_number

    winners = get_candidates_with_max_votes(votes)
    if len(winners) > 1:
        return "can't determine!"

    return winners[0]


def condorce(election_matrix):
    candidates = sorted(list(election_matrix.keys())[0])
    num_candidates = len(candidates)
    priority_matrix = np.zeros((num_candidates, num_candidates))

    for candidates_order, number_of_electors in election_matrix.items():
        for i, candidate in enumerate(candidates_order):
                higher_priority_candidate = candidates.index(candidate)
                for j in range(i + 1, num_candidates):
                    lower_priority_candidate = candidates.index(candidates_order[j])
                    priority_matrix[higher_priority_candidate,
                                    lower_priority_candidate] += number_of_electors

    total_votes = np.sum(priority_matrix, axis=1)
    max = 0
    winners_indices = []
    for i in range(total_votes.size):
        votes = total_votes[i]
        if votes > max:
            max = votes
            winners_indices = [i]
        elif votes == max:
            winners_indices.append(i)

    winners = []
    for i in winners_indices:
        winners.append(candidates[i])

    return winners


def alternative_votes(election_matrix):
    candidates = sorted(list(election_matrix.keys())[0])
    max_iteration = len(candidates) - 1

    for i in range(max_iteration):
        votes = {}
        for candidates_order, votes_number in election_matrix.items():
            i = 0
            while candidates_order[i] not in candidates:
                i += 1

            votes[candidates_order[i]] = votes.get(candidates_order[i], 0) + votes_number
        for candidate in candidates:
            if candidate not in votes.keys():
                votes[candidate] = 0
        losers = get_candidates_with_min_votes(votes)
        if len(losers) == len(candidates):
            return "can't determine!"
        for loser in losers:
            candidates.remove(loser)
        if len(candidates) == 1:
            return candidates[0]

    return "can't determine!"


if __name__ == '__main__':
    election_matrix = {
        ('a', 'b', 'c', 'd'): 3,
        ('c', 'a', 'b', 'd'): 4,
        ('b', 'a', 'c', 'd'): 4
    }

    print('relative majority method, winner: {}'.format(relative_majority(election_matrix)))
    print('condorce method, winner: {}'.format(condorce(election_matrix)))
    print('alternative votes method, winner: {}'.format(alternative_votes(election_matrix)))
