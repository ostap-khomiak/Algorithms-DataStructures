
def bubble_sort(nums):
    # Bubble sort algorithn
    # Time complexity: O(n^2)
    # Space complexity: O(1)
    for i in range(len(nums)):
        swapped = False
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if not swapped:
            break
    



nums = [3, 1, 2, 4, 6, 5]
bubble_sort(nums)
print(f"Sorted array: {nums}")
