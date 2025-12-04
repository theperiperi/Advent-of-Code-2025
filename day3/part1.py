import sys

def max_joltage_from_line(s: str) -> int:
    """Return the maximum two-digit joltage formed by choosing two digits in order from s."""
    s = s.strip()
    if not s or len(s) < 2:
        return 0
    # Efficient linear approach: track max digit to the right for each position.
    n = len(s)
    digits = [int(ch) for ch in s]
    # suffix_max[j] = maximum digit in digits[j:]
    suffix_max = [0] * n
    suffix_max[-1] = digits[-1]
    for i in range(n-2, -1, -1):
        suffix_max[i] = max(digits[i], suffix_max[i+1])
    best = 0
    # For each i as the first chosen battery, we need max digit in positions > i
    # So compare digits[i]*10 + max(digits[i+1:])
    for i in range(n-1):
        candidate = digits[i] * 10 + suffix_max[i+1]
        if candidate > best:
            best = candidate
    return best

def total_output_joltage(input_text: str) -> int:
    """Calculate total output joltage for all lines."""
    lines = [line for line in input_text.splitlines() if line.strip()]
    total = sum(max_joltage_from_line(line) for line in lines)
    return total

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        with open(sys.argv[1], 'r') as f:
            input_text = f.read()
    else:
        input_text = sys.stdin.read()
    
    result = total_output_joltage(input_text)
    print(result)