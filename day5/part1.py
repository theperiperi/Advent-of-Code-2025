import sys

def count_fresh_ingredients(data: str) -> int:
    # Split into two parts: ranges and ingredient IDs
    ranges_part, ids_part = data.strip().split("\n\n")

    # Parse ranges
    ranges = []
    for line in ranges_part.splitlines():
        start, end = map(int, line.split("-"))
        ranges.append((start, end))

    # Parse ingredient IDs
    ids = [int(line.strip()) for line in ids_part.splitlines() if line.strip()]

    # Check freshness
    fresh_count = 0
    for id_ in ids:
        if any(start <= id_ <= end for start, end in ranges):
            fresh_count += 1

    return fresh_count

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        with open(sys.argv[1], "r") as f:
            input_text = f.read()
    else:
        input_text = sys.stdin.read()

    print(count_fresh_ingredients(input_text))