import sys
from itertools import permutations


def baseball_simulation(game):
    inning_count = len(game)
    lineup = [i for i in range(1, 9)]
    max_score = 0

    for x in permutations(lineup, 8):
        x = list(x)
        batting_order = x[:3] + [0] + x[3:]
        player_number, score = 0, 0

        for inning in range(inning_count):
            out = 0
            base1 = base2 = base3 = 0

            while out < 3:
                hit_result = game[inning][batting_order[player_number]]

                if hit_result == 0:
                    out += 1
                elif hit_result == 1:
                    score += base3
                    base1, base2, base3 = 1, base1, base2
                elif hit_result == 2:
                    score += base2 + base3
                    base1, base2, base3 = 0, 1, base1
                elif hit_result == 3:
                    score += base1 + base2 + base3
                    base1, base2, base3 = 0, 0, 1
                elif hit_result == 4:
                    score += base1 + base2 + base3 + 1
                    base1, base2, base3 = 0, 0, 0
                player_number += 1
                if player_number == 9:
                    player_number = 0

        max_score = max(max_score, score)

    return max_score


inning_count = int(input())
game = [list(map(int, input().split())) for _ in range(inning_count)]
max_score = baseball_simulation(game)
print(max_score)
