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