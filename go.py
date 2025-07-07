# Write your solution here
def who_won(game_board: list):
    player_1_pts = 0
    player_2_pts = 0
    for row in game_board:
        for cell in row:
            if cell == 1:
                player_1_pts += 1
            elif cell == 2:
                player_2_pts += 1
    
    if player_1_pts > player_2_pts:
        return 1
    elif player_2_pts > player_1_pts:
        return 2
    else:
        return 0

