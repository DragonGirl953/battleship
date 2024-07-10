#### single player battle ship
import random
import os

user_guesses = []
computer_guesses = []

#####computer board

def computer_board (grid_size):
    grid = [['-' for col in range(grid_size)] for row in range(grid_size)]
    
    return grid


def print_computerboard(grid):
    for i in range( grid_size):
        print('\n')
        for j in range( grid_size ):
           print("|", grid[i][j], end=" |")


##### user board
def user_board (grid_size):
    grid = [['=' for col in range(grid_size)] for row in range(grid_size)]
    
    return grid


def print_userboard(grid):
    for i in range( grid_size):
        print('\n')
        for j in range( grid_size ):
           print("|", grid[i][j], end=" |")



#### designates a location on the grid
def user_battleship_location():

    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    letters_available = letters[ 0 : grid_size]
    numbers_available = numbers[ 0 : grid_size]

    placement = False
    win_coordinates = []
    single_coordinates = []
    while not placement:
        try:
            print('\n')
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
    if ship_place == 1:
        out_of_bounds= True
        while out_of_bounds:
            win_coordinates.clear()
            #direction_choice = random.randint(0,1)
            col = random.randint(0,grid_size - 1)
            row = random.randint(0,grid_size - 1)
            single_coordinates.append(col)
            single_coordinates.append(row)
            win_coordinates.append(single_coordinates.copy())
            single_coordinates.clear()
            print(win_coordinates)
            out_of_bounds = False

            # if direction_choice == 0:
            #     if col-1 < 0 or col+1 > grid_size - 1:
            #         continue
            #     else:
            #         single_coordinates.append(col-1)
            #         single_coordinates.append(row)
            #         win_coordinates.append(single_coordinates.copy())
            #         single_coordinates.clear()
            #         single_coordinates.append(col+1)
            #         single_coordinates.append(row)
            #         win_coordinates.append(single_coordinates.copy())
            #         single_coordinates.clear()
            #         out_of_bounds = False
            #         print(win_coordinates)

                
            # elif direction_choice == 1:
            #     if row-1 < 0 or row+1 > grid_size - 1:
            #         continue
            #     else:
            #         single_coordinates.append(col)
            #         single_coordinates.append(row-1)
            #         win_coordinates.append(single_coordinates.copy())
            #         single_coordinates.clear()
            #         single_coordinates.append(col)
            #         single_coordinates.append(row+1)
            #         win_coordinates.append(single_coordinates.copy())
            #         single_coordinates.clear()  
            #         out_of_bounds = False
            #         print(win_coordinates)


    elif ship_place == 2:
        valid_coordinates = False
        while valid_coordinates == False:
            win_coordinates.clear()
            manual = input("Choose a location for the ship (Enter the coordinates in letter, number format eg. A,1): ")
            try:
                manual = manual.strip()
                single_coordinates = manual.split(",")
                single_coordinates[0] = single_coordinates[0].lower()
                if len(single_coordinates) == 1:
                    print("Please enter a column and row in letter, number format (A,1): ")
                else: 
                    if single_coordinates[0] in letters_available and single_coordinates[1] in numbers_available:
                        single_coordinates[0] = letters_available.index(single_coordinates[0])
                    else:
                        print("Enter a column and row in letter , number format! ")
                    
                col = single_coordinates[0]
                try:
                    single_coordinates[1] = int(single_coordinates[1])
                    if 0 < single_coordinates[1] <= grid_size :
                        single_coordinates[1] -= 1
                        row = single_coordinates[1]
                        win_coordinates.append(single_coordinates.copy())
                        single_coordinates.clear()
                except:
                    print("Invalid coordinates. Try again.")
                    continue

                #####
                
                # try:
                #     direction = int(input("Choose a direction for the ship (1 for vertical, 2 for horizontal): "))
                #     if direction == 1:
                #         if row-1 < 0 or row+1 > grid_size - 1:
                #             print("Coordinates out of bounds.  Try again.")
                #             continue
                #         else:
                #             single_coordinates.append(col)
                #             single_coordinates.append(row-1)
                #             win_coordinates.append(single_coordinates.copy())
                #             single_coordinates.clear()
                #             single_coordinates.append(col)
                #             single_coordinates.append(row+1)
                #             win_coordinates.append(single_coordinates.copy())
                #             single_coordinates.clear()  
                #             valid_coordinates = True
                #             print(win_coordinates)
                #     elif direction == 2:
                #         if col-1 < 0 or col+1 > grid_size - 1:
                #             print("Coordinates out of bounds.  Try again.")
                #             continue
                #         else:
                #             single_coordinates.append(col-1)
                #             single_coordinates.append(row)
                #             win_coordinates.append(single_coordinates.copy())
                #             single_coordinates.clear()
                #             single_coordinates.append(col+1)
                #             single_coordinates.append(row)
                #             win_coordinates.append(single_coordinates.copy())
                #             single_coordinates.clear()
                #             valid_coordinates = True
                #             print(win_coordinates)
                # except:
                #     print("Invalid input.")
                #     continue
                

            except:
                continue  
    return win_coordinates

