
def binary_search(nums, target):
    # Binary search algorithm
    # Time complexity: O(log n)
    # Space complexity: O(1)
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1



nums = [3, 1, 2, 4, 6, 5]
target = 4
nums.sort()
result = binary_search(nums, target)
print(f"Element {target} found at index: {result}")