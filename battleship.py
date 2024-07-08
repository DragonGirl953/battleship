#### single player battle ship

def board ():
    col1 = [""] * 5
    col2 = [""] * 5
    col3 = [""] * 5
    col4 = [""] * 5
    col5 = [""] * 5

    row = [col1, col2, col3, col4, col5]

    return row

def print_board(row):
    print("-------------")
    print(f"| {row[0][0]} | {row[0][1]} | {row[0][2]} | {row[0][3]} | {row[0][4]}")
    print("-------------")
    print(f"| {row[1][0]} | {row[1][1]} | {row[2][2]} | {row[3][3]} | {row[4][4]}")
    print("-------------")
    print(f"| {row[2][0]} | {row[2][1]} | {row[2][2]} | {row[2][3]} | {row[2][4]}")
    print("-------------")
    print(f"| {row[3][0]} | {row[3][1]} | {row[3][2]} | {row[3][3]} | {row[3][4]}")
    print("-------------")
    print(f"| {row[4][0]} | {row[4][1]} | {row[4][2]} | {row[4][3]} | {row[4][4]}")
    print("-------------")

update_board = board()
print_board(update_board)

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
                    print(individual_coordinates)
                    proper_coordinates = True
                    print(coordinates_list)
                else:
                    print("Coordinates out of bounds.  Try again.")
                
            except:
                print("Invalid coordinates.  Try again.")       

        except:
            continue     
    return individual_coordinates
