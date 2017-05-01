def binomial_permutations(n, m):
    """
    Number of unique permutations of (n+m) coins such that there are
    n tails and m heads.
    """
    solutions = [[0] * (m+1) for _ in range(n+1)]
    for x in range(1, n+1):
        solutions[x][0] = 1
    for y in range(1, m+1):
        solutions[0][y] = 1
    for x in range(1, n+1):
        for y in range(1, m+1):
            solutions[x][y] = solutions[x-1][y] + solutions[x][y-1]
    return solutions[n][m]

if __name__ == '__main__':
    print(binomial_permutations(20, 20))
