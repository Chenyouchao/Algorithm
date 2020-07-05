def linear_search(li, val):
    for index, v in enumerate(li):
        if v == val:
            return index
    else:
        return None

def binary_search(li, val):
    # li从小到大排列

    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return None


li = [1,2,3,4,5,6,7,8,9]

print(binary_search(li, 5))

print(linear_search(li, 6))