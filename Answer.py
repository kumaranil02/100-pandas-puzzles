# Environment
# Here's a few tips to help you get started in the CodeSignal IDE:
# To customize the editor settings and see the editor hotkeys, check out the Settings tabon the left sidebar.

# See the README tab for more information about the environment and test run verdicts.

# If needed, you can hard reset the environment by clicking on the circular reset code icon () on the top right of the IDE. Note that your progress will not be saved, so please be careful when using this.

# Task
# Given a square matrix of size n ⨯ n containing integer values, your task is to return a list (let's call it result) of size n where result[i] equals to the sum of the maximum value in the ith row and the maximum value in the ith column of the matrix.

# Some skeleton code for the solution has already been created. You should only make edits under the # implement this sections. If you change any other part of the code, you will not be able to submit your solution.

# Example

# For

# matrix = [[ 2, 5,  8],
#           [ 1, 2,  10],
#           [-2, 0, -1]]
# the output should be solution(matrix) = [10, 15, 10].

# Explanation:

# The maximum value in the top row of the matrix is 8. The maximum value in the leftmost column of the matrix is 2. Therefore, result[0] = 8 + 2 = 10.
# The maximum value in the middle row of the matrix is 10. The maximum value in the middle column of the matrix is 5. Therefore, result[1] = 10 + 5 = 15.
# The maximum value in the bottom row of the matrix is 0. The maximum value in the rightmost column of the matrix is 10. Therefore, result[2] = 0 + 10 = 10.
# Input/Output

# [execution time limit] 4 seconds (py3)

# [memory limit] 1 GB

# [input] array.array.integer matrix

# A two-dimensional array of integers representing a square matrix.

# Guaranteed constraints:
# 1 ≤ matrix.length ≤ 100,
# matrix[i].length = matrix.length,
# -100 ≤ matrix[i][j] ≤ 100.

# [output] array.integer

import numpy as np
import numpy.typing as npt


def get_max_row_values(matrix: npt.NDArray[np.int64]) -> npt.NDArray[np.int64]:
    """
    Return a NumPy array containing the maximum value of each row of the given matrix.
    The i-th element of the result should correspond to the i-th row of the matrix.
    """
    # implement this
    return matrix[np.arange(matrix.shape[0]),np.argmax(matrix,axis=1)]


def get_max_column_values(matrix: npt.NDArray[np.int64]) -> npt.NDArray[np.int64]:
    """
    Return a NumPy array containing the maximum value of each column of the given matrix.
    The i-th element of the result should correspond to the i-th column of the matrix.
    """
    # implement this
    return matrix[np.argmax(matrix,axis=0),np.arange(matrix.shape[1])]


def solution(matrix: list[list[int]]) -> list[int]:
    np_matrix = np.array(matrix)
    return list(get_max_row_values(np_matrix) + get_max_column_values(np_matrix))
