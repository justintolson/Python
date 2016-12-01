import random

CELLS = [(0, 0), (0, 1), (0, 2), (0, 3),
         (1, 0), (1, 1), (1, 2), (1, 3),
         (2, 0), (2, 1), (2, 2), (2, 3),
         (3, 0), (3, 1), (3, 2), (3, 3),
         (4, 0), (4, 1), (4, 2), (4, 3)]


def get_locations():
    trap_door = random.choice(CELLS)
    monster = random.choice(CELLS)
    door = random.choice(CELLS)
    start = random.choice(CELLS)

    if monster == door or monster == start or door == start or trap_door == start:
        return get_locations()

    return trap_door, monster, door, start



def move_player(player, move):
    x, y = player

    if move == 'LEFT':
        y -= 1
    elif move == 'RIGHT':
        y += 1
    elif move == "UP":
        x -= 1
    elif move == 'DOWN':
        x += 1

    return x, y


def get_moves(player):
    moves = ['LEFT', 'RIGHT', "UP", 'DOWN']
    # player = (x, y)

    if player[1] == 0:
        moves.remove('LEFT')
    if player[1] == 3:
        moves.remove('RIGHT')
    if player[0] == 0:
        moves.remove('UP')
    if player[0] == 4:
        moves.remove('DOWN')

    return moves

def draw_map(player):
    print(' _ _ _')
    tile = '|{}'

    for idx, cell in enumerate(CELLS):
        if idx in [0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14, 16, 17, 18]:
            if cell == player:
                print(tile.format('X'), end='')
            else:
                print(tile.format('_'), end='')
        else:
            if cell == player:
                print(tile.format('X|'))
            else:
                print(tile.format('_|'))

trap_door, monster, door, player = get_locations()
print("Welcome to the dungeon!")
print("Enter QUIT to quit")
while True:
    moves = get_moves(player)

    print("You're currently in room {}".format(player))    # fill in with position

    draw_map(player)

    print("You can move {}".format(moves))    # fill in with available moves

    move = input("> ")
    move = move.upper()

    if move == 'QUIT':
        break

    if move in moves:
        player = move_player(player, move)
    else:
        print("** Walls are hard, stop walking into them! **")
        continue

    if player == door:
        print("You escaped!")
        break
    elif player == monster:
        print("You were eaten by the grue!")
        break
    elif player == trap_door:
        print("You have fallen through the trap door to your death!")
        break







