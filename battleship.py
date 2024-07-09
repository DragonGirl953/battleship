#### single player battle ship
import random

user_guesses = []

def board (grid_size):
    grid = [['-' for col in range(grid_size)] for row in range(grid_size)]
    
    return grid


def print_board(grid):
    for i in range( grid_size):
        print('\n')
        for j in range( grid_size ):
           print("|", grid[i][j], end=" |")

#### designates a location on the grid
def battleship_location():
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
            col = random.randint(0,grid_size)
            row = random.randint(0,grid_size)
            single_coordinates.append(col)
            single_coordinates.append(row)
            win_coordinates.append(single_coordinates.copy())
            single_coordinates.clear()

            if direction_choice == 0:
                if col-1 < 0 or col+1 > 4:
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
                if row-1 < 0 or row+1 > 4:
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
            manual = input("Choose a location for the ship (Enter the coordinates in number, letter format eg. A,1): ")
            try:
                manual = manual.strip()
                single_coordinates = manual.split(",")
                if single_coordinates[0].lower() == "a":
                    single_coordinates[0] = 0
                elif single_coordinates[0].lower() == "b":
                    single_coordinates[0] = 1
                elif single_coordinates[0].lower() == "c":
                    single_coordinates[0] = 2
                elif single_coordinates[0].lower() == "d":
                    single_coordinates[0] = 3
                elif single_coordinates[0].lower() == "e":
                    single_coordinates[0] = 4
                else:
                    print("Invalid coordinates.")
                    continue
                col = single_coordinates[0]
                try:
                    single_coordinates[1] = int(single_coordinates[1])
                    if single_coordinates[1] <= 5 and single_coordinates[1] >= 1:
                        single_coordinates[1] -= 1
                        row = single_coordinates[1]
                        win_coordinates.append(single_coordinates.copy())
                        single_coordinates.clear()
                except:
                    print("Invalid coordinates. Try again.")
                    continue
                
                try:
                    direction = int(input("Choose a direction for the ship (1 for vertical, 2 for horizontal): "))
                    if direction == 1:
                        if row-1 < 0 or row+1 > 4:
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
                        if col-1 < 0 or col+1 > 4:
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
    limit = 10
    win_coordinates = battleship_location()
    proper_coordinates = False
    win_counter = 0
    # This section of the function takes the user input of the coordinates and tries to separate it and turn it into an actual location on the board.
    while proper_coordinates == False:
        coordinates = input("Enter the coordinates for your guess (must be a letter from A to E and a number from 1 to 5 in number, letter format eg. A,1): ")
        
        try:
            coordinates_no_blanks = coordinates.strip()
            individual_coordinates = coordinates_no_blanks.split(",")
            if individual_coordinates[0].lower() == "a":
                individual_coordinates[0] = 0
            elif individual_coordinates[0].lower() == "b":
                individual_coordinates[0] = 1
            elif individual_coordinates[0].lower() == "c":
                individual_coordinates[0] = 2
            elif individual_coordinates[0].lower() == "d":
                individual_coordinates[0] = 3
            elif individual_coordinates[0].lower() == "e":
                individual_coordinates[0] = 4
            else:
                print("Invalid coordinates.")
                continue
            
            try:
                individual_coordinates[1] = int(individual_coordinates[1])
                if individual_coordinates[1] <= 5 and individual_coordinates[1] >= 1:
                    individual_coordinates[1] -= 1
                    if individual_coordinates in win_coordinates and update_board[individual_coordinates[1]][individual_coordinates[0]] == "-":
                        update_board[individual_coordinates[1]][individual_coordinates[0]] = "X"
                        print_board(update_board)
                        win_counter += 1
                        if win_counter == 3:
                            print("You win!")
                            break
                    elif update_board[individual_coordinates[1]][individual_coordinates[0]] == "-":
                        update_board[individual_coordinates[1]][individual_coordinates[0]] = "O"
                        print_board(update_board)
                    
                    else:
                        print("Already chosen input another coordinate! ")
                        
                    if len(board) >= limit:
                        print("You are out of turns.")
                        break
                    else:
                        turns_left = limit - len(board)
                        print(f"{turns_left} guesses left.")
                    
                else:
                    print("Coordinates out of bounds.  Try again.")
                
            except:
                print("Invalid coordinates.  ffsfdfsdTry again.")       

        except:
            continue     
    return individual_coordinates


#### main
grid_size = int(input("Please enter one number for your grid size: ")) 
update_board = board(grid_size)
print_board(update_board)
user_choice(update_board)
