import sys

def count_zero_hits(lines):
    pos = 50
    count = 0
    for line in lines:
        s = line.strip()
        if not s: continue
        dir_char = s[0].upper()
        try:
            dist = int(s[1:])
        except ValueError:
            raise ValueError(f"Bad line: {s}")
        if dir_char == 'R':
            pos = (pos + dist) % 100
        elif dir_char == 'L':
            pos = (pos - dist) % 100
        else:
            raise ValueError(f"Bad direction in line: {s}")
        if pos == 0:
            count += 1
    return count

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        with open(sys.argv[1], 'r') as f:
            lines = f.readlines()
    else:
        lines = sys.stdin.read().splitlines()

    print(count_zero_hits(lines))
