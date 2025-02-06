def has_pair_with_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement  = target - num

        if complement in seen:
            return True

        seen[num]  = i
    return False


arr = [10, 15, 3, 7]
target = 17
print(has_pair_with_sum(arr, target))  # Вывод: True (10 + 7 = 17)
