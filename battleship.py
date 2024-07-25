#### single player battle ship
import random
import os

### initial list
alphabet = ["     A ", "    B ", "    C ", "    D ", "    E ", "    F ", "    G ", "    H ", "    I ", "    J "]

#### starts printing in white
print("\033[1;37m", end="")

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

#####computer board
def create_board (grid_size):
    grid = [['- ' for col in range(grid_size)] for row in range(grid_size)]
   
    return grid

#### prints the board
def print_board(grid):
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
def battleship_location():

    ship_counter = 0

    letters_available = []
    numbers_available = []
    ascii_number = 87
    for i in range(grid_size):
        letters_available.append(chr(grid_size + ascii_number))
        numbers_available.append(str(i + 1))
        ascii_number += 1
    
    placement = False
    userWin_coordinates = []
    compWin_coordinates = []
    single_coordinates = []
    tempWin_coordinates = []
    while not placement:
        try:
            ship_place = int(input("Would you like to place ships randomly or manually? 1 for random, 2 for manually: "))
            if ship_place == 1:
                os.system('cls')
                print("You selected random.")
                placement = True
            elif ship_place == 2:
                os.system('cls')
                print("You selected manually.")
                placement = True
            else:
                print("Invalid input.")
        except:
            print("Invalid input.")
    # This runs if random (1) is chosen; It generates random coordinates for the ship, appends them to userWin_coordinates, and prints them out for the user to see.
    if ship_place == 1:
        while ship_counter < 2:
            out_of_bounds= True
            while out_of_bounds:
                direction_choice = random.randint(0,1)
                col = random.randint(0,grid_size - 1)
                row = random.randint(0,grid_size - 1)
                single_coordinates.append(col)
                single_coordinates.append(row)
                if single_coordinates not in userWin_coordinates:
                    #### Vertical expansion of ship by one coordinate
                    if direction_choice == 0 and col + 1 <= grid_size - 1:
                        tempWin_coordinates.append(single_coordinates.copy())
                        single_coordinates[0] = col + 1
                        if single_coordinates not in userWin_coordinates:
                            userWin_coordinates.append(tempWin_coordinates[0].copy())
                            userWin_coordinates.append(single_coordinates.copy())
                            ship_counter += 1
                            single_coordinates.clear()
                            tempWin_coordinates.clear()
                            out_of_bounds = False 
                    #### Horizontal expansion of code
                    if direction_choice == 1 and row + 1 <= grid_size - 1:
                        tempWin_coordinates.append(single_coordinates.copy())
                        single_coordinates[1] = row + 1
                        if single_coordinates not in userWin_coordinates:
                            userWin_coordinates.append(tempWin_coordinates[0].copy())
                            userWin_coordinates.append(single_coordinates.copy())
                            ship_counter += 1
                            single_coordinates.clear()
                            tempWin_coordinates.clear()
                            out_of_bounds = False 
                single_coordinates.clear()
    # This runs if manual (2) is chosem; it prompts the user to enter coordinates in a number, letter format.
    elif ship_place == 2:
        while ship_counter < 2:
            valid_coordinates = False
            while valid_coordinates == False:
                print_board(comupdate_board)
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
                    # Prompts the user to choose the direction for the ship to be placed
                    try:
                        direction = int(input("Choose a direction for the ship (1 for vertical, 2 for horizontal): "))
                        #### Expands the battle ship in a vertical direction depending on user input
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
                                        print(userWin_coordinates)
                                        tempWin_coordinates.clear()
                                        single_coordinates.clear()
                                        valid_coordinates = True
                                        ship_counter += 1
                                    elif up_or_down == 2:
                                        single_coordinates.append(col)
                                        single_coordinates.append(row+1)
                                        if single_coordinates in userWin_coordinates:
                                            print("Battleship already placed here.  Choose another location.")
                                            single_coordinates.clear()
                                            continue
                                        userWin_coordinates.append(tempWin_coordinates[0].copy())
                                        userWin_coordinates.append(single_coordinates.copy())
                                        print(userWin_coordinates)
                                        tempWin_coordinates.clear()
                                        single_coordinates.clear()  
                                        valid_coordinates = True
                                        ship_counter += 1
                                    else:
                                        continue
                                except:
                                    continue
                        #### Expands battleship horizontally left or right depending on battleship location
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
                                        print(userWin_coordinates)
                                        tempWin_coordinates.clear()
                                        single_coordinates.clear()
                                        valid_coordinates = True
                                        ship_counter += 1
                                    elif left_or_right == 2:
                                        single_coordinates.append(col+1)
                                        single_coordinates.append(row)
                                        if single_coordinates in userWin_coordinates:
                                            print("Battleship already placed here.  Choose another location.")
                                            single_coordinates.clear()
                                            continue
                                        userWin_coordinates.append(tempWin_coordinates[0].copy())
                                        userWin_coordinates.append(single_coordinates.copy())
                                        print(userWin_coordinates)
                                        tempWin_coordinates.clear()
                                        single_coordinates.clear()
                                        valid_coordinates = True
                                        ship_counter += 1
                                    else:
                                        continue
                                except:
                                    continue
                    except:
                        print("Invalid input.")
                        continue
                except:
                    continue 
    # Randomly generates coordinates for the computer and prints them.
    ship_counter = 0
    while ship_counter < 2:
        out_of_bounds = True
        while out_of_bounds:
            direction_choice = random.randint(0,1)
            col = random.randint(0,grid_size - 1)
            row = random.randint(0,grid_size - 1)
            single_coordinates.append(col)
            single_coordinates.append(row)
            if single_coordinates not in compWin_coordinates:
                #### Vertical expansion of ship by one coordinate
                if direction_choice == 0 and col + 1 <= grid_size - 1:
                    tempWin_coordinates.append(single_coordinates.copy())
                    single_coordinates[0] = col + 1
                    if single_coordinates not in compWin_coordinates:
                        compWin_coordinates.append(tempWin_coordinates[0].copy())
                        compWin_coordinates.append(single_coordinates.copy())
                        ship_counter += 1
                        single_coordinates.clear()
                        tempWin_coordinates.clear()
                        out_of_bounds = False 
                #### Horizontal expansion of code
                if direction_choice == 1 and row + 1 <= grid_size - 1:
                    tempWin_coordinates.append(single_coordinates.copy())
                    single_coordinates[1] = row + 1
                    if single_coordinates not in compWin_coordinates:
                        compWin_coordinates.append(tempWin_coordinates[0].copy())
                        compWin_coordinates.append(single_coordinates.copy())
                        ship_counter += 1
                        single_coordinates.clear()
                        tempWin_coordinates.clear()
                        out_of_bounds = False 
                single_coordinates.clear()

    os.system('cls')
    print(ship_name1, "is at:", userWin_coordinates[0], userWin_coordinates[1])
    print(ship_name2, "is at:", userWin_coordinates[2], userWin_coordinates[3])
    print("Computer ship1 is at:", compWin_coordinates[0], compWin_coordinates[1])
    print("Computer ship2 is at:", compWin_coordinates[2], compWin_coordinates[3])
    return userWin_coordinates, compWin_coordinates


