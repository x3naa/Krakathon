from os import system, name
import sys
import random
import msvcrt
from numpy.random import random_integers as rand

player = "@"
block = "#"
space = " "
exitt = "X"
enemy = "&"

num_enemies = 3

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def draw_maze(maze):
    clear()
    for i in range(0, len(maze)):
        for j in range(0, len(maze[i])):
            print(maze[i][j], end='')

def read_maze(filename):
    maze = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for i in range(0, len(lines)): # for each line
            maze.append([])
            line = lines[i]
            for j in range(0, len(line)): # for each char in line
                maze[i].append(line[j])
    return maze

def set_starting_pos(maze, character):
    got_it = False
    while (not got_it):
        x = random.randint(0, get_maze_width(maze)-1)
        y = random.randint(0, get_maze_height(maze)-1)
        if (maze[y][x] == space):
            maze[y][x] = character
            got_it = True

def get_player_pos(maze):
    for i in range(0, len(maze)):
        for j in range(0, len(maze[i])):
            if maze[i][j] == player:
                return (i,j)

def get_enemy_pos(maze):
    enemies_pos = []
    for i in range(0, len(maze)):
        for j in range(0, len(maze[i])):
            if maze[i][j] == enemy:
                enemies_pos.append((i,j))
    return enemies_pos

def get_maze_height(maze):
    return len(maze)

def get_maze_width(maze):
    return len(maze[0])

def win_game(win = True):
    clear()
    if (win):
        print("Game Over. You Win !")
    else:
        print("Game Over. You Lose !")
    sys.exit()

def move_player(maze):
    valid = False
    while (not valid):
        # inp = input('')[0].lower()
        inp = msvcrt.getwche()
        print(inp)
        if (inp in ['w','a','s','d']):
            valid = True
            if inp == 'w':
                move_up(maze)
            elif inp == 'a':
                move_left(maze)
            elif inp == 'd':
                move_right(maze)
            elif inp == 's':
                move_down(maze)
            move_enemy(maze)
        if inp == 'x':
            sys.exit()

def move_up(maze):
    pos = get_player_pos(maze)
    # check if at top
    if (pos[0] == 0):
        return
    up_pos = maze[pos[0]-1][pos[1]]
    if (up_pos == space):
        maze[pos[0]][pos[1]] = space
        maze[pos[0]-1][pos[1]] = player
    elif (up_pos == block):
        if(pos[0] == 1):
            return
        block_up = maze[pos[0]-2][pos[1]]
        if (block_up == space):
            maze[pos[0]][pos[1]] = space
            maze[pos[0]-1][pos[1]] = player
            maze[pos[0]-2][pos[1]] = block
    elif (up_pos == enemy):
        win_game(False)
    elif (up_pos == exitt):
        win_game()
    else:
        return

def move_down(maze):
    pos = get_player_pos(maze)
    # check if at bottom
    if (pos[0] == get_maze_height(maze)-1):
        return
    down_pos = maze[pos[0]+1][pos[1]]
    if (down_pos == space):
        maze[pos[0]][pos[1]] = space
        maze[pos[0]+1][pos[1]] = player
    elif (down_pos == block):
        if (pos[0] == get_maze_height(maze)-2):
            return
        block_down = maze[pos[0]+2][pos[1]]
        if(block_down == space):
            maze[pos[0]][pos[1]] = space
            maze[pos[0]+1][pos[1]] = player
            maze[pos[0]+2][pos[1]] = block
    elif (down_pos == enemy):
        win_game(False)
    elif (down_pos == exitt):
        win_game()
    else:
        return

def move_left(maze):
    pos = get_player_pos(maze)
    # check if at leftmost
    if (pos[1] == 0):
        return
    left_pos = maze[pos[0]][pos[1]-1]
    if (left_pos == space):
        maze[pos[0]][pos[1]] = space
        maze[pos[0]][pos[1]-1] = player
    elif (left_pos == block):
        if(pos[1] == 1):
            return
        block_left = maze[pos[0]][pos[1]-2]
        if (block_left == space):
            maze[pos[0]][pos[1]] = space
            maze[pos[0]][pos[1]-1] = player
            maze[pos[0]][pos[1]-2] = block
    elif (left_pos == enemy):
        win_game(False)
    elif (left_pos == exitt):
        win_game()
    else:
        return

def move_right(maze):
    pos = get_player_pos(maze)
    # check if at rightmost
    if (pos[1] == get_maze_width(maze)-1):
        return
    right_pos = maze[pos[0]][pos[1]+1]
    if (right_pos == space):
        maze[pos[0]][pos[1]] = space
        maze[pos[0]][pos[1]+1] = player
    elif (right_pos == block):
        if(pos[1] == get_maze_width(maze)-2):
            return
        block_right = maze[pos[0]][pos[1]+2]
        if(block_right == space):
            maze[pos[0]][pos[1]] = space
            maze[pos[0]][pos[1]+1] = player
            maze[pos[0]][pos[1]+2] = block
    elif (right_pos == enemy):
        win_game(False)
    elif (right_pos == exitt):
        win_game()
    else:
        return

def move_enemy(maze):
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



def main():
    # Read Maze
    maze = read_maze("labyrinthe.txt")

    # TODO: Generate Maze
    # maze = generate_maze(height, width)

    # Find starting pos
    set_starting_pos(maze, player)
    for i in range(0, num_enemies):
        set_starting_pos(maze, enemy)

    draw_maze(maze)

    # Play Game
    while True:
        # Get Move
        move_player(maze)
        # Clear and redraw maze
        draw_maze(maze)

if __name__ == "__main__":
    main()