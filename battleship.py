#### single player battle ship
import random
import os

user_guesses = []
computer_guesses = []
alphabet = ["     A ", "    B ", "    C ", "    D ", "    E ", "    F ", "    G ", "    H ", "    I ", "    J "]

def battle_ship_art():

    print("                  _           _   _   _           _     _ ")
    print("                 | |         | | | | | |         | |   (_)")
    print("                 | |__   __ _| |_| |_| | ___  ___| |__  _ _ __")
    print("                 | '_ \\ / _` | __| __| |/ _ \\/ __| '_ \\| | '_ \\ ")
    print("                 | |_) | (_| | |_| |_| |  __/\\__ \\ | | | | |_) |")
    print("                 |_.__/ \\__,_|\\__|\\__|_|\\___||___/_| |_|_| .__/")
    print("                                                         | |  ")
    print("                                     |__                 |_|")                                 
    print("                                     |\\/")                                 
    print("                                     ---")                                 
    print("                                     / | [")                                 
    print("                              !      | |||")                          
    print("                            _/|     _/|-++'")                        
    print("                        +  +--|    |--|--|_ |-")                    
    print("                     { /|__|  |/\\__|  |--- |||__/")                            
    print("                    +---------------___[}-_===_.'____                 /\\ ")                           
    print("                ____`-' ||___-{]_| _[}-  |     |_[___\\==--            \\/   _")                       
    print(" __..._____--==/___]_|__|_____________________________[___\\==--____,------' .7")        
    print("|                                                                     BB-61/")       
    print(" \\_________________________________________________________________________|")        


#### starts printing in white
print("\033[1;37m", end="")

#####computer board
def computer_board (grid_size):
    grid = [['- ' for col in range(grid_size)] for row in range(grid_size)]
   
    return grid

def print_computerboard(grid):
    count = 0
    t = 0
    num = 1
    #### starts printing in cyan
    print("\033[0;36m", end="")

    for i in range(grid_size):
        print(alphabet[i], end=" ")
    print()
    for i in range(grid_size):
        if count > 0:
              print('\n')
        count += 1
        for j in range( grid_size ):
            if t == 0 or t % grid_size == 0:
                if grid[i][j] == "O":
                    print(num, "|", "\033[32m", grid[i][j], "\033[0;36m", end=" |")
                elif grid[i][j] == "X":
                    print(num, "|", "\033[0;31m", grid[i][j], "\033[0;36m", end=" |")
                else:
                    print(num, "|", "\033[0;36m", grid[i][j], end=" |")
                t += 1
                num += 1
            else:
                if grid[i][j] == "O":
                    print( "|", "\033[32m", grid[i][j], "\033[0;36m", end=" |")
                elif grid[i][j] == "X":
                    print( "|", "\033[0;31m", grid[i][j], "\033[0;36m", end=" |")
                else:
                    print( "|", "\033[0;36m", grid[i][j], end=" |")
                t += 1
    #### starts printing in white
    print("\033[1;37m", end="")
    print()

##### user board
def user_board (grid_size):
    grid = [['= ' for col in range(grid_size)] for row in range(grid_size)]
    
    return grid

def print_userboard(grid):
    count = 0
    t = 0
    num = 1
    
    #### starts printing in cyan
    print("\033[0;36m", end="")

    for i in range(grid_size):
        print(alphabet[i], end=" ")
    print()

    for i in range(grid_size):
        if count > 0:
              print('\n')
        count += 1
        for j in range( grid_size ):
           
            if t == 0 or t % grid_size == 0:
                if grid[i][j] == "O":
                    print(num, "|", "\033[32m", grid[i][j], "\033[0;36m", end=" |")
                elif grid[i][j] == "X":
                    print(num, "|", "\033[0;31m", grid[i][j], "\033[0;36m", end=" |")
                else:
                    print(num, "|", "\033[0;36m", grid[i][j], end=" |")
                t += 1
                num += 1
            else:
                if grid[i][j] == "O":
                    print( "|", "\033[32m", grid[i][j], "\033[0;36m", end=" |")
                elif grid[i][j] == "X":
                    print( "|", "\033[0;31m", grid[i][j], "\033[0;36m", end=" |")
                else:
                    print( "|", "\033[0;36m", grid[i][j], end=" |")
                t += 1
    #### starts printing in white
    print("\033[1;37m", end="")
    print()