#### user puts in a location and it updates and prints the board
def coordinates (individual_coordinates, com_coordinates):

    # This section of the function takes the user input of the coordinates and tries to separate it and turn it into an actual location on the board.
    proper_coordinates = False
    while proper_coordinates == False:
        print("Number of hits: ", player_win_count)
        print("Computer ship1 is at:", compWin_coordinates[0], compWin_coordinates[1])
        print("Computer ship2 is at:", compWin_coordinates[2], compWin_coordinates[3])
        coordinates = input("Enter the coordinates for your guess (must be a letter, number format eg. A,1): ")
        
        try:
            coordinates_no_blanks = coordinates.strip()
            individual_coordinates = coordinates_no_blanks.split(",")
            individual_coordinates[0] = individual_coordinates[0].upper()
            individual_coordinates[1] = int(individual_coordinates[1])
            if len(individual_coordinates) == 1:
                    print("Please enter a column and row in letter, number format (A,1): ")
                    continue
            else: 
                individual_coordinates[0] = ord(individual_coordinates[0]) - 65
              
                if individual_coordinates[0] < 10 and 0 < individual_coordinates[1] < 11:
                    individual_coordinates[1] -= 1
                    print(f"Individual coordinate: {individual_coordinates}")
                    print(compWin_coordinates)
                else:
                        print("Enter a column and row in letter , number format! ")
                        continue
        except:
            print("Invalid coordinates.  Try again.")
            continue  

        proper_coordinates = True

    os.system('cls')
    

    ##### computer randomizes coordinates till one is available 
    repeat = True
    while repeat == True:
        compCol = random.randint(0, grid_size - 1)
        compRow = random.randint(0, grid_size - 1)
        com_coordinates = [compCol, compRow]
        if userupdate_board[compRow][compCol] == "- ":
            repeat = False

    return individual_coordinates, com_coordinates
    

