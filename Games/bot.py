print('Task-1')
import math

def evaluate_branch(level, node, maximize, scores, max_level, a, b):
    if level == max_level:
        return scores[node]

    if maximize:
        left_score = evaluate_branch(level + 1, node * 2, False, scores, max_level, a, b)
        right_score = evaluate_branch(level + 1, node * 2 + 1, False, scores, max_level, a, b)
        best_score = max(left_score, right_score)
        a = max(a, best_score)

        if a >= b:
            return best_score
        return best_score

    else:
        left_score = evaluate_branch(level + 1, node * 2, True, scores, max_level, a, b)
        right_score = evaluate_branch(level + 1, node * 2 + 1, True, scores, max_level, a, b)
        best_score = min(left_score, right_score)
        b = min(b, best_score)

        if a >= b:
            return best_score
        return best_score

def battle_simulation(first_player):
    leaf_nodes = 32
    match_scores = [1 if i % 2 == 0 else -1 for i in range(leaf_nodes)]
    depth = 5
    alpha = float('-inf')
    beta = float('inf')
    battle_results = []
    scorpion_victories = 0
    subzero_victories = 0
    active_turn = first_player

    for match in range(3):
        final_score = evaluate_branch(0, 0, active_turn == 1, match_scores, depth, alpha, beta)
        if final_score == 1:
            winner = "Sub-Zero"
        else:
            winner = "Scorpion"

        battle_results.append(f"Winner of Match {match + 1}: {winner}")
        if winner == "Scorpion":
            scorpion_victories += 1
        else:
            subzero_victories += 1

        active_turn = 1 - active_turn

    final_winner = "Scorpion" if scorpion_victories > subzero_victories else "Sub-Zero"

    print(f"Champion: {final_winner}")
    print(f"Total Matches: 3")
    for result in battle_results:
        print(result)

player = int(input("Who starts? (0 for Scorpion, 1 for Sub-Zero): "))
if player in [0, 1]:
    battle_simulation(player)
else:
    print("Invalid choice")


print("Task-2")

def strategic_evaluation(step, pos, is_max, values, limit, alpha, beta):
    if step == limit:
        return values[pos]

    if is_max:
        left = strategic_evaluation(step + 1, pos * 2, False, values, limit, alpha, beta)
        right = strategic_evaluation(step + 1, pos * 2 + 1, False, values, limit, alpha, beta)
        optimal = max(left, right)
        alpha = max(alpha, optimal)
        if alpha >= beta:
            return optimal
        return optimal

    else:
        left = strategic_evaluation(step + 1, pos * 2, True, values, limit, alpha, beta)
        right = strategic_evaluation(step + 1, pos * 2 + 1, True, values, limit, alpha, beta)
        optimal = min(left, right)
        beta = min(beta, optimal)
        if alpha >= beta:
            return optimal
        return optimal

def pacman_challenge(magic_cost):
    data = [3, 6, 2, 3, 7, 1, 2, 0]
    total_nodes = len(data)
    depth_limit = int(math.log2(total_nodes))
    alpha = float('-inf')
    beta = float('inf')

    base_score = strategic_evaluation(0, 0, True, data, depth_limit, alpha, beta)

    left_tree_max = max(
        strategic_evaluation(2, 0, True, data, depth_limit, alpha, beta),
        strategic_evaluation(2, 1, True, data, depth_limit, alpha, beta)
    )
    left_magic_score = left_tree_max - magic_cost

    right_tree_max = max(
        strategic_evaluation(2, 2, True, data, depth_limit, alpha, beta),
        strategic_evaluation(2, 3, True, data, depth_limit, alpha, beta)
    )
    right_magic_score = right_tree_max - magic_cost

    if max(left_magic_score, right_magic_score) > base_score:
        if right_magic_score >= left_magic_score:
            print(f"New score: {right_magic_score}. Pacman moves right and uses dark magic.")
        else:
            print(f"New score: {left_magic_score}. Pacman moves left and uses dark magic.")
    else:
        print(f"Score remains: {base_score}. Pacman avoids dark magic.")

magic_cost = int(input("Cost of using dark magic: "))
pacman_challenge(magic_cost)