#### designates a location on the grid whether random or manual with user input
def user_battleship_location():

    ship_count = 0
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    letters_available = letters[ 0 : grid_size]
    numbers_available = numbers[ 0 : grid_size]

    placement = False
    userWin_coordinates = []
    single_coordinates = []
    tempWin_coordinates = []
    while not placement:
        try:
            ship_place = int(input("Would you like to place ships randomly or manually? 1 for random, 2 for manually: "))
            if ship_place == 1:
                print("You selected random.")
                placement = True
            elif ship_place == 2:
                print("You selected manually.")
                placement = True
            else:
                print("Invalid input.")
        except:
            print("Invalid input.")
    # This runs if random (1) is chosen; It generates random coordinates for the ship, appends them to userWin_coordinates, and prints them out for the user to see.
    if ship_place == 1:
        while ship_count < 2:
            out_of_bounds= True
            while out_of_bounds:
                direction_choice = random.randint(0,1)
                col = random.randint(0,grid_size - 1)
                row = random.randint(0,grid_size - 1)
                single_coordinates.append(col)
                single_coordinates.append(row)
                if single_coordinates in userWin_coordinates:
                    single_coordinates.clear()
                    continue
                out_of_bounds = False
                #### Vertical expansion of ship by one coordinate
                if direction_choice == 0:
                    if col+1 > grid_size - 1:
                        single_coordinates.clear()
                        continue
                    else:
                        tempWin_coordinates.append(single_coordinates.copy())
                        single_coordinates.clear()
                        single_coordinates.append(col+1)
                        single_coordinates.append(row)
                        if single_coordinates in userWin_coordinates:
                            tempWin_coordinates.clear()
                            single_coordinates.clear()
                            continue
                        else:
                            userWin_coordinates.append(tempWin_coordinates[0].copy())
                            userWin_coordinates.append(single_coordinates.copy())
                            single_coordinates.clear()
                            tempWin_coordinates.clear()
                            out_of_bounds = False
                #### Horizontal expansion of code
                elif direction_choice == 1:
                    if row+1 > grid_size - 1:
                        single_coordinates.clear()
                        continue
                    else:
                        tempWin_coordinates.append(single_coordinates.copy())
                        single_coordinates.clear()
                        single_coordinates.append(col)
                        single_coordinates.append(row+1)
                        if single_coordinates in userWin_coordinates:
                            tempWin_coordinates.clear()
                            single_coordinates.clear()
                            continue
                        else:
                            userWin_coordinates.append(tempWin_coordinates[0].copy())
                            userWin_coordinates.append(single_coordinates.copy())
                            single_coordinates.clear()
                            tempWin_coordinates.clear()  
                            out_of_bounds = False
                ship_count += 1

    # This runs if manual (2) is chosem; it prompts the user to enter coordinates in a number, letter format.
    elif ship_place == 2:
        
        while ship_count < 2:
            valid_coordinates = False
            while valid_coordinates == False:
                # userWin_coordinates.clear()
                manual = input("Choose a location for the ship (Enter the coordinates in letter, number format eg. A,1): ")
                # Splits the user-entered coordinates and turns them into coordinates python can understand.  If it can't, makes the user re-enter the coordinates.
                try:
                    manual = manual.strip()
                    single_coordinates = manual.split(",")
                    single_coordinates[0] = single_coordinates[0].lower()
                    if len(single_coordinates) == 1:
                        print("Please enter a column and row in letter, number format (A,1): ")
                    else: 
                        if single_coordinates[0] in letters_available and single_coordinates[1] in numbers_available:
                            single_coordinates[0] = letters_available.index(single_coordinates[0])
                            valid_coordinates = True
                        else:
                            print("Enter a column and row in letter , number format! ")
                        
                    col = single_coordinates[0]
                    try:
                        single_coordinates[1] = int(single_coordinates[1])
                        if 0 < single_coordinates[1] <= grid_size :
                            single_coordinates[1] -= 1
                            row = single_coordinates[1]
                            if single_coordinates in userWin_coordinates:
                                print("Battleship already placed here.  Choose another location.")
                                single_coordinates.clear()
                                continue
                            tempWin_coordinates.append(single_coordinates.copy())
                            single_coordinates.clear()
                    except:
                        print("Invalid coordinates. Try again.")
                        continue

                    #####
                    
                    try:
                        direction = int(input("Choose a direction for the ship (1 for vertical, 2 for horizontal): "))
                        if direction == 1:
                            if row-1 < 0 or row+1 > grid_size - 1:
                                print("Coordinates out of bounds.  Try again.")
                                tempWin_coordinates.clear()
                                continue
                            else:
                                try:
                                    up_or_down = int(input("Would you like the ship to be placed up or down?(1 for up, 2 for down): "))
                                    if up_or_down == 1:
                                        single_coordinates.append(col)
                                        single_coordinates.append(row-1)
                                        if single_coordinates in userWin_coordinates:
                                            print("Battleship already placed here.  Choose another location.")
                                            single_coordinates.clear()
                                            continue
                                        userWin_coordinates.append(tempWin_coordinates[0].copy())
                                        userWin_coordinates.append(single_coordinates.copy())
                                        tempWin_coordinates.clear()
                                        single_coordinates.clear()
                                        valid_coordinates = True
                                        ship_count += 1
                                    elif up_or_down == 2:
                                        single_coordinates.append(col)
                                        single_coordinates.append(row+1)
                                        if single_coordinates in userWin_coordinates:
                                            print("Battleship already placed here.  Choose another location.")
                                            single_coordinates.clear()
                                            continue
                                        userWin_coordinates.append(tempWin_coordinates[0].copy())
                                        userWin_coordinates.append(single_coordinates.copy())
                                        tempWin_coordinates.clear()
                                        single_coordinates.clear()  
                                        valid_coordinates = True
                                        ship_count += 1
                                    else:
                                        continue
                                except:
                                    continue
                        elif direction == 2:
                            if col-1 < 0 or col+1 > grid_size - 1:
                                print("Coordinates out of bounds.  Try again.")
                                tempWin_coordinates.clear()
                                continue
                            else:
                                try:
                                    left_or_right = int(input("Would you like the ship to be placed to the left or right? (1 for left, 2 for right): "))
                                    if left_or_right == 1:
                                        single_coordinates.append(col-1)
                                        single_coordinates.append(row)
                                        if single_coordinates in userWin_coordinates:
                                            print("Battleship already placed here.  Choose another location.")
                                            single_coordinates.clear()
                                            continue
                                        userWin_coordinates.append(tempWin_coordinates[0].copy())
                                        userWin_coordinates.append(single_coordinates.copy())
                                        tempWin_coordinates.clear()
                                        single_coordinates.clear()
                                        valid_coordinates = True
                                        
                                        ship_count += 1
                                    elif left_or_right == 2:
                                        single_coordinates.append(col+1)
                                        single_coordinates.append(row)
                                        if single_coordinates in userWin_coordinates:
                                            print("Battleship already placed here.  Choose another location.")
                                            single_coordinates.clear()
                                            continue
                                        userWin_coordinates.append(tempWin_coordinates[0].copy())
                                        userWin_coordinates.append(single_coordinates.copy())
                                        tempWin_coordinates.clear()
                                        single_coordinates.clear()
                                        valid_coordinates = True
                                        
                                        ship_count += 1
                                    else:
                                        continue
                                except:
                                    continue
                    except:
                        print("Invalid input.")
                        continue
                    

                except:
                    continue 
    print("Your ship is at: ", userWin_coordinates)
    return userWin_coordinates

