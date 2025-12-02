import sys
from bisect import bisect_left, bisect_right

def sum_repeated_sequence_in_ranges(ranges_str: str) -> int:
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
    results = set()
    max_digits = len(str(global_max))
    # k = length of the repeating block
    for k in range(1, max_digits):  # at least one digit in block
        # t must be k-digit number without leading zeros
        t_min = 10**(k-1)
        t_max = 10**k - 1
        # m is number of repetitions, at least 2
        max_m = max_digits // k
        if max_m < 2:
            continue
        for m in range(2, max_m+1):
            # total length = k*m;
            total_len = k * m
            if total_len > max_digits:
                break
            # string repetition
            for t in range(t_min, t_max+1):
                rep_str = str(t) * m
                # skip numbers with leading zeros in t (already ensured) and convert
                rep = int(rep_str)
                if rep > global_max:
                    break  # further t will only increase rep
                results.add(rep)
    results_list = sorted(results)
    total = 0
    for a,b in ranges:
        i = bisect_left(results_list, a)
        j = bisect_right(results_list, b)
        total += sum(results_list[i:j])
    return total

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        with open(sys.argv[1], 'r') as f:
            input_str = f.read()
    else:
        input_str = sys.stdin.read()
    
    result = sum_repeated_sequence_in_ranges(input_str.strip())
    print(result)