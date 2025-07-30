# reverse_array.py
"""
This module provides a function to reverse an array in place.
"""
def reverse_array(arr):
    """
    Reverses the given array in place.

    Parameters:
    arr (list): The array to be reversed.

    Returns:
    None: The function modifies the array in place.
    """
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

# Example usage:
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print("Original array:", arr)
    reverse_array(arr)
    print("Reversed array:", arr)
