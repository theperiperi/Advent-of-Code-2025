import sys
from bisect import bisect_left, bisect_right

def sum_repeated_twice_in_ranges(ranges_str: str) -> int:
    # parse ranges
    ranges = []
    for part in ranges_str.split(','):
        part = part.strip()
        if not part:
            continue
        a,b = part.split('-')
        ranges.append((int(a), int(b)))
    if not ranges:
        return 0
    global_max = max(b for _,b in ranges)
    results = []
    # maximum digits of global_max
    max_digits = len(str(global_max))
    # k is digits in the repeated half
    for k in range(1, max_digits//2 + 1):
        base = 10**k
        coef = base + 1  # repeated number = t * (10^k + 1)
        # t must be k-digit (no leading zeros), so from 10^{k-1} .. 10^k -1
        t_min = 10**(k-1)
        t_max = min(10**k - 1, global_max // coef)
        if t_min > t_max:
            continue
        # iterate t in this limited range and make repeated numbers
        for t in range(t_min, t_max+1):
            rep = t * coef
            # rep <= global_max by construction
            results.append(rep)
    # Sort for efficient range checks
    results.sort()
    # For each range, sum repeated numbers within it
    total = 0
    for a,b in ranges:
        i = bisect_left(results, a)
        j = bisect_right(results, b)
        total += sum(results[i:j])
    return total

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        with open(sys.argv[1], 'r') as f:
            input_str = f.read()
    else:
        input_str = sys.stdin.read()
    
    result = sum_repeated_twice_in_ranges(input_str.strip())
    print(result)