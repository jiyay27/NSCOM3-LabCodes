import numpy as np

def calculate_parity(data_block):
    # calculate row and col parity
    row_parity = np.mod(np.sum(data_block, axis=1), 2)
    col_parity = np.mod(np.sum(data_block, axis=0), 2)

    overall_parity = np.mod(np.sum(row_parity) + np.sum(col_parity), 2)

    return row_parity, col_parity, overall_parity


def display_parity_matrix(data_block, row_parity, col_parity, overall_parity):
    rows, cols = data_block.shape

    # new matrix with space for parity bits
    parity_matrix = np.zeros((rows + 1, cols + 1), dtype=int)

    parity_matrix[:rows, :cols] = data_block
    parity_matrix[:rows, cols] = row_parity
    parity_matrix[rows, :cols] = col_parity
    parity_matrix[rows, cols] = overall_parity

    print("Data Block with Parity:")
    print(parity_matrix)

    return parity_matrix


def introduce_error(parity_matrix):
    error_row = np.random.randint(0, parity_matrix.shape[0] - 1)
    error_col = np.random.randint(0, parity_matrix.shape[1] - 1)

    # flips a bit
    parity_matrix[error_row, error_col] = 1 - parity_matrix[error_row, error_col]
    
    print(f"Error introduced at row {error_row}, col {error_col}")
    return parity_matrix, error_row, error_col


def detect_and_correct_error(parity_matrix):
    rows, cols = parity_matrix.shape

    # extract the original data block and parities
    data_block = parity_matrix[:rows - 1, :cols - 1]
    row_parity = parity_matrix[:rows - 1, cols - 1]
    col_parity = parity_matrix[rows - 1, :cols - 1]
    overall_parity = parity_matrix[rows - 1, cols - 1]

    recalculated_row_parity, recalculated_col_parity, recalculated_overall_parity = calculate_parity(data_block)

    row_parity_mismatch = np.where(row_parity != recalculated_row_parity)[0]
    col_parity_mismatch = np.where(col_parity != recalculated_col_parity)[0]

    # Detect error
    if len(row_parity_mismatch) == 1 and len(col_parity_mismatch) == 1:
        error_row = row_parity_mismatch[0]
        error_col = col_parity_mismatch[0]
        print(f"Error detected at row {error_row}, col {error_col}. Correcting it.")
        # Correct the error
        parity_matrix[error_row, error_col] = 1 - parity_matrix[error_row, error_col]
    else:
        print("No single-bit error detected or unable to correct.")

    print("Corrected Data Block with Parity:")
    print(parity_matrix)

    return parity_matrix


def simulate_2d_parity_check():
    rows, cols = 4, 5  # Define the size of the data block
    data_block = np.random.randint(0, 2, (rows, cols))

    print("Original Data Block:")
    print(data_block)

    # calculate row, column, overall parity
    row_parity, col_parity, overall_parity = calculate_parity(data_block)

    # display data block with parity
    parity_matrix = display_parity_matrix(data_block, row_parity, col_parity, overall_parity)

    parity_matrix, error_row, error_col = introduce_error(parity_matrix)

    print("\nParity Matrix After Transmission (with error):")
    print(parity_matrix)

    detect_and_correct_error(parity_matrix)


simulate_2d_parity_check()
