
def linear_search(nums, target):
    # Linear search algorithm
    # Time complexity: O(n)
    # Space complexity: O(1)

    for i in range(len(nums)):
        if nums[i] == target:
            return i  

    return -1


nums = [3, 1, 2, 4, 6, 5]
target = 4
result = linear_search(nums, target)
print(f"Element {target} found at index: {result}")  

