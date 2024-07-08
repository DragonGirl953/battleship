#### single player battle ship
import random

def board ():
    col1 = [""] * 5
    col2 = [""] * 5
    col3 = [""] * 5
    col4 = [""] * 5
    col5 = [""] * 5

    row = [col1, col2, col3, col4, col5]

    return row

def print_board(row):
    print("   A  B  C  D  E ")
    print("  ----------------")
    print(f"1 | {row[0][0]} | {row[0][1]} | {row[0][2]} | {row[0][3]} | {row[0][4]} |")
    print("  ----------------")
    print(f"2 | {row[1][0]} | {row[1][1]} | {row[1][2]} | {row[1][3]} | {row[1][4]} |")
    print("  ----------------")
    print(f"3 | {row[2][0]} | {row[2][1]} | {row[2][2]} | {row[2][3]} | {row[2][4]} |")
    print("  ----------------")
    print(f"4 | {row[3][0]} | {row[3][1]} | {row[3][2]} | {row[3][3]} | {row[3][4]} |")
    print("  ----------------")
    print(f"5 | {row[4][0]} | {row[4][1]} | {row[4][2]} | {row[4][3]} | {row[4][4]} |")
    print("  ----------------")



def battleship_location():
    win_coordinates = []
    col = random.randint(0,5)
    row = random.randint(0,5)
    win_coordinates.append(col)
    win_coordinates.append(row)
    return win_coordinates


#### user puts in a location and it updates and prints the board
def user_choice(battleship_location):
    coordinates_list = board()
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
                    if update_board[individual_coordinates[1]][individual_coordinates[0]] == "":
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