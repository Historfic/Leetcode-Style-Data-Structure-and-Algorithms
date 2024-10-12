def max_sum_subarray(arr, k):
    max_sum = current_sum = sum(arr[:k])  # Initial window sum
    
    for i in range(k, len(arr)):
        current_sum += arr[i] - arr[i - k]  # Slide the window
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# How to call the function:
arr = [2, 1, 5, 1, 3, 2]
k = 3
result = max_sum_subarray(arr, k)
print(result)  # Output: 9 (The subarray [5, 1, 3] has the maximum sum)
