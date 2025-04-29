import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import svd
from skimage import io, color

def compress_image(image_path, k):
    """
    Compress an image using SVD by keeping only the top k singular values.

    Parameters:
    image_path (str): Path to the image file.
    k (int): Number of singular values to retain for compression.

    Returns:
    compressed_image (ndarray): The compressed image.
    """
    # Load the image
    image = io.imread(image_path)
    
    # Convert to grayscale if it's a color image
    if len(image.shape) == 3:
        image = color.rgb2gray(image)
    
    # Perform SVD on the image matrix
    U, S, Vt = svd(image, full_matrices=False)
    
    # Keep only the top k singular values
    U_k = U[:, :k]
    S_k = np.diag(S[:k])
    Vt_k = Vt[:k, :]
    
    # Reconstruct the compressed image
    compressed_image = np.dot(U_k, np.dot(S_k, Vt_k))
    
    return compressed_image

# Example usage
image_path = 'dog.jpg'  # Replace with your image path
k_values = [5, 50, 100]  # Different k values to see compression effects

# Plot original and compressed images
original_image = io.imread(image_path)
if len(original_image.shape) == 3:
    original_image = color.rgb2gray(original_image)

plt.figure(figsize=(10, 5))

# Plot original image
plt.subplot(1, len(k_values)+1, 1)
plt.imshow(original_image, cmap='gray')
plt.title("Original Image")
plt.axis('off')

# Plot compressed images for different k values
for i, k in enumerate(k_values, start=2):
    compressed_image = compress_image(image_path, k)
    plt.subplot(1, len(k_values)+1, i)
    plt.imshow(compressed_image, cmap='gray')
    plt.title(f"Compressed (k={k})")
    plt.axis('off')

plt.tight_layout()
plt.show()
