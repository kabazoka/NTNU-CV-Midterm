import numpy as np

def convolve(matrix, kernel):
    # Get the dimensions of the matrix and kernel
    matrix_rows, matrix_cols = matrix.shape
    kernel_rows, kernel_cols = kernel.shape
    
    # Calculate the padding needed for the matrix
    pad_rows = (kernel_rows - 1) // 2
    pad_cols = (kernel_cols - 1) // 2
    
    # Create a padded matrix
    padded_matrix = np.zeros((matrix_rows + pad_rows * 2, matrix_cols + pad_cols * 2))
    padded_matrix[pad_rows:-pad_rows, pad_cols:-pad_cols] = matrix
    
    # Create an output matrix
    output_matrix = np.zeros((matrix_rows, matrix_cols))
    
    # Perform convolution
    for i in range(matrix_rows):
        for j in range(matrix_cols):
            output_matrix[i, j] = (kernel * padded_matrix[i:i+kernel_rows, j:j+kernel_cols]).sum()
    
    return output_matrix

def main():
    matrix = np.array([[169, 180, 84, 233, 246, 102, 156, 235], 
                   [17, 247, 133, 71, 187, 42, 234, 59], 
                   [159, 165, 166, 97, 15, 68, 73, 150], 
                   [160, 184, 167, 157, 81, 96, 63, 81], 
                   [193, 114, 106, 27, 86, 8, 222, 194]])
    kernel = np.array([[-2, 1, 4], [-1, -1, 3], [-4, -4, 2]])
    output_matrix = convolve(matrix, kernel)
    print(output_matrix)
    scale_matrix(matrix)
    print(matrix)

def scale_matrix(matrix):
    # Find the minimum and maximum pixel values in the matrix
    min_val = np.min(matrix)
    max_val = np.max(matrix)
    
    # Calculate the divisor and offset
    divisor = max_val - min_val
    offset = min_val

    print(divisor, offset)
    
    # Scale the matrix to the range from 0 to 255 (8-bit Unsigned)
    scaled_matrix = (matrix - offset) * (255 / divisor)
    
    # Convert the matrix to 8-bit Unsigned
    scaled_matrix = scaled_matrix.astype(np.uint8)
    
    return scaled_matrix


main()