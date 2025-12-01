import sys

def count_zero_clicks(lines):
    pos = 50  # starting position
    total_zero_hits = 0

    for raw in lines:
        s = raw.strip()
        if not s:
            continue

        direction = s[0].upper()
        k = int(s[1:])

        if direction == 'R':
            # count zero hits while moving right k steps from pos
            if pos == 0:
                first = 100
            else:
                first = (100 - pos) % 100

            if first != 0 and first <= k:
                total_zero_hits += 1 + (k - first) // 100

            pos = (pos + k) % 100

        elif direction == 'L':
            # count zero hits while moving left k steps from pos
            if pos == 0:
                first = 100
            else:
                first = pos

            if first != 0 and first <= k:
                total_zero_hits += 1 + (k - first) // 100

            pos = (pos - k) % 100

        else:
            raise ValueError(f"Bad direction: {s}")

    return total_zero_hits


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        with open(sys.argv[1]) as f:
            lines = f.readlines()
    else:
        lines = sys.stdin.read().splitlines()

    print(count_zero_clicks(lines))