# Randomly generates coordinates for the computer and prints them.
def computer_battleship_location():
    tempWin_coordinates = []
    compWin_coordinates = []
    single_coordinates = []
    ship_counter = 0
    while ship_counter < 2:
        out_of_bounds= True
        while out_of_bounds:
            direction_choice = random.randint(0,1)
            col = random.randint(0,grid_size - 1)
            row = random.randint(0,grid_size - 1)
            single_coordinates.append(col)
            single_coordinates.append(row)
            if single_coordinates in compWin_coordinates:
                single_coordinates.clear()
                continue
            out_of_bounds = False

            if direction_choice == 0:
                if col+1 > grid_size - 1:
                    single_coordinates.clear()
                    continue
                else:
                    tempWin_coordinates.append(single_coordinates.copy())
                    single_coordinates.clear()
                    single_coordinates.append(col+1)
                    single_coordinates.append(row)
                    if single_coordinates in compWin_coordinates:
                        single_coordinates.clear()
                        tempWin_coordinates.clear()
                        continue
                    else:
                        compWin_coordinates.append(tempWin_coordinates[0].copy())
                        compWin_coordinates.append(single_coordinates.copy())
                        single_coordinates.clear()
                        tempWin_coordinates.clear()
                        ship_counter += 1
                        out_of_bounds = False

                
            elif direction_choice == 1:
                if row+1 > grid_size - 1:
                    single_coordinates.clear()
                    
                    continue
                else:
                    tempWin_coordinates.append(single_coordinates.copy())
                    single_coordinates.clear()
                    single_coordinates.append(col)
                    single_coordinates.append(row+1)                    
                    if single_coordinates in compWin_coordinates:
                        
                        single_coordinates.clear()
                        tempWin_coordinates.clear()
                        continue
                    else:
                        compWin_coordinates.append(tempWin_coordinates[0].copy())
                        compWin_coordinates.append(single_coordinates.copy())
                        tempWin_coordinates.clear()
                        single_coordinates.clear()
                        ship_counter += 1  
                        out_of_bounds = False
        
    print("Computers ships: ", compWin_coordinates)
    return compWin_coordinates

