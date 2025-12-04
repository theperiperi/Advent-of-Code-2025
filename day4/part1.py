import sys

def count_accessible(grid_lines):
    """Count accessible paper rolls ('@') where fewer than 4 adjacent '@' in 8 neighbors."""
    h = len(grid_lines)
    w = len(grid_lines[0]) if h > 0 else 0
    grid = [list(line) for line in grid_lines]
    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    accessible = [[False]*w for _ in range(h)]
    total = 0
    for r in range(h):
        for c in range(w):
            if grid[r][c] != '@':
                continue
            adj = 0
            for dr,dc in dirs:
                rr,cc = r+dr, c+dc
                if 0 <= rr < h and 0 <= cc < w:
                    if grid[rr][cc] == '@':
                        adj += 1
            if adj < 4:
                accessible[r][c] = True
                total += 1
    return total

def solve_from_string(input_text):
    """Parse input and count accessible paper rolls."""
    lines = [line.rstrip("\n") for line in input_text.splitlines() if line.strip()]
    return count_accessible(lines)

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        with open(sys.argv[1], 'r') as f:
            input_text = f.read()
    else:
        input_text = sys.stdin.read()
    
    result = solve_from_string(input_text)
    print(result)