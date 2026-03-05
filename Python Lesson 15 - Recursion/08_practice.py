# Binary search (recursive)
def binary_search(arr, target, low, high):
    if low > high:
        return -1  # Target not found
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid  # Target found at index mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)  # Search in the left half
    else:
        return binary_search(arr, target, mid + 1, high)  # Search in the right half
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = int(input("Enter a number to search: "))
result = binary_search(arr, target, 0, len(arr) - 1)
if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")