########################## main
play_again = True
while play_again == True:
    battle_ship_art()
    placeholder = input("Press enter to start the game: ")
    os.system('cls')

    grid_size = 10     

    ### call and store functions in variable       
    comupdate_board = create_board(grid_size)
    userupdate_board = create_board(grid_size)

    #### naming of players ship
    ship_name1 = input("Name your first battleship: ")
    ship_name2 = input("Name your second battleship: ")

    individual_coordinates = []
    com_coordinates = []
    compCol = 0
    compRow = 0
    ship_list_name = {}
    computerShips = {}

    userWin_coordinates, compWin_coordinates = battleship_location()
    ship_list_name[ship_name1] = [userWin_coordinates[0], userWin_coordinates[1]]
    ship_list_name[ship_name2] = [userWin_coordinates[2], userWin_coordinates[3]]
    computerShips["ship1"] = [compWin_coordinates[0], compWin_coordinates[1]]
    computerShips["ship2"] = [compWin_coordinates[2], compWin_coordinates[3]]

    
    ###### repeats turn functions until one of them returns a win 
    play_repeat = True
    computer_repeat = True
    player_win_count = 0
    computer_win_count = 0
    playloop = 0
    while play_repeat == True and computer_repeat == True:
        
        if playloop == 0 :
            os.system('cls')
            print("Players Board: ")
            print_board(comupdate_board)
            individual_coordinates, com_coordinates = coordinates(individual_coordinates, com_coordinates)
            print("individ cords: ", individual_coordinates)
            print("com cords: ", com_coordinates)

            #### prints user hits or misses
           
            #### if user guess is a hit
            if individual_coordinates in compWin_coordinates and comupdate_board[individual_coordinates[1]][individual_coordinates[0]] == "- ":
                comupdate_board[individual_coordinates[1]][individual_coordinates[0]] = "X"
                # os.system('cls')
                print("Hit!")
                print("Users Board: ")
                print_board(comupdate_board)
                player_win_count += 1
                print("Hits: ", player_win_count)
                if player_win_count < 3:
                    if comupdate_board[computerShips["ship1"][0][1]][computerShips["ship1"][0][0]] == "X" and comupdate_board[computerShips["ship1"][1][1]][computerShips["ship1"][1][0]] == "X":
                        print("Computer ship1 has been sunken! ")
                    elif comupdate_board[computerShips["ship2"][0][1]][computerShips["ship2"][0][0]] == "X" and comupdate_board[computerShips["ship2"][1][1]][computerShips["ship2"][1][0]] == "X":
                        print("Computer ship2 has been sunken! ")
                if player_win_count == 4:
                    print("Both ships have been sunken! ")
                    quit()
                else:
                    print(f"Your ships are located at {ship_list_name[ship_name1][0]} {ship_list_name[ship_name1][1]} and {ship_list_name[ship_name2][0]} {ship_list_name[ship_name2][1]}.  Your ships have {4 - computer_win_count} spaces remaining.") 
                    nextTurn = input("Press enter for the computer's turn: ")
                    playloop += 1
                    continue
            #### if user guess is a miss
            elif comupdate_board[individual_coordinates[1]][individual_coordinates[0]] == "- ":
                comupdate_board[individual_coordinates[1]][individual_coordinates[0]] = "O"
                print("Miss")
                # os.system('cls')
                print("Users Board: ")
                print_board(comupdate_board)
                print(f"Your ships are located at {ship_list_name[ship_name1][0]} {ship_list_name[ship_name1][1]} and {ship_list_name[ship_name2][0]} {ship_list_name[ship_name2][1]}.  Your ships have {4 - computer_win_count} spaces remaining.") 
                nextTurn = input("Press enter for the computers turn: ")
                playloop += 1
                continue
            else:
                print("Already chosen input another coordinate! ")      
           
            
        

        if playloop == 1 :
           os.system('cls')
           print("Computers guess... ")

           compCol = com_coordinates[0]
           compRow = com_coordinates[1]
           print("com coordinate: ", chr(compCol +65) , ",", compRow + 1)

            #### when computer gets a hit
           if com_coordinates in ship_list_name[ship_name1] or com_coordinates in ship_list_name[ship_name2]:
                userupdate_board[compRow][compCol] = "X"
                print("Hit!")
                print_board(userupdate_board)
                computer_win_count += 1
                print(computer_win_count)
                if computer_win_count == 4:
                    print("Both ships sunk!")
                    quit()
                elif computer_win_count >= 2:
                     if userupdate_board[ship_list_name[ship_name1][0][1]][ship_list_name[ship_name1][0][0]] == "X" and userupdate_board[ship_list_name[ship_name1][1][1]][ship_list_name[ship_name1][1][0]] == "X":
                        print(f"{ship_name1} sunk!")
                     elif userupdate_board[ship_list_name[ship_name2][0][1]][ship_list_name[ship_name2][0][0]] == "X" and userupdate_board[ship_list_name[ship_name2][1][1]][ship_list_name[ship_name2][1][0]] == "X":
                        print(f"{ship_name2} sunk!")

            #### when computer misses
           else:
                userupdate_board[compRow][compCol] = "O"
                print("Miss!")
                print_board(userupdate_board)

           playloop -= 1
           placeholder = input("Press enter for Player Turn: ")

        os.system('cls')
        print("ergefwerergwg")