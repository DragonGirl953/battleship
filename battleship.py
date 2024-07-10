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
    grid = [['-' for col in range(grid_size)] for row in range(grid_size)]
    
    return grid


def print_userboard(grid):
    for i in range( grid_size):
        print('\n')
        for j in range( grid_size ):
           print("|", grid[i][j], end=" |")



#### designates a location on the grid
def battleship_location():

    
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
            direction_choice = random.randint(0,1)
            col = random.randint(0,grid_size - 1)
            row = random.randint(0,grid_size - 1)
            single_coordinates.append(col)
            single_coordinates.append(row)
            win_coordinates.append(single_coordinates.copy())
            single_coordinates.clear()

            if direction_choice == 0:
                if col-1 < 0 or col+1 > grid_size - 1:
                    continue
                else:
                    single_coordinates.append(col-1)
                    single_coordinates.append(row)
                    win_coordinates.append(single_coordinates.copy())
                    single_coordinates.clear()
                    single_coordinates.append(col+1)
                    single_coordinates.append(row)
                    win_coordinates.append(single_coordinates.copy())
                    single_coordinates.clear()
                    out_of_bounds = False
                    print(win_coordinates)

                
            elif direction_choice == 1:
                if row-1 < 0 or row+1 > grid_size - 1:
                    continue
                else:
                    single_coordinates.append(col)
                    single_coordinates.append(row-1)
                    win_coordinates.append(single_coordinates.copy())
                    single_coordinates.clear()
                    single_coordinates.append(col)
                    single_coordinates.append(row+1)
                    win_coordinates.append(single_coordinates.copy())
                    single_coordinates.clear()  
                    out_of_bounds = False
                    print(win_coordinates)


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
                
                try:
                    direction = int(input("Choose a direction for the ship (1 for vertical, 2 for horizontal): "))
                    if direction == 1:
                        if row-1 < 0 or row+1 > grid_size - 1:
                            print("Coordinates out of bounds.  Try again.")
                            continue
                        else:
                            single_coordinates.append(col)
                            single_coordinates.append(row-1)
                            win_coordinates.append(single_coordinates.copy())
                            single_coordinates.clear()
                            single_coordinates.append(col)
                            single_coordinates.append(row+1)
                            win_coordinates.append(single_coordinates.copy())
                            single_coordinates.clear()  
                            valid_coordinates = True
                            print(win_coordinates)
                    elif direction == 2:
                        if col-1 < 0 or col+1 > grid_size - 1:
                            print("Coordinates out of bounds.  Try again.")
                            continue
                        else:
                            single_coordinates.append(col-1)
                            single_coordinates.append(row)
                            win_coordinates.append(single_coordinates.copy())
                            single_coordinates.clear()
                            single_coordinates.append(col+1)
                            single_coordinates.append(row)
                            win_coordinates.append(single_coordinates.copy())
                            single_coordinates.clear()
                            valid_coordinates = True
                            print(win_coordinates)
                except:
                    print("Invalid input.")
                    continue
                

            except:
                continue  
    return win_coordinates


#### user puts in a location and it updates and prints the board
def user_choice(update_board):

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    letters_available = letters[ 0 : grid_size]
    numbers_available = numbers[ 0 : grid_size]

    limit = 10
    win_coordinates = battleship_location()
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
                    if individual_coordinates in win_coordinates and update_board[individual_coordinates[1]][individual_coordinates[0]] == "-":
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
                    
                    else:
                        print("Already chosen input another coordinate! ")
                        
                    if len(user_guesses) >= limit:
                        print("You are out of turns.")
                        break
                    else:
                        turns_left = limit - len(user_guesses)
                        print(f"{turns_left} guesses left.")

                    print(f"Your ship is located at {win_coordinates}.  Your ship has {3 - win_counter} spaces remaining.")
                    
                else:
                    print("Coordinates out of bounds.  Try again.")
                
            except:
                print("Invalid coordinates.  ffsfdfsdTry again.")       

        except:
            continue     
    return individual_coordinates


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
    update_board = computer_board(grid_size)
print_computerboard(update_board)
user_choice(update_board)
