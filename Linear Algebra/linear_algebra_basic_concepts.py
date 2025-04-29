import numpy as np

def matrix_multiply(A, B):
    if A.shape[1] != B.shape[0]:
        raise ValueError("Number of columns in A must equal number of rows in B.")

    return np.dot(A, B)
# Example usage
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
result = matrix_multiply(A, B)
print(result) # [[19 22],[43 50]]



def are_vectors_linearly_independent(vectors):
    matrix = np.column_stack(vectors)
    
    rank = np.linalg.matrix_rank(matrix)
    return rank == len(vectors)
# Example usage
v1 = np.array([1, 2])
v2 = np.array([2, 4])  # Dependent on v1
v3 = np.array([0, 1])  # Independent from v1

print("v1 & v2 independent?", are_vectors_linearly_independent([v1, v2]))  # False
print("v1 & v3 independent?", are_vectors_linearly_independent([v1, v3]))  # True


def matrix_rank(matrix):
    return np.linalg.matrix_rank(matrix)

# Example usage
A = np.array([[1, 2], [2, 4]])  # Rank 1 (second row is a multiple of the first)
B = np.array([[1, 2], [3, 4]])  # Rank 2
print("Rank of A:", matrix_rank(A))  # 1
print("Rank of B:", matrix_rank(B))  # 2


def is_invertible(matrix):
    """
    Checks if a square matrix is invertible.
    """
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Matrix must be square to check invertibility.")
    
    return np.linalg.det(matrix) != 0
# Example usage
A = np.array([[1, 2], [3, 4]])       # Invertible (det ≠ 0)
B = np.array([[1, 2], [2, 4]])       # Not invertible (det = 0)

print("A is invertible:", is_invertible(A))  # True
print("B is invertible:", is_invertible(B))  # False


def are_orthogonal(v1, v2):
    v1 = np.array(v1)
    v2 = np.array(v2)
    
    dot_product = np.dot(v1, v2)
    
    return dot_product == 0

# Example usage:
v1 = [1, 2, 3]
v2 = [-2, 1, 0]

result = are_orthogonal(v1, v2)
print(f"Are the vectors orthogonal? {result}")