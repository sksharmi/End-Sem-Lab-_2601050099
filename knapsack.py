def knapsack(w, v, cap):
    n = len(w)
    dp = [[0]*(cap+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for c in range(cap+1):
            if w[i-1] <= c:
                dp[i][c] = max(dp[i-1][c],
                                v[i-1] + dp[i-1][c-w[i-1]])
            else:
                dp[i][c] = dp[i-1][c]
    chosen=[]
    c=cap
    for i in range(n,0,-1):
        if dp[i][c] != dp[i-1][c]:
            chosen.append(i)
            c -= w[i-1]
    chosen.reverse()
    return dp, chosen
n = int(input("Number of items: "))
w = list(map(int,input("Weights: ").split()))
v = list(map(int,input("Values: ").split()))
cap = int(input("Capacity: "))
dp, chosen = knapsack(w,v,cap)
print("Maximum value:", dp[n][cap])
print("Selected item numbers:", chosen)
print("DP table:")
for row in dp: print(row)
print("Time: O(nW), Space: O(nW)")