def computer_battleship_location():
    win_coordinates = []
    single_coordinates = []
    out_of_bounds= True
    while out_of_bounds:
        win_coordinates.clear()
        direction_choice = random.randint(0,1)
        col = random.randint(0,grid_size - 1)
        row = random.randint(0,grid_size - 1)
        single_coordinates.append(col)
        single_coordinates.append(row)
        win_coordinates.append(single_coordinates.copy())
        single_coordinates.clear()

        # if direction_choice == 0:
        #     if col-1 < 0 or col+1 > grid_size - 1:
        #         continue
        #     else:
        #         single_coordinates.append(col-1)
        #         single_coordinates.append(row)
        #         win_coordinates.append(single_coordinates.copy())
        #         single_coordinates.clear()
        #         single_coordinates.append(col+1)
        #         single_coordinates.append(row)
        #         win_coordinates.append(single_coordinates.copy())
        #         single_coordinates.clear()
        #         out_of_bounds = False
        #         print(win_coordinates)

            
        # elif direction_choice == 1:
        #     if row-1 < 0 or row+1 > grid_size - 1:
        #         continue
        #     else:
        #         single_coordinates.append(col)
        #         single_coordinates.append(row-1)
        #         win_coordinates.append(single_coordinates.copy())
        #         single_coordinates.clear()
        #         single_coordinates.append(col)
        #         single_coordinates.append(row+1)
        #         win_coordinates.append(single_coordinates.copy())
        #         single_coordinates.clear()  
        out_of_bounds = False
        print(win_coordinates)
    return win_coordinates

#### user puts in a location and it updates and prints the board
def user_choice(update_board):

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    letters_available = letters[ 0 : grid_size]
    numbers_available = numbers[ 0 : grid_size]

    user_win_coordinates = user_battleship_location()
    computer_win_coordinates = computer_battleship_location()
    proper_coordinates = False
    win_counter = 0
    # This section of the function takes the user input of the coordinates and tries to separate it and turn it into an actual location on the board.
    while proper_coordinates == False:
        coordinates = input("Enter the coordinates for your guess (must be a letter, number format eg. A,1): ")
        
        try:
            coordinates_no_blanks = coordinates.strip()
            individual_coordinates = coordinates_no_blanks.split(",")
            individual_coordinates[0] = individual_coordinates[0].lower()
            if len(individual_coordinates) == 1:
                    print("Please enter a column and row in letter, number format (A,1): ")
            else: 
                if individual_coordinates[0] in letters_available and individual_coordinates[1] in numbers_available:
                        individual_coordinates[0] = letters_available.index(individual_coordinates[0])
                else:
                        print("Enter a column and row in letter , number format! ")
            
            try:
                individual_coordinates[1] = int(individual_coordinates[1])
                if 0 < individual_coordinates[1] <= grid_size :
                    individual_coordinates[1] -= 1
                    if individual_coordinates in computer_win_coordinates and update_board[individual_coordinates[1]][individual_coordinates[0]] == "-":
                        update_board[individual_coordinates[1]][individual_coordinates[0]] = "X"
                        user_guesses.append(individual_coordinates)
                        os.system('cls')
                        print_computerboard(update_board)
                        win_counter += 1
                        if win_counter == 3:
                            print("You win!")
                            break
                    elif update_board[individual_coordinates[1]][individual_coordinates[0]] == "-":
                        update_board[individual_coordinates[1]][individual_coordinates[0]] = "O"
                        user_guesses.append(individual_coordinates)
                        os.system('cls')
                        print_computerboard(update_board)
                        nextTurn = input("Press enter for the computers turn: ")
                        break
                    
                    else:
                        print("Already chosen input another coordinate! ")
                        

                    print(f"Your ship is located at {user_win_coordinates}.  Your ship has {3 - win_counter} spaces remaining.")
                    
                else:
                    print("Coordinates out of bounds.  Try again.")
                
            except:
                print("Invalid coordinates.  ffsfdfsdTry again.")       

        except:
            continue     
    return individual_coordinates

##### computer turn function
def computer_turn(update_board):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    letters_available = letters[ 0 : grid_size]
    numbers_available = numbers[ 0 : grid_size]
    compWin_counter = 0
    os.system('cls')

    #### PLACE HOLDER V
    compWin_cords = [1, 2]

    print_userboard(userupdate_board)
    print("Computer will now take a guess...")

    repeat = True
    while repeat == True:
        compCol = random.randint(0, grid_size - 1)
        compRow = random.randint(0, grid_size - 1)
        com_coordinates = (compRow, compCol)
        print(letters[compCol], ",", numbers[compRow])
        if userupdate_board[compRow][compCol] == "=":
            repeat = False

    if com_coordinates in compWin_cords:
        userupdate_board[compRow][compCol] = "X"
        computer_guesses.append(com_coordinates)
        print_userboard(userupdate_board)
        compWin_counter += 1
        if compWin_counter == 3:
            print("You win!")
    else:
        userupdate_board[compRow][compCol] = "O"
        computer_guesses.append(com_coordinates)
        print_userboard(userupdate_board)
            



#### main
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
    comupdate_board = computer_board(grid_size)
    userupdate_board = user_board(grid_size)
print("User Board: ")    
print_userboard(userupdate_board)
user_choice(comupdate_board)
computer_turn(userupdate_board)
