print('Task-1')
import math

def alpha_beta_pruning(curDepth, nodeIndex, maxTurn, scores, targetDepth, alpha, beta):
    if curDepth == targetDepth:
        return scores[nodeIndex]

    if maxTurn:
        left_child_value = alpha_beta_pruning(curDepth + 1, nodeIndex * 2, False, scores, targetDepth, alpha, beta)
        right_child_value = alpha_beta_pruning(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth, alpha, beta)

        max_value = max(left_child_value, right_child_value)
        alpha = max(alpha, max_value)

        if beta <= alpha:
            return max_value
        return max_value

    else:
        left_child_value = alpha_beta_pruning(curDepth + 1, nodeIndex * 2, True, scores, targetDepth, alpha, beta)
        right_child_value = alpha_beta_pruning(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth, alpha, beta)

        min_value = min(left_child_value, right_child_value)
        beta = min(beta, min_value)

        if beta <= alpha:
            return min_value
        return min_value

def mortal_kombat(starting_player):
    num_leaves = 32
    scores = [1 if i % 2 == 0 else -1 for i in range(num_leaves)]
    treeDepth = 5
    alpha = -math.inf
    beta = math.inf
    rounds = []
    scorpion_wins = 0
    sub_zero_wins = 0
    current_player = starting_player

    for round_num in range(3):
        result = alpha_beta_pruning(0, 0, current_player, scores, treeDepth, alpha, beta)
        if result == 1:
            round_winner = "Sub-Zero"
        else:
            round_winner = "Scorpion"

        rounds.append(f"Winner of Round {round_num + 1}: {round_winner}")
        if round_winner == "Scorpion":
            scorpion_wins += 1
        else:
            sub_zero_wins += 1

        current_player = 1 - current_player

    if scorpion_wins > sub_zero_wins:
        game_winner = "Scorpion"
    
    else :
        game_winner="Sub-Zero"

    print(f"Game Winner: {game_winner}")
    print(f"Total Rounds Played: 3")
    for result in rounds:
        print(result)

starting_player = int(input("Enter the starting player (0 for Scorpion, 1 for Sub-Zero): "))
if starting_player in [0, 1]:
    mortal_kombat(starting_player)
else:
    print("Invalid input")


print("Task-2")

def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth, alpha, beta):
    if curDepth == targetDepth:
        return scores[nodeIndex]

    if maxTurn:
        left_child_value = minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth, alpha, beta)
        right_child_value = minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth, alpha, beta)

        max_value = max(left_child_value, right_child_value)
        alpha = max(alpha, max_value)
        if beta <= alpha:
            return max_value
        return max_value

    else:
        left_child_value = minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth, alpha, beta)
        right_child_value = minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth, alpha, beta)

        min_value = min(left_child_value, right_child_value)
        beta = min(beta, min_value)
        if beta <= alpha:
            return min_value
        return min_value

def pacman_game(c):
    scores = [3, 6, 2, 3, 7, 1, 2, 0]  
    num_leaves = len(scores)
    treeDepth = int(math.log2(num_leaves))
    alpha = -math.inf
    beta = math.inf

    without_magic_value = minimax(0, 0, True, scores, treeDepth, alpha, beta)

    left_subtree_value = max(
        minimax(2, 0, True, scores, treeDepth, alpha, beta),
        minimax(2, 1, True, scores, treeDepth, alpha, beta)
    )
    left_value_with_magic = left_subtree_value - c

    right_subtree_value = max(
        minimax(2, 2, True, scores, treeDepth, alpha, beta),
        minimax(2, 3, True, scores, treeDepth, alpha, beta)
    )
    right_value_with_magic = right_subtree_value - c

    if max(left_value_with_magic, right_value_with_magic) > without_magic_value:
        if right_value_with_magic >= left_value_with_magic:
            print(f"The new minimax value is {right_value_with_magic}. Pacman goes right and uses dark magic.")
        else:
            print(f"The new minimax value is {left_value_with_magic}. Pacman goes left and uses dark magic.")
    else:
        print(f"The minimax value is {without_magic_value}. Pacman does not use dark magic.")

c = int(input("Enter the cost of using dark magic (c): "))
pacman_game(c)
