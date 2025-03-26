import numpy as np
from collections import deque
import sys

def optimized_dssp_with_backtrack(str1, str2):
    """
    Optimized O(n^2) DP algorithm for DSSP with backtracking.
    Returns the minimum cycles and the synthesis decision trace.
    """
    m, n = len(str1), len(str2)
    cycle = "ACGT"
    INF = float('inf')

    dp = np.full((m + 1, n + 1, 4), INF)
    dp[0][0][0] = 0

    parent = {}
    queue = deque()
    queue.append((0, 0, 0))

    while queue:
        i, j, c = queue.popleft()
        cost = dp[i][j][c]
        next_c = (c + 1) % 4
        next_cost = cost + 1
        machine_char = cycle[c]

        # Option 1: Wait
        if next_cost < dp[i][j][next_c]:
            dp[i][j][next_c] = next_cost
            parent[(i, j, next_c)] = (i, j, c, ("-", "wait"))
            queue.append((i, j, next_c))

        # Option 2: Build Str1
        if i < m and str1[i] == machine_char:
            if next_cost < dp[i + 1][j][next_c]:
                dp[i + 1][j][next_c] = next_cost
                parent[(i + 1, j, next_c)] = (i, j, c, (machine_char, "Str1"))
                queue.append((i + 1, j, next_c))

        # Option 3: Build Str2
        if j < n and str2[j] == machine_char:
            if next_cost < dp[i][j + 1][next_c]:
                dp[i][j + 1][next_c] = next_cost
                parent[(i, j + 1, next_c)] = (i, j, c, (machine_char, "Str2"))
                queue.append((i, j + 1, next_c))

    final_state = min([(dp[m][n][c], m, n, c) for c in range(4)])
    min_cycles, i, j, c = final_state

    synthesis_order = []
    while (i, j, c) in parent:
        prev_i, prev_j, prev_c, action = parent[(i, j, c)]
        synthesis_order.append(action)
        i, j, c = prev_i, prev_j, prev_c

    synthesis_order.reverse()
    return int(min_cycles), synthesis_order


# ===== Command Line Usage =====
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <Str1> <Str2>")
        sys.exit(1)

    str1 = sys.argv[1].upper()
    str2 = sys.argv[2].upper()

    min_cycles, synthesis = optimized_dssp_with_backtrack(str1, str2)

    print(f"\nMinimum synthesis cycles: {min_cycles}")
    print("Synthesis schedule:")
    for step in synthesis:
        print(step)
