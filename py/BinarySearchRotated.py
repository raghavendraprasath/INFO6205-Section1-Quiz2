def binary_search_rotated(arr, target, rotation_index):
    """
    Perform binary search on a rotated sorted array.
    
    A rotated sorted array is an array that was initially sorted in ascending order
    but then rotated at a certain pivot index.
    
    Example:
    Original sorted array: [0, 1, 2, 4, 5, 6, 7]
    Rotated at index 4: [4, 5, 6, 7, 0, 1, 2]
    Here, the rotation index 4 means that the first four elements were moved to the end.
    
    :param arr: List[int] - The rotated sorted array.
    :param target: int - The number to search for.
    :param rotation_index: int - The index at which the array was rotated.
    :return: bool - True if the target is in the array, False otherwise.
    """
    
    # TODO: Check if the rotation_index is 0, meaning the array is not rotated.
    
    # TODO: Determine which half (before or after rotation_index) the target belongs to.
    
    def binary_search(arr, left, right, target):
 
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

    n = len(arr)
    
    # If the array is not rotated
    if rotation_index == 0:
        return binary_search(arr, 0, n - 1, target)

    # Determine which half (before or after rotation_index) the target belongs to
    if arr[0] <= target <= arr[rotation_index - 1]:
        return binary_search(arr, 0, rotation_index - 1, target)
    else:
        return binary_search(arr, rotation_index, n - 1, target)

