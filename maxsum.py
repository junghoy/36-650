
# Define the function maxSubSum

def maxSubSum(number_list):
    best = current = 0
    for ii in number_list:
        current = max(current + ii, 0)
        best = max(best, current)
    return best

    