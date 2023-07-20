def find_winner(candidates):
    vote_count = {}

    for candidate in candidates:
        if candidate in vote_count:
            vote_count[candidate] += 1
        else:
            vote_count[candidate] = 1

    max_votes = max(vote_count.values())

    winners = [candidate for candidate, votes in vote_count.items() if votes == max_votes]

    winners.sort()

    for winner in winners:
        print(winner)

candidates = ['Alice', 'Bob', 'Charlie', 'Bob', 'Alice', 'Charlie', 'Alice']
find_winner(candidates)
