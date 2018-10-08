def move_enemy():
    player_pos = get_player_pos(maze)
    enemies_pos = get_enemy_pos(maze) # Array of tuples of size num_enemies
    for e_pos in enemies_pos:
        moved = False
        # Move towards player pos
        if (not moved) and (e_pos[0] > player_pos[0]):
            # Move enemy down
            moved = move_enemy_down(maze, e_pos)
        if (not moved) and (e_pos[0] < player_pos[0]):
            # Move enemy up
            moved = move_enemy_up(maze, e_pos)
        if (not moved) and (e_pos[1] > player_pos[1]):
            # Move enemy left
            moved = move_enemy_left(maze, e_pos)
        if (not moved) and (e_pos[1] < player_pos[1]):
            # Move enemy right
            moved = move_enemy_right(maze, e_pos)

def move_enemy_up(maze, pos):
    # check if at top
    if (pos[0] == 0):
        return False
    up_pos = maze[pos[0]-1][pos[1]]
    if (up_pos == space):
        maze[pos[0]][pos[1]] = space
        maze[pos[0]-1][pos[1]] = enemy
        return True
    elif (up_pos == player):
        win_game(False)
    else:
        return False

def move_enemy_down(maze, pos):
    # check if at bottom
    if (pos[0] == get_maze_height(maze)-1):
        return False
    down_pos = maze[pos[0]+1][pos[1]]
    if (down_pos == space):
        maze[pos[0]][pos[1]] = space
        maze[pos[0]+1][pos[1]] = enemy
        return True
    elif (down_pos == player):
        win_game(False)
    else:
        return False

def move_enemy_left(maze, pos):
    # check if at leftmost
    if (pos[1] == 0):
        return False
    left_pos = maze[pos[0]][pos[1]-1]
    if (left_pos == space):
        maze[pos[0]][pos[1]] = space
        maze[pos[0]][pos[1]-1] = enemy
        return True
    elif (left_pos == player):
        win_game(False)
    else:
        return False

def move_enemy_right(maze, pos):
    # check if at rightmost
    if (pos[1] == get_maze_width(maze)-1):
        return False
    right_pos = maze[pos[0]][pos[1]+1]
    if (right_pos == space):
        maze[pos[0]][pos[1]] = space
        maze[pos[0]][pos[1]+1] = enemy
        return True
    elif (right_pos == player):
        win_game(False)
    else:
        return False
