import numpy as np

def am_gm_inequality(numbers):
    numbers = np.array(numbers)
    
    if np.any(numbers <= 0):
        raise ValueError("All numbers must be positive for the geometric mean to be defined.")

    arithmetic_mean = np.mean(numbers)
    geometric_mean = np.exp(np.mean(np.log(numbers)))

    print(f"Numbers: {numbers}")
    print(f"Arithmetic Mean: {arithmetic_mean}")
    print(f"Geometric Mean: {geometric_mean}")
    print("AM ≥ GM:", arithmetic_mean >= geometric_mean)

am_gm_inequality([1, 3, 9])
