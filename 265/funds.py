
IMPOSSIBLE = 'Mission impossible. No one can contribute.'

def max_fund(village):
    """Find a contiguous subarray with the largest sum."""
    max_sum = 0
    run_sum = 0
    best_start = 0
    best_end = 0
    for end, entry in enumerate(village):
        if run_sum <= 0:
            start = end
            run_sum = entry

        else:
            run_sum += entry

        if run_sum > max_sum:
            max_sum = run_sum
            best_start = start
            best_end = end + 1
    if max_sum <= 0:
        print(IMPOSSIBLE)
        return (0, 0, 0)

    return (max_sum, best_start + 1, best_end) 