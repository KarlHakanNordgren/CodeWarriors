# Kadane's algorithm
# https://youtu.be/86CQq3pKSUw
# could be cool to visualise

def max_sequence(arr: list) -> int:
    current_sum = 0
    best_sum = 0
    for i in arr:
        current_sum = max(0, current_sum + i)
        best_sum = max(best_sum, current_sum)
    return best_sum


print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))