# Given a list of integers, find the largest sum of two pairs of digits such that the pair has an equal digit sum
def equal_digit_sum(nums) -> int:
    best = {}
    best_sum = -1

    def num_to_sum(num)-> int:
        res = 0
        for c in str(num):
            res += int(c)
        return res

    for num in nums:
        digits = num_to_sum(num)
        if digits not in best:
            best[digits] = num
        else:
            best_sum = max(best_sum, best[digits] + num)
            best[digits] = max(best[digits], num)
    print(best)
    return best_sum

print(equal_digit_sum([10, 11,12]))