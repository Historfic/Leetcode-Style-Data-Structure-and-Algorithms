def two_sum_sorted(arr, target):
    # Initialize two pointers, one at the start and the other at the end
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return [left, right]  # Return the indices of the two numbers
        
        elif current_sum < target:
            left += 1  # Move the left pointer to the right
        else:
            right -= 1  # Move the right pointer to the left
    
    return []  # If no pair is found

# How to call the function:
arr = [1, 2, 3, 4, 6]
target = 6
result = two_sum_sorted(arr, target)
print(result)  # Output: [1, 3] (Since 2 + 4 = 6)
