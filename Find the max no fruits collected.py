class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        diag = sum(fruits[i][i] for i in range(n))

        dpb = [[0]* n for _ in range(n)]
        dpb[0][n - 1] = fruits [0] [n - 1]
        for i in range(n):
            for j in range(n-1, n-2-i, -1):
                if j>i or (i == j == n - 1):
                    for di, dj in [(-1, -1), (-1, 0),(-1, 1)]:
                        pi, pj = i + di, j + dj
                        if 0 <= pi < n and 0 <= pj < n:
                            dpb[i][j] = max(dpb[i][j], dpb[pi][pj] + fruits[i][j])

        dpc = [[0] * n for _ in range(n)]
        dpc[n - 1] [0] = fruits[n - 1] [0]
        for j in range(n):
            for i in range(n-1, n-2-j, -1):
                if i > j or (i == j == n - 1):
                    for di, dj in [(-1, -1), (0, -1), (1,-1)]:
                        pi, pj = i + di, j + dj
                        if 0 <= pi < n and 0 <= pj < n:
                            dpc[i] [j] = max(dpc[i][j], dpc[pi] [pj] + fruits[i] [j])

        return diag + dpb[n - 1] [n - 1] + dpc[n - 1] [n - 1] - 2 * fruits[n - 1] [n - 1]