#### user puts in a location and it updates and prints the board
def user_turn(update_board, computer_win_coordinates, player_win_count):

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    letters_available = letters[ 0 : grid_size]
    numbers_available = numbers[ 0 : grid_size]
  
    print("Players Board: ")
    print_computerboard(comupdate_board)

    # This section of the function takes the user input of the coordinates and tries to separate it and turn it into an actual location on the board.
    proper_coordinates = False
    while proper_coordinates == False:
        print("Number of hits: ", player_win_count)
        coordinates = input("Enter the coordinates for your guess (must be a letter, number format eg. A,1): ")
        
        try:
            coordinates_no_blanks = coordinates.strip()
            individual_coordinates = coordinates_no_blanks.split(",")
            individual_coordinates[0] = individual_coordinates[0].lower()
            if len(individual_coordinates) == 1:
                    print("Please enter a column and row in letter, number format (A,1): ")
                    continue
            else: 
                if individual_coordinates[0] in letters_available and individual_coordinates[1] in numbers_available:
                        individual_coordinates[0] = letters_available.index(individual_coordinates[0])
                else:
                        print("Enter a column and row in letter , number format! ")
            #### prints user hits or misses
            try:
                individual_coordinates[1] = int(individual_coordinates[1])
                if 0 < individual_coordinates[1] <= grid_size :
                    individual_coordinates[1] -= 1
                    print(f"Individual coordinate: {individual_coordinates}")
                    if individual_coordinates in computer_win_coordinates and comupdate_board[individual_coordinates[1]][individual_coordinates[0]] == "- ":
                        comupdate_board[individual_coordinates[1]][individual_coordinates[0]] = "X"
                        user_guesses.append(individual_coordinates)
                        os.system('cls')
                        print("Hit!")
                        print("Users Board: ")
                        print_computerboard(comupdate_board)
                        player_win_count += 1
                        print("Hits: ", player_win_count)
                        if player_win_count == 4:
                            return False, player_win_count
                        else:
                            print(f"Your ship is located at {userWin_coordinates}.  Your ship is still alive.") 
                            nextTurn = input("Press enter for the computer's turn: ")
                            break
                    elif update_board[individual_coordinates[1]][individual_coordinates[0]] == "- ":
                        update_board[individual_coordinates[1]][individual_coordinates[0]] = "O"
                        user_guesses.append(individual_coordinates)
                        os.system('cls')
                        print("Miss")
                        print("Users Board: ")
                        print_computerboard(update_board)
                        print(f"Your ship is located at {userWin_coordinates}.  Your ship is still alive.") 
                        nextTurn = input("Press enter for the computers turn: ")
                        break
                    
                    else:
                        print("Already chosen input another coordinate! ")
                    
                else:
                    print("Coordinates out of bounds.  Try again.")
                
            except:
                print("Invalid coordinates. Try again.")       

        except:
            continue    
    return True, player_win_count

