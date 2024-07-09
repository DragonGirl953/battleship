#### single player battle ship
import random

def board ():
    col1 = ["-"] * 5
    col2 = ["-"] * 5
    col3 = ["-"] * 5
    col4 = ["-"] * 5
    col5 = ["-"] * 5

    row = [col1, col2, col3, col4, col5]

    return row


def print_board(row):
    print("    A   B   C   D   E ")
    print("  ---------------------")
    print(f"1 | {row[0][0]} | {row[0][1]} | {row[0][2]} | {row[0][3]} | {row[0][4]} |")
    print("  ---------------------")
    print(f"2 | {row[1][0]} | {row[1][1]} | {row[1][2]} | {row[1][3]} | {row[1][4]} |")
    print("  ---------------------")
    print(f"3 | {row[2][0]} | {row[2][1]} | {row[2][2]} | {row[2][3]} | {row[2][4]} |")
    print("  ---------------------")
    print(f"4 | {row[3][0]} | {row[3][1]} | {row[3][2]} | {row[3][3]} | {row[3][4]} |")
    print("  ---------------------")
    print(f"5 | {row[4][0]} | {row[4][1]} | {row[4][2]} | {row[4][3]} | {row[4][4]} |")
    print("  ---------------------")


#### designates a location on the grid
def battleship_location():
    placement = False
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
    if ship_place == 1:
        out_of_bounds= True
        while out_of_bounds:
            win_coordinates = []
            single_coordinates = []
            direction_choice = random.randint(0,1)
            col = random.randint(0,4)
            row = random.randint(0,4)
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
            manual = input("Choose a location for the ship (Enter the coordinates in number, letter format eg. A,1): ")
            try:
                manual = manual.strip()
                win_coordinates = manual.split(",")
                if win_coordinates[0].lower() == "a":
                    win_coordinates[0] = 0
                elif win_coordinates[0].lower() == "b":
                    win_coordinates[0] = 1
                elif win_coordinates[0].lower() == "c":
                    win_coordinates[0] = 2
                elif win_coordinates[0].lower() == "d":
                    win_coordinates[0] = 3
                elif win_coordinates[0].lower() == "e":
                    win_coordinates[0] = 4
                else:
                    print("Invalid coordinates.")
                    continue
                try:
                    win_coordinates[1] = int(win_coordinates[1])
                    if win_coordinates[1] <= 5 and win_coordinates[1] >= 1:
                        win_coordinates[1] -= 1
                        valid_coordinates = True
                except:
                    print("Invalid coordinates.  Try again.")       

            except:
                continue  
    
    return win_coordinates


#### user puts in a location and it updates and prints the board
def user_choice(update_board, battleship_location):
    coordinates_list = board()
    win_coordinates = battleship_location()
    proper_coordinates = False
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
                    if individual_coordinates in win_coordinates:
                        update_board[individual_coordinates[1]][individual_coordinates[0]] = "X"
                        print_board(update_board)
                        print("You win!")
                        break
                    elif update_board[individual_coordinates[1]][individual_coordinates[0]] == "-":
                        update_board[individual_coordinates[1]][individual_coordinates[0]] = "O"
                        print_board(update_board)
                    
                    else:
                        print("Already choosen input another coordinate! ")
                    
                else:
                    print("Coordinates out of bounds.  Try again.")
                
            except:
                print("Invalid coordinates.  Try again.")       

        except:
            continue     
    return individual_coordinates


#### main
update_board = board()
print_board(update_board)
user_choice(update_board)
