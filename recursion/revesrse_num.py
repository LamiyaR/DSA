nums = [2, 4, 1, 7, 6, 3, 9, 9, 5]

def func(arr, left, right):
    if left >= right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    func(arr, left + 1, right - 1)

def reverseArray(nums, l, r):
    func(nums, l, r)
    return nums

print(reverseArray(nums, 0, len(nums) - 1))
# [5, 9, 9, 3, 6, 7, 1, 4, 2]