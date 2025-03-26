import numpy as np

def dp_scs_synthesis(str1, str2, str3, str4):
    """Computes the shortest synthesis sequence for four DNA strands using DP."""
    m, n, p, q = len(str1), len(str2), len(str3), len(str4)

    # Step 1: Initialize 4D DP table with infinity values
    dp = np.full((m + 1, n + 1, p + 1, q + 1), float('inf'))

    # Base case: Empty sequences have an SCS length of 0
    dp[0][0][0][0] = 0

    # Step 2: Fill the DP table
    for i in range(m + 1):
        for j in range(n + 1):
            for k in range(p + 1):
                for l in range(q + 1):
                    if i == 0 and j == 0 and k == 0 and l == 0:
                        continue  # Already set

                    options = []

                    # Extend one from (Str1, Str2) and one from (Str3, Str4) if they match
                    if i > 0 and k > 0 and str1[i - 1] == str3[k - 1]:
                        options.append(dp[i - 1][j][k - 1][l] + 1)
                    if i > 0 and l > 0 and str1[i - 1] == str4[l - 1]:
                        options.append(dp[i - 1][j][k][l - 1] + 1)
                    if j > 0 and k > 0 and str2[j - 1] == str3[k - 1]:
                        options.append(dp[i][j - 1][k - 1][l] + 1)
                    if j > 0 and l > 0 and str2[j - 1] == str4[l - 1]:
                        options.append(dp[i][j - 1][k][l - 1] + 1)

                    # Extend a single sequence if no match occurs
                    if i > 0:
                        options.append(dp[i - 1][j][k][l] + 1)
                    if j > 0:
                        options.append(dp[i][j - 1][k][l] + 1)
                    if k > 0:
                        options.append(dp[i][j][k - 1][l] + 1)
                    if l > 0:
                        options.append(dp[i][j][k][l - 1] + 1)

                    # Assign the minimum possible value
                    dp[i][j][k][l] = min(options)

    # Step 3: Retrieve the SCS length from DP table
    scs_length = dp[m][n][p][q]

    return scs_length, dp


def backtrack_scs_synthesis(str1, str2, str3, str4, dp):
    """Backtracks through the DP table to reconstruct the optimal synthesis sequence."""
    i, j, k, l = len(str1), len(str2), len(str3), len(str4)
    synthesis_sequence = ""
    synthesis_steps = []

    while i > 0 or j > 0 or k > 0 or l > 0:
        step_info = ""

        if i > 0 and j > 0 and k > 0 and l > 0 and str1[i - 1] == str2[j - 1] == str3[k - 1] == str4[l - 1]:
            synthesis_sequence = str1[i - 1] + str1[i - 1] + synthesis_sequence
            step_info = f"Extended {str1[i - 1]} in Str1, Str2, Str3, Str4"
            i -= 1
            j -= 1
            k -= 1
            l -= 1
        else:
            options = []
            if i > 0 and k > 0 and str1[i - 1] == str3[k - 1]:
                options.append((dp[i - 1][j][k - 1][l], str1[i - 1], "Str1 and Str3"))
            if i > 0 and l > 0 and str1[i - 1] == str4[l - 1]:
                options.append((dp[i - 1][j][k][l - 1], str1[i - 1], "Str1 and Str4"))
            if j > 0 and k > 0 and str2[j - 1] == str3[k - 1]:
                options.append((dp[i][j - 1][k - 1][l], str2[j - 1], "Str2 and Str3"))
            if j > 0 and l > 0 and str2[j - 1] == str4[l - 1]:
                options.append((dp[i][j - 1][k][l - 1], str2[j - 1], "Str2 and Str4"))

            if i > 0:
                options.append((dp[i - 1][j][k][l], str1[i - 1], "Str1"))
            if j > 0:
                options.append((dp[i][j - 1][k][l], str2[j - 1], "Str2"))
            if k > 0:
                options.append((dp[i][j][k - 1][l], str3[k - 1], "Str3"))
            if l > 0:
                options.append((dp[i][j][k][l - 1], str4[l - 1], "Str4"))

            best_choice = min(options, key=lambda x: x[0])
            synthesis_sequence = best_choice[1] + synthesis_sequence
            step_info = f"Extended {best_choice[1]} in {best_choice[2]}"

            if "Str1" in best_choice[2]:
                i -= 1
            if "Str2" in best_choice[2]:
                j -= 1
            if "Str3" in best_choice[2]:
                k -= 1
            if "Str4" in best_choice[2]:
                l -= 1

        synthesis_steps.append(step_info)

    return synthesis_sequence, synthesis_steps


# Example DNA Sequences
dna1 = "GATTACA"
dna2 = "GTACGGA"
dna3 = "CAGTTAC"
dna4 = "GCTAGGA"

# Compute the DP table and extract the optimized synthesis sequence
scs_length, dp_table = dp_scs_synthesis(dna1, dna2, dna3, dna4)
optimized_synthesis_sequence, synthesis_steps = backtrack_scs_synthesis(dna1, dna2, dna3, dna4, dp_table)

# Print results
print(f"Optimized SCS Length: {scs_length}")
print(f"Optimized Synthesis Sequence: {optimized_synthesis_sequence}")
print("Synthesis Steps:")
for step in synthesis_steps:
    print(step)
