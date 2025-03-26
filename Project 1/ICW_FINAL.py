# Import necessary modules
import random
import datetime
from prettytable import PrettyTable as PT
import sys

# Main function to execute the program
def main():
    # Default dimensions
    num_rows = 5
    num_cols = 5

    # Check if user input is provided
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
        if 'x' in user_input:
            dimensions = user_input.split('x')
            if len(dimensions) == 2:
                try:
                    num_rows = int(dimensions[0])
                    num_cols = int(dimensions[1])
                    if not (3 <= num_rows <= 9 and 3 <= num_cols <= 9):
                        print("Error: Dimensions must be between '3x3' and '9x9'.")
                        return
                except ValueError:
                    print("Error: Invalid dimensions format.")
                    return
            else:
                print("Error: Invalid dimensions format.")
                return
        else:
            try:
                num_rows, num_cols = map(int, user_input.split())
                if not (3 <= num_rows <= 9 and 3 <= num_cols <= 9):
                    print("Error: Dimensions must be between '3 3' and '9 9'.")
                    return
            except ValueError:
                print("Error: Invalid input format.")
                return

    print(f"Valid dimensions: {num_rows}x{num_cols}")

    # Generate matrix based on user-specified or default dimensions
    matrix = generate_matrix(num_rows, num_cols)
    # Display the generated matrix
    display_matrix(matrix)
    # Check percolation in the matrix
    print(check_percolation(matrix))
    # Save the matrix and percolation data
    save_matrix(matrix)


# Function to generate a matrix with random values and empty cells
def generate_matrix(rows, cols, empty_prob=0.2):
    matrix = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            # Randomly decide whether to add a number or leave cell empty
            if random.random() > empty_prob:
                row.append(random.randint(10, 99))  # Add a random number
            else:
                row.append('')  # Add an empty cell
        matrix.append(row)
    return matrix

# Function to display the matrix using PrettyTable
def display_matrix(matrix):
    table = PT()
    table.header = False
    table.hrules = True
    table.vrules = True
    table.border = True
    for row in matrix:
        table.add_row(row)
    print(table)

    
# Function to check percolation in the matrix column-wise
def check_percolation(matrix):
    num_cols = len(matrix[0])
    statuses = []
    for col in range(num_cols):
        percolates = True
        for row in matrix:
            # Check if cell in the current column is empty
            if row[col] == '':
                percolates = False  # Matrix doesn't percolate in this column
                break
        statuses.append("OK" if percolates else "NO")  # Add status for the column
    
    # Format the statuses for display
    max_status_width = max(map(len, statuses))
    formatted_statuses = [f"{status:{max_status_width}}" for status in statuses]
    return " ".join(formatted_statuses)


# Function to save the matrix and percolation data to files
def save_matrix(matrix):
    current_date_time = datetime.datetime.now().strftime("%Y_%m_%d_%H%M")
    text_file_name = f"{current_date_time}.txt"  # Generate unique text file name
    html_file_name = f"{current_date_time}.html"  # Generate unique HTML file name

    with open(text_file_name, "w") as txt_file, open(html_file_name, "w") as html_file:
        html_file.write("<pre>\n")
        for row in matrix:
            txt_file.write(" ".join(str(cell) for cell in row) + "\n")  # Write matrix to text file
            html_file.write(" ".join(str(cell) for cell in row) + "<br>\n")  # Write matrix to HTML file
        txt_file.write(check_percolation(matrix))  # Write percolation data to text file
        html_file.write(check_percolation(matrix).replace(" ", "&nbsp;"))  # Write percolation data to HTML file
        html_file.write("\n</pre>")

    print("Matrix and percolation data saved as", text_file_name, "and", html_file_name)

    
# Entry point of the program

main()
