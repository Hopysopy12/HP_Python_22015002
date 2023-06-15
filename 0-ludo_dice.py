import random

players = ["Red", "Blue", "Green", "Yellow"]
tokens = {"Red": [0, 0, 0, 0], "Blue": [0, 0, 0, 0], "Green": [0, 0, 0, 0], "Yellow": [0, 0, 0, 0]}
board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

def print_board():
  print(board[0:11])
  print(board[11:22])
  print(board[22:33])
  print(board[33:44])
  print(board[44:55])
  print(board[55:66])
  print(board[66:77])

def get_valid_input():
  while True:
    command = input("Enter 'toss' to roll the dice, or 'quit' to exit: ")
    if command == "toss" or command == "quit":
      return command
    else:
      print("Invalid input. Try again.")

def move_token(player, token, steps):
  current_position = tokens[player][token]
  new_position = current_position + steps
  if new_position > 57:
    return False
  if board[new_position] != " ":
    if board[new_position] == player:
      return False
    else:
      other_player = board[new_position]
      tokens[other_player][board[new_position:].index(player)] = 0
      board[new_position] = player
      board[current_position] = " "
      tokens[player][token] = new_position
      return True
  else:
    board[new_position] = player
    board[current_position] = " "
    tokens[player][token] = new_position
    return True

def get_winner():
  for player in players:
    if tokens[player] == [58, 59, 60, 61]:
      return player
  return False

# Start the game loop
print("Welcome to Ludo Dice Game!")
while True:
  command = get_valid_input()
  if command == "quit":
    print("Thanks for playing!")
    break
  else:
    dice_roll = random.randint(1, 6)
    print("You rolled a", dice_roll)
    current_player = players[0]
    while True:
      if dice_roll == 6 and tokens[current_player].count(0) > 0:
        token_index = tokens[current_player].index(0)
        tokens[current_player][token_index] = 1
        board[1] = current_player
        print(current_player, "token", token_index, "was added to the board")
        break
      elif tokens[current_player] == [58, 59, 60, 61]:
        break
      else:
        available_tokens = [i for i, x in enumerate(tokens[current_player]) if x != 0]
        if len(available_tokens) == 0:
          break
        else:
          token_index = available_tokens[0]
          if move_token(current_player, token_index, dice_roll):
            print(current_player, "token", token_index, "moved to", tokens[current_player][token_index])
            break
          else:
            if len(available_tokens) == 1:
              print("No available moves.")
              break
            else:
              print("Token", token_index, "can't move. Trying next token...")
              available_tokens.pop(0)
    print_board()
    winner = get_winner()
    if winner:
      print("Congratulations,", winner, "wins!")
      break
    else:
      players.append(players.pop(0)) # rotate to next player
