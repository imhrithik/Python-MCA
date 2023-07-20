n = 4
out = [[" " for i in range(2*n+1)] for j in range(n)]

for i in range(n):
    mid = n
    out[i][mid] = 1
    for j in range(i):
        out[i][mid - i + j] = i + 1 - j
        out[i][mid + i - j] = i + 1 - j

for i in out:
    for j in i:
        print(j, end=" ")
    print("")

n = 3

out = [[" " for i in range(2*n+1)] for j in range(2 * n - 1)]

for i in range(n):
    mid = n
    out[i][mid] = "*"
    out[2 * n - 2 - i][mid] = "*"
    for j in range(i):
        out[i][mid - i + j] = "*"
        out[i][mid + i - j] = "*"
        out[2 * n - 2 - i][mid + i - j] = "*"
        out[2 * n - 2 - i][mid - i + j] = "*"

for i in out:
    print(" " * (n - 1), end="")
    for j in i:
        print(j, end=" ")
    print("")