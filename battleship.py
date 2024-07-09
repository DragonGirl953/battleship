#### single player battle ship
import random

def board (grid_size):
    print(grid_size)
    grid = [[col for col in range(grid_size)] for row in range(grid_size)]
    
    print(grid)
    return grid


def print_board(grid):
    for i in range( grid_size):
        print('\n')
        for j in range( grid_size ):
           print("|", grid[i][j], end=" |")

#### designates a location on the grid
def battleship_location():
    win_coordinates = []
    col = random.randint(0,4)
    row = random.randint(0,4)
    win_coordinates.append(col)
    win_coordinates.append(row)
    
    return win_coordinates


#### user puts in a location and it updates and prints the board
def user_choice(update_board):
    coordinates_list = board(grid_size)
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
                    if individual_coordinates == win_coordinates:
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
grid_size = int(input("Please enter one number for your grid size: ")) 
update_board = board(grid_size)
print_board(update_board)
user_choice(update_board)
