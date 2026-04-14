from idlelib.iomenu import errors


def input_grid():
    grid = []
    for i in range(9):
        userssudoko = int(input("Enter all numbers for row", (i + 1)))
        row_numbers = []

        for digit in row_numbers:
            row_numbers.append(int(digit))

        grid.append(row_numbers)

    return grid


def check_row(row_array):
    used = []
    for num in row_array:
        if num in used:
            return False
        if num < 1 or num > 9:
            return False
        used.append(num)
    return True


def check_column(grid, col_index):
    column = []
    for row in range(9):
        column.append(grid[row][col_index])
     return check_row(column)


def check_subgrid(grid, start_row, start_col):
    subgrid_numbers = []

    for r in range(start_row, start_row + 3):

        for c in range(start_col, start_col + 3):
            subgrid_numbers.append(grid[r][c])

    return check_row(subgrid_numbers)


def main():

    grid = input_grid()
    errors = 0
    rulesfailed = 0

    for i in range (9):
        if not check_row(grid[i]):
            errors += 1
            rulesfailed += 1

    for j in range (9):
        if not check_column(grid, j):
            errors += 1
            rulesfailed += 1

    for r in [0,3,6]:
        for c in [0,3,6]:
            if not check_subgrid(grid, r, c):
                errors += 1
                rulesfailed += 1

print("Valid Sudokosolution Checker")

if errors == 0:
    print("No errors")

else:
    print("Errors: ", errors)
    for rule in rulesfailed:
        print("Rule: ", rule)

        
