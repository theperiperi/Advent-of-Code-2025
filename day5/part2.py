import sys

def count_total_fresh_ids(data: str) -> int:
    # Only the range section matters
    ranges_part = data.strip().split("\n\n")[0]

    # Parse ranges into (start, end)
    ranges = []
    for line in ranges_part.splitlines():
        start, end = map(int, line.split("-"))
        ranges.append((start, end))

    # Sort ranges by start
    ranges.sort()

    # Merge overlapping or adjacent ranges
    merged = []
    cur_start, cur_end = ranges[0]

    for start, end in ranges[1:]:
        if start <= cur_end + 1:  # overlap or adjacency
            cur_end = max(cur_end, end)
        else:
            merged.append((cur_start, cur_end))
            cur_start, cur_end = start, end

    merged.append((cur_start, cur_end))

    # Sum lengths of merged intervals
    total = sum(end - start + 1 for start, end in merged)

    return total

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        with open(sys.argv[1], "r") as f:
            input_text = f.read()
    else:
        input_text = sys.stdin.read()

    print(count_total_fresh_ids(input_text))