##### computer turn function
def computer_turn(userupdate_board, userWin_coordinates, win_counter):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    os.system('cls')

    print("Computer will now take a guess...")

    ##### computer randomizes coordinates till one is available 
    repeat = True
    while repeat == True:
        compCol = random.randint(0, grid_size - 1)
        compRow = random.randint(0, grid_size - 1)
        com_coordinates = [compRow, compCol]
        if userupdate_board[compRow][compCol] == "= ":
            repeat = False

    print(letters[compCol], ",", numbers[compRow])

    #### when computer gets a hit
    if com_coordinates in userWin_coordinates:
        userupdate_board[compRow][compCol] = "X"
        computer_guesses.append(com_coordinates)
        print("Hit!")
        print_userboard(userupdate_board)
        win_counter += 1
        if win_counter == 4:
            return False, win_counter
        else:
            placeholder = input("Press enter for Player Turn: ")
            return True, win_counter
    #### when computer misses
    else:
        userupdate_board[compRow][compCol] = "O"
        computer_guesses.append(com_coordinates)
        print("Miss!")
        print_userboard(userupdate_board)
        placeholder = input("Press enter for Player Turn: ")
        return True, win_counter
    
    



########################## main
play_again = True
while play_again == True:
    battle_ship_art()
    placeholder = input("Press enter to start the game: ")
    os.system('cls')

    ##### repeats until user inputs valid response
    repeat = True
    while(repeat):
        try:
            grid_size = int(input("Please enter a number between 4-10 for your grid size: ")) 
            if 3 < grid_size < 11:
                repeat = False
            else:
                print("Enter a number between 1-10! ")
        except:
            print("Invalid Syntax! ")
    ### call and store functions in variable       
    comupdate_board = computer_board(grid_size)
    userupdate_board = user_board(grid_size)

    #### naming of players ship
    ship_name1 = input("Name your first battleship: ")
    ship_name2 = input("Name your second battleship: ")
    # ship_list_name = ship_name1
    ship_list_name = {}

    userWin_coordinates = user_battleship_location()
    computer_win_coordinates = computer_battleship_location()
    ship_list_name[ship_name1] = [userWin_coordinates[0], userWin_coordinates[1]]
    ship_list_name[ship_name2] = [userWin_coordinates[2], userWin_coordinates[3]]
    print(ship_list_name)
    ###### repeats turn functions until one of them returns a win 
    user_repeat = True
    computer_repeat = True
    player_win_count = 0
    computer_win_count = 0
    while user_repeat == True and computer_repeat == True:
        user_repeat, player_win_count = user_turn(comupdate_board, computer_win_coordinates, player_win_count)
        if user_repeat == False:
            print("You win!")
            tryAgain = input("Press 0 to quit or anything else to play again: ")
            os.system('cls')
            if tryAgain == "0":
                play_again = False
            break
        computer_repeat, computer_win_count = computer_turn(userupdate_board, userWin_coordinates, computer_win_count)
        if computer_repeat == False:
            print("You lost.  Computer wins!")
            tryAgain = input("Press 0 to quit or anything else to play again: ")
            os.system('cls')
            if tryAgain == "0":
                play_again = False
            break
        os.system('cls')