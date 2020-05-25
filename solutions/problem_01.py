def sum_to_k(arr, k):
    addends = set()
    for num in arr:
        if (k - num) in addends:
            return True
        addends.add(num)
    return False

assert sum_to_k([10, 15, 3, 7], 17)
assert not sum_to_k([], 5)
assert not sum_to_k([2], 2)
assert sum_to_k([3, 0], 3)
