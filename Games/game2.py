#TASK 1

depth = 5
b_factor = 2

utility_value = b_factor ** (depth - 1)
leaf_utilities = {}


for i in range(0,utility_value):
    if i%2 == 0:
        leaf_utilities[i] = 1
    else:
        leaf_utilities[i] = -1

def alpha_beta_pruning(node, depth, alpha, beta, is_maximizingPlayer, leaf_utilities):
    if depth == 0:
        return leaf_utilities[node]
    if is_maximizingPlayer:
        max_eval = float('-inf')
        for index in range(2):
            eval = alpha_beta_pruning(node, depth - 1, alpha, beta, False, leaf_utilities)
            node += 1
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for index in range(2):
            eval = alpha_beta_pruning(node, depth - 1, alpha, beta, True, leaf_utilities)
            node += 1
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def game_sim(starting_player, leaf_utilities):
    matches= []
    total_matches = 0
    current_player = starting_player

    for i in range(3):
        result= alpha_beta_pruning(0, 5, -float('inf'), float('inf'), current_player == 1, leaf_utilities)
        if result==1:
            round_winner="Sub-Zero"
        else:
            round_winner="Scorpion"

        matches.append(round_winner)
        current_player = 1-current_player

        scorpion_wins= matches.count("Scorpion")
        sub_zero_wins= matches.count("Sub-Zero")

        if scorpion_wins > sub_zero_wins:
            game_winner= "Scorpion"
        else:
            game_winner= "Sub-Zero"

    print(f"Game Winner: {game_winner}")
    print(f"Total rounds Played: 3")

    for i in range(3):
        print(f"Winner of Round {i+1}: {matches[i]}")

test= int(input())
if test==0 or test==1:
    game_sim(test, leaf_utilities)
else:
    print("Invalid input")


#TASK 2

def pacman_game(c):
    scores = [3, 6, 2, 3, 7, 1, 2, 0]

    def minimax(depth, is_maximizing_player, alpha, beta, score_index):
        if depth == 3:
            return scores[score_index]

        if is_maximizing_player:
            max_eval = float('-inf')
            for i in range(2):
                eval = minimax(depth + 1, False, alpha, beta, score_index * 2 + i)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for i in range(2):
                eval = minimax(depth + 1, True, alpha, beta, score_index * 2 + i)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    final_score_index = minimax(0, True, float('-inf'), float('inf'), 0)
    left_subtree_value = max(minimax(2, True, float('-inf'), float('inf'), 0),
                             minimax(2, True, float('-inf'), float('inf'), 1))
    left_value_with_magic = left_subtree_value - c

    right_subtree_value = max(minimax(2, True, float('-inf'), float('inf'), 2),
                              minimax(2, True, float('-inf'), float('inf'), 3))
    right_value_with_magic = right_subtree_value - c

    if max(left_value_with_magic, right_value_with_magic) > final_score_index:
        if right_value_with_magic >= left_value_with_magic:
            print(f"The new minimax value is {right_value_with_magic}. Pacman goes right and uses dark magic")
        else:
            print(f"The new minimax value is {left_value_with_magic}. Pacman goes left and uses dark magic")
    else:
        print(f"The new minimax value is {final_score_index}. Pacman does not use dark magic")


input1 = int(input())
pacman_game(input1)
