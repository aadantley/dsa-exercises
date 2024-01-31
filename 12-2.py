def golomb(n, memo={}):
    if n == 1:
        return 1
    
    if n in memo.keys():
        return memo[n]
    
    else:
        memo[n] = 1 + golomb(golomb(n - golomb(n-1)))
        return 1 + golomb(n - golomb(golomb(n-1)))
    
print(golomb(7))