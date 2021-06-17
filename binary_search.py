# comprehensively understanding different version of binary search


# scenario A
def binary_search_a(nums, target):
    n = 0
    left = 0
    right = len(nums) - 1
    while left <= right:
        n += 1
        mid = (left + right) // 2
        display(nums, left, mid, right, target, n)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


# scenario B
def binary_search_b(nums, target):
    n = 0
    left = 0
    right = len(nums)
    while left < right:
        n += 1
        mid = (left + right) // 2
        display(nums, left, mid, right, target, n)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid
        else:
            left = mid + 1
    return -1


# scenario C
def binary_search_c(nums, target):
    n = 0
    left = 0
    right = len(nums) - 1
    while left + 1 < right:
        n += 1
        mid = (left + right) // 2
        display(nums, left, mid, right, target, n)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid
        else:
            left = mid
    if nums[left] == target:
        return left
    if nums[right] == target:
        return right
    return -1


# binary insert (from binary search a)
def binary_insert(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left


# display function
def display(arr, left, mid, right, target, n):
    c = (4 * len(arr) - 3) // 2
    print("-" * c, n, "-" * c)
    t = arr.index(target)
    print("\t" * t + "t")
    for num in arr[:-1]:
        print(num, end="\t")
    print(arr[-1])
    print("\t" * left + "l" + "\t" * (mid - left) + "m" + "\t" * (right - mid) + "r")


if __name__ == '__main__':
    arr_a = [1, 3, 5, 6, 9, 12]
    arr_b = [1, 3, 5, 6, 9]
    binary_search_a(arr_a, 3)
    print("====" * len(arr_a))
    binary_search_b(arr_a, 3)
    print("====" * len(arr_a))
