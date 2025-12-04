import sys

def max_k_joltage_from_line(s: str, k: int) -> int:
    """Compute maximum k-digit subsequence (in order) from a line."""
    s = s.strip()
    n = len(s)
    if k <= 0 or n < k:
        raise ValueError("Line too short for requested k")
    digits = s
    res_digits = []
    start = 0
    for t in range(k):
        # we must pick one digit from indices [start, n - (k - t)]
        end = n - (k - t)  # inclusive? compute slice end exclusive, so +1
        # candidates in digits[start:end+1]
        slice_ = digits[start:end+1]
        # find max digit and earliest occurrence
        max_d = max(slice_)
        idx = slice_.index(max_d) + start
        res_digits.append(max_d)
        start = idx + 1
    return int(''.join(res_digits))

def total_k_output_joltage(input_text: str, k: int) -> int:
    """Calculate total output joltage for all lines with k-digit subsequences."""
    lines = [line for line in input_text.splitlines() if line.strip()]
    per_line = [max_k_joltage_from_line(line, k) for line in lines]
    return sum(per_line)

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        with open(sys.argv[1], 'r') as f:
            input_text = f.read()
    else:
        input_text = sys.stdin.read()
    
    # Use k=12 as specified in the problem
    result = total_k_output_joltage(input_text, 12)
    print(result)