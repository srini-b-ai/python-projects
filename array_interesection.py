# get intersection of two arrays
def array_intersection(arr1, arr2):
	# Return the intersection of two arrays as a list
	return list(set(arr1) & set(arr2))

# Example usage:
if __name__ == "__main__":
	arr1 = [1, 2, 3, 4]
	arr2 = [3, 4, 5, 6]
	print(array_intersection(arr1, arr2))
	    # Output: [3, 4]