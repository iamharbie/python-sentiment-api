# Dyanmic Programing on Trees


```
dp[v] = size of max independent set rooted at v
```

Base: dp[leaf] = 1

```
dp[v] = max(1 + (summation(grandnode) dp[g]), (summation(child) dp[c]))