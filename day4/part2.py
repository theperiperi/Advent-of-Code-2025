import sys

def total_removed_paper(grid_lines):
    """
    grid_lines: list of strings like ['..@@.@@@@.', '@@@.@.@.@@', ...]
    returns: total_removed (int)
    """
    h = len(grid_lines)
    w = len(grid_lines[0]) if h > 0 else 0
    grid = [list(row) for row in grid_lines]

    dirs = [(-1, -1), (-1, 0), (-1, 1),
            ( 0, -1),          ( 0, 1),
            ( 1, -1), ( 1, 0), ( 1, 1)]

    total_removed = 0

    while True:
        removable = []

        # Find all currently accessible rolls
        for r in range(h):
            for c in range(w):
                if grid[r][c] != '@':
                    continue
                adj = 0
                for dr, dc in dirs:
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < h and 0 <= cc < w and grid[rr][cc] == '@':
                        adj += 1
                if adj < 4:
                    removable.append((r, c))

        # Stop if no more can be removed
        if not removable:
            break

        # Remove them all at once
        for r, c in removable:
            grid[r][c] = '.'

        total_removed += len(removable)

    return total_removed

def solve_from_string(input_text):
    """Parse input and calculate total removed paper rolls."""
    lines = [line.rstrip("\n") for line in input_text.splitlines() if line.strip()]
    return total_removed_paper(lines)

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        with open(sys.argv[1], 'r') as f:
            input_text = f.read()
    else:
        input_text = sys.stdin.read()
    
    result = solve_from_string(input_text)
    print(result)
